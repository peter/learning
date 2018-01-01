# Angular 4 (formerly Angular 2) - The Complete Guide (Udemy Course)

Angular is a framework for building reactive single page applications.

## Angular Versions

* Angular 1 - very popular
* Angular 2 - complete rewrite, component based
* Angular 4 - an update of Angular 2

## Angular CLI

```
npm install -g @angular/cli
ng new my-first-app
cd my-first-app
ng serve
```

## Making a First Change

Change title in app.component.ts.

Add some HTML in the app component:

```html
<input type="text" [(ngModel)]="name">
{{name}}
```

Add the name property in the app component:

```typescript
export class AppComponent {
  title = 'My First App!!'
  name = ''
}
```

And an import to the app module to be able to use ngModel:

```typescript
import { FormsModule } from '@angular/forms'
```
