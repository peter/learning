# Introduction to Reactive Programming Notes

Notes from the course [Introduction to Reactive Programming](https://egghead.io/courses/introduction-to-reactive-programming).

## 1. Reactive Programming - What is RxJS?

Reactive programming is programming with event streams, i.e. a sequence of events
happening over time, like an asynchronous array. A regular JavaScript array is
a sequence in space.

Subscribing to a simple event stream (observable):

```javascript
var source = Rx.Observable.interval(400).take(9)
  .map(i => ['1', '1', 'foo', '2', '3', '5', 'bar', '8', '13'][i])

source.subscribe(x => console.log(x));
```

Using map/filter/reduce to create a sum of values from a stream:

```javascript
var source = Rx.Observable.interval(400).take(9)
  .map(i => ['1', '1', 'foo', '2', '3', '5', 'bar', '8', '13'][i])

var sumOfInts = source
  .map(x => parseInt(x))
  .filter(x => !isNaN(x))
  .reduce((x, y) => x + y);

source.subscribe(x => console.log("Value: " + parseInt(x)))
sumOfInts.subscribe(x => console.log("Sum of numbers: " + x));
```

## 2. Reactive Programming - Using an event stream of double clicks

```html
<!DOCTYPE html>
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/rxjs/4.1.0/rx.all.js"></script>
  <meta charset="utf-8">
  <title>JS Bin</title>
</head>
<body>
<div class="header">
         <a href="#" class="button">BUTTON</a><h4>-</h4>
    </div>
</body>
</html>
```

```javascript
var button = document.querySelector('.button');
var label = document.querySelector('h4');

var clickStream = Rx.Observable.fromEvent(button, 'click');

var doubleClickStream = clickStream
  .buffer(() => clickStream.debounce(250))
  .map(arr => arr.length)
  .filter(len => len === 2);

doubleClickStream.subscribe(event => {
  label.textContent = 'double click';
});

doubleClickStream
  .delay(1000)
  .subscribe(suggestion => {
    label.textContent = '-';
  });
```

## 3. Reactive Programming - Why choose RxJS?

You can specify the dynamic behavior of a value completely at the time
of declaration.

```javascript
var a = 3;
var b = 10 * a;

console.log(b);

a = 4;
// b = 11 * a;
console.log(b);
```

```javascript
var streamA = Rx.Observable.of(3, 4);
var streamB = streamA.map(a => 10 * a);

streamB.subscribe(b => console.log(b));
```

## 4. Async Requests and Responses

A promise is like an event stream with one value, success or error.

```html
<!DOCTYPE html>
<html>
<head>
<script src="https://code.jquery.com/jquery-1.7.2.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/rxjs/4.1.0/rx.all.js"></script>
  <meta charset="utf-8">
  <title>JS Bin</title>
</head>
<body>
<div class="container">
    <div class="header">
         <h3>Who to follow</h3><a href="#" class="refresh">Refresh</a>
    </div>
    <ul class="suggestions">
        <li class="suggestion1">
            <img />
            <a href="#" target="_blank" class="username">this will not be displayed</a>
            <a href="#" class="close close1">x</a>
        </li>
        <li class="suggestion2">
            <img />
            <a href="#" target="_blank" class="username">neither this</a>
            <a href="#" class="close close2">x</a>
        </li>
        <li class="suggestion3">
            <img />
            <a href="#" target="_blank" class="username">nor this</a>
            <a href="#" class="close close3">x</a>
        </li>
    </ul>
</div>
</body>
</html>
```

...

## Resources

* [Course: Introduction to Reactive Programming](https://egghead.io/courses/introduction-to-reactive-programming)
* [Article: The introduction to Reactive Programming you've been missing](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754)
