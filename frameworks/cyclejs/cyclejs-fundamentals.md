# Cycle.js Fundamentals Notes

Notes from the course at [egghead.io](https://egghead.io).

## 1. The Cycle.js principle: separating logic from effects

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>JS Bin</title>
</head>
<body>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/rxjs/4.0.6/rx.all.js"></script>
  <script src="https://rawgit.com/cyclejs/cycle-core/v6.0.0/dist/cycle.js"></script>
  <script src="https://rawgit.com/cyclejs/cycle-dom/v9.0.1/dist/cycle-dom.js"></script>
  <script src="https://rawgit.com/cyclejs/cycle-http-driver/v7.0.0/dist/cycle-http-driver.min.js"></script>
  <script src="https://rawgit.com/cyclejs/isolate/v1.1.1/dist/cycle-isolate.js"></script>

  <div id="app">

  </div>
</body>
</html>
```

```javascript
// Logic:
Rx.Observable.timer(0, 1000)
  .map(i => `Seconds elapsed: ${i}`)
// Effects:
  .subscribe(text => {
    const container = document.querySelector('#app');
    container.textContent = text;
  })
```

Effects is any change to the external world and changes live in subscribes. Logic
on the other hand is event streams. The logic is functional and the effects are
imperative.

## 2. Main function and effects functions

```javascript
// Logic (functional)
function main() {
  return Rx.Observable.timer(0, 1000)
    .map(i => `Seconds elapsed ${i}`);
}

// Effects (imperative)
function DOMEffect(text$) {
  text$.subscribe(text => {
    document.querySelector('#app').textContent = text;
  });
}

function consoleLogEffect(text$) {
  text$.subscribe(text => console.log(text));
}

const sink = main();
DOMEffect(sink);
consoleLogEffect(sink);
```

## 3. Customizing effects from the main function

What if we want the two effects to display different strings?

```javascript
// Logic (functional)
function main() {
  return {
    DOM: Rx.Observable.timer(0, 1000)
          .map(i => `Seconds elapsed ${i}`),
    Log: Rx.Observable.timer(0, 2000)
          .map(i => 2*i)
  };
}

// Effects (imperative)
function DOMEffect(text$) {
  text$.subscribe(text => {
    document.querySelector('#app').textContent = text;
  });
}

function consoleLogEffect(text$) {
  text$.subscribe(text => console.log(text));
}

// Tie together main with effects
const sink = main();
DOMEffect(sink.DOM);
consoleLogEffect(sink.Log);
```

## 4. Introducing run() and driver functions

```javascript
// Logic (functional)
function main() {
  return {
    DOM: Rx.Observable.timer(0, 1000)
          .map(i => `Seconds elapsed ${i}`),
    Log: Rx.Observable.timer(0, 2000)
          .map(i => 2*i)
  };
}

// source: input (read) effects
// sink: output (write) effects

// Effects (imperative)
function DOMEffect(text$) {
  text$.subscribe(text => {
    document.querySelector('#app').textContent = text;
  });
}

function consoleLogEffect(text$) {
  text$.subscribe(text => console.log(text));
}

function run(mainFn, drivers) {
  // Tie together main with effects
  const sinks = mainFn();
  Object.keys(drivers).forEach(key => {
    drivers[key](sinks[key]);
  });
}

const drivers = {
  DOM: DOMEffect,
  Log: consoleLogEffect,
};

run(main, drivers)
```

## 5. Read effects from the DOM: click events

```javascript
// Logic (functional)
function main(DOMSource) {
  const click$ = DOMSource;
  return {
    DOM: click$
      .startWith(null)
      .flatMapLatest(() =>
        Rx.Observable.timer(0, 1000)
          .map(i => `Seconds elapsed ${i}`)
      ),
    Log: Rx.Observable.timer(0, 2000)
          .map(i => 2*i)
  };
}

// source: input (read) effects
// sink: output (write) effects

// Effects (imperative)
function DOMDriver(text$) {
  text$.subscribe(text => {
    document.querySelector('#app').textContent = text;
  });
  const DOMSource = Rx.Observable.fromEvent(document, 'click');
  return DOMSource;
}

function consoleLogDriver(text$) {
  text$.subscribe(text => console.log(text));
}

// Cycle:
// bProxy = ...
// a = f(bProxy)
// b = g(a)
// bProxy.imitate(b)

function run(mainFn, drivers) {
  // Tie together main with effects
  const proxyDOMSource = new Rx.Subject();
  const sinks = mainFn(proxyDOMSource);
  const DOMSource = drivers.DOM(sinks.DOM);
  DOMSource.subscribe(click => proxyDOMSource.onNext(click));
  // Object.keys(drivers).forEach(key => {
  //   drivers[key](sinks[key]);
  // });
}

const drivers = {
  DOM: DOMDriver,
  Log: consoleLogDriver,
};

run(main, drivers)
```

## 6. Generalizing run() function for more types of sources

```javascript
// Logic (functional)
function main(sources) {
  const click$ = sources.DOM;
  return {
    DOM: click$
      .startWith(null)
      .flatMapLatest(() =>
        Rx.Observable.timer(0, 1000)
          .map(i => `Seconds elapsed ${i}`)
      ),
    Log: Rx.Observable.timer(0, 2000)
          .map(i => 2*i)
  };
}

// source: input (read) effects
// sink: output (write) effects

// Effects (imperative)
function DOMDriver(text$) {
  text$.subscribe(text => {
    document.querySelector('#app').textContent = text;
  });
  const DOMSource = Rx.Observable.fromEvent(document, 'click');
  return DOMSource;
}

function consoleLogDriver(text$) {
  text$.subscribe(text => console.log(text));
}

// function run(mainFn, drivers) {
//   const proxySources = {};
//   Object.keys(drivers).forEach(key => {
//     proxySources[key] = new Rx.Subject();
//   });
//   const sinks = mainFn(proxySources);
//   Object.keys(drivers).forEach(key => {
//     const source = drivers[key](sinks[key]);
//     source.subscribe(x => proxySources[key].onNext(x));
//   });
// }

const drivers = {
  DOM: DOMDriver,
  Log: consoleLogDriver,
};

Cycle.run(main, drivers)
```

## 7. Making our toy DOM Driver more flexible

```javascript
// Logic (functional)
function main(sources) {
  const click$ = sources.DOM;
  return {
    DOM: click$
      .startWith(null)
      .flatMapLatest(() =>
        Rx.Observable.timer(0, 1000)
          .map(i => {
            return {
              tagName: 'H1',
              children: [
                {
                  tagName: 'SPAN',
                  children: [
                    `Seconds elapsed: ${i}`
                  ]
                }                
              ]
            };
          })
      ),
    Log: Rx.Observable.timer(0, 2000)
          .map(i => 2*i)
  };
}

// source: input (read) effects
// sink: output (write) effects


// Effects (imperative)
function DOMDriver(obj$) {
  function createElement(obj) {
    const element = document.createElement(obj.tagName);
    console.log("pm debug createElement", obj);
    obj.children
      .filter(c => typeof c === 'object')
      .map(createElement)
      .forEach(c => element.appendChild(c));
    obj.children
      .filter(c => typeof c === 'string')
      .forEach(c => element.innerHTML += c);
    return element;
  }



  obj$.subscribe(obj => {
    const container = document.querySelector('#app');
    container.innerHTML = '';
    const element = createElement(obj);
    console.log("pm debug DOMDriver subscribe", obj, element);
    container.appendChild(element);
  });
  const DOMSource = Rx.Observable.fromEvent(document, 'click');
  return DOMSource;
}

function consoleLogDriver(text$) {
  text$.subscribe(text => console.log(text));
}

// function run(mainFn, drivers) {
//   const proxySources = {};
//   Object.keys(drivers).forEach(key => {
//     proxySources[key] = new Rx.Subject();
//   });
//   const sinks = mainFn(proxySources);
//   Object.keys(drivers).forEach(key => {
//     const source = drivers[key](sinks[key]);
//     source.subscribe(x => proxySources[key].onNext(x));
//   });
// }

const drivers = {
  DOM: DOMDriver,
  Log: consoleLogDriver,
};

Cycle.run(main, drivers)
```

## 8. Fine-grained control over the DOM Source

What if we want to react on hover. App logic should live in main.

```javascript
// Logic (functional)
function main(sources) {
  // eventType: click/mouseover
  const click$ = sources.DOM.selectEvents('span', 'mouseover');

  return {
    DOM: click$
      .startWith(null)
      .flatMapLatest(() =>
        Rx.Observable.timer(0, 1000)
          .map(i => {
            return {
              tagName: 'H1',
              children: [
                {
                  tagName: 'SPAN',
                  children: [
                    `Seconds elapsed: ${i}`
                  ]
                }                
              ]
            };
          })
      ),
    Log: Rx.Observable.timer(0, 2000)
          .map(i => 2*i)
  };
}

// source: input (read) effects
// sink: output (write) effects



// Effects (imperative)
function DOMDriver(obj$) {
  function createElement(obj) {
    const element = document.createElement(obj.tagName);
    obj.children
      .filter(c => typeof c === 'object')
      .map(createElement)
      .forEach(c => element.appendChild(c));
    obj.children
      .filter(c => typeof c === 'string')
      .forEach(c => element.innerHTML += c);
    return element;
  }



  obj$.subscribe(obj => {
    const container = document.querySelector('#app');
    container.innerHTML = '';
    const element = createElement(obj);
    container.appendChild(element);
  });
  const DOMSource = {
    selectEvents: function(tagName, eventType) {
      return Rx.Observable.fromEvent(document, eventType)
              .filter(ev => ev.target.tagName === tagName.toUpperCase());
    }
  };
  return DOMSource;
}

function consoleLogDriver(text$) {
  text$.subscribe(text => console.log(text));
}

// function run(mainFn, drivers) {
//   const proxySources = {};
//   Object.keys(drivers).forEach(key => {
//     proxySources[key] = new Rx.Subject();
//   });
//   const sinks = mainFn(proxySources);
//   Object.keys(drivers).forEach(key => {
//     const source = drivers[key](sinks[key]);
//     source.subscribe(x => proxySources[key].onNext(x));
//   });
// }

const drivers = {
  DOM: DOMDriver,
  Log: consoleLogDriver,
};

Cycle.run(main, drivers)
```

## 9. Hyperscript as our alternative to template languages

```javascript
function h(tagName, children) {
  return {
    tagName: tagName,
    children: children
  };
}

function h1(children) {
  return h('H1', children);
}

function span(children) {
  return h('SPAN', children);
}

// Logic (functional)
function main(sources) {
  // eventType: click/mouseover
  const click$ = sources.DOM.selectEvents('span', 'mouseover');

  return {
    DOM: click$
      .startWith(null)
      .flatMapLatest(() =>
        Rx.Observable.timer(0, 1000)
          .map(i => {
            return h1([
                span([
                  `Seconds elapsed: ${i}`
                ])
              ]);
          })
      ),
    Log: Rx.Observable.timer(0, 2000)
          .map(i => 2*i)
  };
}

// source: input (read) effects
// sink: output (write) effects



// Effects (imperative)
function DOMDriver(obj$) {
  function createElement(obj) {
    const element = document.createElement(obj.tagName);
    obj.children
      .filter(c => typeof c === 'object')
      .map(createElement)
      .forEach(c => element.appendChild(c));
    obj.children
      .filter(c => typeof c === 'string')
      .forEach(c => element.innerHTML += c);
    return element;
  }



  obj$.subscribe(obj => {
    const container = document.querySelector('#app');
    container.innerHTML = '';
    const element = createElement(obj);
    container.appendChild(element);
  });
  const DOMSource = {
    selectEvents: function(tagName, eventType) {
      return Rx.Observable.fromEvent(document, eventType)
              .filter(ev => ev.target.tagName === tagName.toUpperCase());
    }
  };
  return DOMSource;
}

function consoleLogDriver(text$) {
  text$.subscribe(text => console.log(text));
}

const drivers = {
  DOM: DOMDriver,
  Log: consoleLogDriver,
};

Cycle.run(main, drivers)
```

## 10. From toy DOM Driver to real DOM Driver

```javascript
const {h, h1, span, makeDOMDriver} = CycleDOM;

// Logic (functional)
function main(sources) {
  // eventType: click/mouseover
  const click$ = sources.DOM.select('span').events('mouseover');

  return {
    DOM: click$
      .startWith(null)
      .flatMapLatest(() =>
        Rx.Observable.timer(0, 1000)
          .map(i => {
            return h1([
                span([
                  `Seconds elapsed: ${i}`
                ])
              ]);
          })
      ),
    Log: Rx.Observable.timer(0, 2000)
          .map(i => 2*i)
  };
}

function consoleLogDriver(text$) {
  text$.subscribe(text => console.log(text));
}

const drivers = {
  DOM: makeDOMDriver('#app'),
  Log: consoleLogDriver,
};

Cycle.run(main, drivers)
```

## 11. Hello World in Cycle.js

```javascript
const {label, input, h1, hr, div, makeDOMDriver} = CycleDOM;

// Logic (functional)
function main(sources) {
  const inputEv$ = sources.DOM.select('.field').events('input');
  const name$ = inputEv$.map(ev => ev.target.value).startWith('');
  return {
    DOM: name$.map(name =>
      div([
        label('Name:'),
        input('.field', {type: 'text'}),
        hr(),
        h1(`Hello ${name}!`)
      ])
    )
  }
}

const drivers = {
  DOM: makeDOMDriver('#app')
};

Cycle.run(main, drivers)
```

## 12. An interactive counter in cycle.js

Using `scan` is the way you maintain state with cycle.js. You keep
previous values around and update those.

```javascript
const {button, p, label, div, makeDOMDriver} = CycleDOM;

// Logic (functional)
function main(sources) {
  const decrementClick$ = sources.DOM
    .select('.decrement').events('click');
  const incrementClick$ = sources.DOM
    .select('.increment').events('click');
  const decrementAction$ = decrementClick$.map(ev => -1);
  const incrementAction$ = incrementClick$.map(ev => +1);

  const number$ = Rx.Observable.of(10)
    .merge(decrementAction$).merge(incrementAction$);
  return {
    DOM: number$.map(number =>
      div([
        button('.decrement', 'Decrement'),
        button('.increment', 'Increment'),
        p([
          label(String(number))
        ])
      ])
    )
  }
}

const drivers = {
  DOM: makeDOMDriver('#app')
};

Cycle.run(main, drivers)
```

## 13. Using the HTTP Driver

```javascript
const {button, h1, h4, a, div, makeDOMDriver} = CycleDOM;
const {makeHTTPDriver} = CycleHTTPDriver;

// 1. button clicked (DOM read - sources)
// 2. send request (write HTTP - sinks)
// 3. receive response (read HTTP - sources)
// 4. display data (write DOM - sinks)

function main(sources) {
  const clickEvent$ = sources.DOM
    .select('.get-first').events('click');

  const apiUrl = 'http://jsonplaceholder.typicode.com/users/1';
  const request$ = clickEvent$.map(() => {
    return {
      url: apiUrl,
      method: 'GET'
    };
  });

  // response stream stream
  const response$$ = sources.HTTP
    .filter(response$ => response$.request.url === apiUrl);

  const response$ = response$$.switch();
  const firstUser$ = response$.map(response => response.body).startWith(null);

  const sinks = {
    DOM: firstUser$.map(firstUser =>
      div([
        button('.get-first', 'Get first user'),
        (firstUser == null ? null : div('.user-details', [
          h1('.user-name', firstUser.name),
          h4('.user-email', firstUser.email),
          a('.user-website', {href: 'google.com'}, firstUser.website)
        ]))
      ])
    ),
    HTTP: request$,
  };

  return sinks;
}

const drivers = {
  DOM: makeDOMDriver('#app'),
  HTTP: makeHTTPDriver(),
};

Cycle.run(main, drivers)
```

## 14. Body-Mass Index calculator built in Cycle.js

```javascript
const {div, input, label, h2, makeDOMDriver} = CycleDOM;

// 1. detect slider change (DOM source)
// 2. recalculate BMI
// 3. display BMI (DOM sink)

function main(sources) {
  const changeWeight$ = sources.DOM.select('.weight')
    .events('input')
    .map(ev => ev.target.value);
  const changeHeight$ = sources.DOM.select('.height')
    .events('input')
    .map(ev => ev.target.value);

  const state$ = Rx.Observable.combineLatest(
    changeWeight$.startWith(70),
    changeHeight$.startWith(170),
    (weight, height) => {
      const heightMeters = height * 0.01;
      const bmi = Math.round(weight / (heightMeters * heightMeters));
      return {weight: weight, height: height, bmi: bmi};
    }
  );

  const sinks = {
    DOM: state$.map(state =>
      div([
        div([
          label('Weight: ' + state.weight + 'kg'),
          input('.weight', {type: 'range', min: 40, max: 150, value: state.weight})
        ]),

        div([
          label('Height: ' + state.height + 'cm'),
          input('.height', {type: 'range', min: 140, max: 220, value: state.height})
        ]),

        h2('BMI is ' + state.bmi)
      ])
    ),
  };

  return sinks;
}

const drivers = {
  DOM: makeDOMDriver('#app'),
};

Cycle.run(main, drivers)
```

## 15. Model-View-Intent pattern for separation of concerns

```javascript
const {div, input, label, h2, makeDOMDriver} = CycleDOM;

function intent(DOMSource) {
  const changeWeight$ = DOMSource.select('.weight')
    .events('input')
    .map(ev => ev.target.value);
  const changeHeight$ = DOMSource.select('.height')
    .events('input')
    .map(ev => ev.target.value);
  return {changeWeight$, changeHeight$};
}

function model(changeWeight$, changeHeight$) {
  return Rx.Observable.combineLatest(
    changeWeight$.startWith(70),
    changeHeight$.startWith(170),
    (weight, height) => {
      const heightMeters = height * 0.01;
      const bmi = Math.round(weight / (heightMeters * heightMeters));
      return {weight: weight, height: height, bmi: bmi};
    }
  );  
}

function view(state$) {
  return state$.map(state =>
      div([
        div([
          label('Weight: ' + state.weight + 'kg'),
          input('.weight', {type: 'range', min: 40, max: 150, value: state.weight})
        ]),

        div([
          label('Height: ' + state.height + 'cm'),
          input('.height', {type: 'range', min: 140, max: 220, value: state.height})
        ]),

        h2('BMI is ' + state.bmi)
      ])
    );
}

function main(sources) {
  const {changeWeight$, changeHeight$} = intent(sources.DOM);
  const state$ = model(changeWeight$, changeHeight$);
  const vtree$ = view(state$);

  const sinks = {
    DOM: vtree$
  };

  return sinks;
}

const drivers = {
  DOM: makeDOMDriver('#app'),
};

Cycle.run(main, drivers)
```

## 16. Our first component: a labeled slider

How can we reuse code for the height/weight sliders. Can we create a generic
slider component.

```javascript
const {div, input, label, h2, makeDOMDriver} = CycleDOM;

function intent(DOMSource) {
  return DOMSource.select('.slider').events('input')
    .map(ev => ev.target.value);
}


function model(change$, props$) {
  const initialValue$ = props$.map(props => props.init).first();
  const value$ = initialValue$.concat(change$);
  return Rx.Observable.combineLatest(
    value$,
    props$,
    (value, props) => {
      return {
        label: props.label,
        unit: props.unit,
        min: props.min,
        max: props.max,
        value: value
      };
    });
}

function view(state$) {
  return state$.map(state =>
      div('.labeled-slider', [
        label('.label', `${state.label}: ${state.value}${state.unit}`),
        input('.slider', {type: 'range', min: state.min, max: state.max, value: state.value})
      ])
    );
}

function LabeledSlider(sources) {
  const change$ = intent(sources.DOM);
  const state$ = model(change$, sources.props);
  const vtree$ = view(state$);
  const sinks = {
    DOM: vtree$
  };
  return sinks;  
}

function main(sources) {
  const props$ = Rx.Observable.of({
    label: 'Height',
    unit: 'cm',
    min: 140,
    max: 220,
    init: 170
  })
  return LabeledSlider({DOM: sources.DOM, props: props$});
}

const drivers = {
  DOM: makeDOMDriver('#app'),
};

Cycle.run(main, drivers)
```

## 17. Using the component in the main() function

Already implemented above.

## 18. Multiple independent instances of a component

```javascript
const {div, input, label, h2, makeDOMDriver} = CycleDOM;

function intent(DOMSource) {
  return DOMSource.select('.slider').events('input')
    .map(ev => ev.target.value);
}

function model(change$, props$) {
  const initialValue$ = props$.map(props => props.init).first();
  const value$ = initialValue$.concat(change$);
  return Rx.Observable.combineLatest(
    value$,
    props$,
    (value, props) => {
      return {
        label: props.label,
        unit: props.unit,
        min: props.min,
        max: props.max,
        value: value
      };
    });
}

function view(state$) {
  return state$.map(state =>
      div('.labeled-slider', [
        label('.label', `${state.label}: ${state.value}${state.unit}`),
        input('.slider', {type: 'range', min: state.min, max: state.max, value: state.value})
      ])
    );
}

function LabeledSlider(sources) {
  const change$ = intent(sources.DOM);
  const state$ = model(change$, sources.props);
  const vtree$ = view(state$);
  const sinks = {
    DOM: vtree$
  };
  return sinks;  
}

function main(sources) {
  const weightProps$ = Rx.Observable.of({
    label: 'Weight',
    unit: 'kg',
    min: 40,
    max: 150,
    init: 70
  })
  const weightSinks = LabeledSlider({
    DOM: sources.DOM.select('.weight'), props: weightProps$});
  const weightVTree$ = weightSinks.DOM.map(vtree => {
      vtree.properties.className += " weight";
      return vtree;
  });

  const heightProps$ = Rx.Observable.of({
    label: 'Height',
    unit: 'cm',
    min: 140,
    max: 220,
    init: 170
  })
  const heightSinks = LabeledSlider({
    DOM: sources.DOM.select('.height'), props: heightProps$});
  const heightVTree$ = heightSinks.DOM.map(vtree => {
      vtree.properties.className += " height";
      return vtree;
  });

  const vtree$ = Rx.Observable.combineLatest(
    weightVTree$,
    heightVTree$,
    (weightVTree, heightVTree) =>
      div([
        weightVTree,
        heightVTree
      ])
    );

  return {
    DOM: vtree$
  };
}

const drivers = {
  DOM: makeDOMDriver('#app'),
};

Cycle.run(main, drivers)
```

## 19. Isolating Component instances

```javascript
const {div, input, label, h2, makeDOMDriver} = CycleDOM;
const isolate = CycleIsolate;

function intent(DOMSource) {
  return DOMSource.select('.slider').events('input')
    .map(ev => ev.target.value);
}

function model(change$, props$) {
  const initialValue$ = props$.map(props => props.init).first();
  const value$ = initialValue$.concat(change$);
  return Rx.Observable.combineLatest(
    value$,
    props$,
    (value, props) => {
      return {
        label: props.label,
        unit: props.unit,
        min: props.min,
        max: props.max,
        value: value
      };
    });
}

function view(state$) {
  return state$.map(state =>
      div('.labeled-slider', [
        label('.label', `${state.label}: ${state.value}${state.unit}`),
        input('.slider', {type: 'range', min: state.min, max: state.max, value: state.value})
      ])
    );
}

function LabeledSlider(sources) {
  const change$ = intent(sources.DOM);
  const state$ = model(change$, sources.props);
  const vtree$ = view(state$);
  const sinks = {
    DOM: vtree$
  };
  return sinks;  
}

function main(sources) {
  const weightProps$ = Rx.Observable.of({
    label: 'Weight',
    unit: 'kg',
    min: 40,
    max: 150,
    init: 70
  })
  const WeightSlider = isolate(LabeledSlider, 'weight');  
  const weightSinks = WeightSlider({
    DOM: sources.DOM, props: weightProps$});

  const heightProps$ = Rx.Observable.of({
    label: 'Height',
    unit: 'cm',
    min: 140,
    max: 220,
    init: 170
  })
  const HeightSlider = isolate(LabeledSlider, 'height');  
  const heightSinks = HeightSlider({
    DOM: sources.DOM, props: heightProps$});

  const vtree$ = Rx.Observable.combineLatest(
    weightSinks.DOM,
    heightSinks.DOM,
    (weightVTree, heightVTree) =>
      div([
        weightVTree,
        heightVTree
      ])
    );

  return {
    DOM: vtree$
  };
}

const drivers = {
  DOM: makeDOMDriver('#app'),
};

Cycle.run(main, drivers)
```

## 20. Exporting values from components through sinks

Sinks from a component can be write effects to the DOM but they can also
be data or messages passed up to parent components in the component hierarchy.

```javascript
const {div, input, label, h2, makeDOMDriver} = CycleDOM;
const isolate = CycleIsolate;

function intent(DOMSource) {
  return DOMSource.select('.slider').events('input')
    .map(ev => ev.target.value);
}

function model(change$, props$) {
  const initialValue$ = props$.map(props => props.init).first();
  const value$ = initialValue$.concat(change$);
  return Rx.Observable.combineLatest(
    value$,
    props$,
    (value, props) => {
      return {
        label: props.label,
        unit: props.unit,
        min: props.min,
        max: props.max,
        value: value
      };
    });
}

function view(state$) {
  return state$.map(state =>
      div('.labeled-slider', [
        label('.label', `${state.label}: ${state.value}${state.unit}`),
        input('.slider', {type: 'range', min: state.min, max: state.max, value: state.value})
      ])
    );
}

function LabeledSlider(sources) {
  const change$ = intent(sources.DOM);
  const state$ = model(change$, sources.props);
  const vtree$ = view(state$);
  const sinks = {
    DOM: vtree$,
    value: state$.map(state => state.value),
  };
  return sinks;  
}

const IsolatedLabeledSlider = function(sources) {
  return isolate(LabeledSlider)(sources);
}

function main(sources) {
  const weightProps$ = Rx.Observable.of({
    label: 'Weight',
    unit: 'kg',
    min: 40,
    max: 150,
    init: 70
  })
  const weightSinks = IsolatedLabeledSlider({
    DOM: sources.DOM, props: weightProps$});
  const weightValue$ = weightSinks.value;
  const heightProps$ = Rx.Observable.of({
    label: 'Height',
    unit: 'cm',
    min: 140,
    max: 220,
    init: 170
  })
  const heightSinks = IsolatedLabeledSlider({
    DOM: sources.DOM, props: heightProps$});
  const heightValue$ = heightSinks.value;

  const bmi$ = Rx.Observable.combineLatest(
    weightValue$,
    heightValue$,
    (weight, height) => {
      const heightMeters = height * 0.01;
      const bmi = Math.round(weight / (heightMeters * heightMeters));
      return bmi;
    });

  const vtree$ = Rx.Observable.combineLatest(
    bmi$,
    weightSinks.DOM,
    heightSinks.DOM,
    (bmi, weightVTree, heightVTree) =>
      div([
        weightVTree,
        heightVTree,
        h2('BMI is ' + bmi)
      ]),
    );

  return {
    DOM: vtree$
  };
}

const drivers = {
  DOM: makeDOMDriver('#app'),
};

Cycle.run(main, drivers)
```
