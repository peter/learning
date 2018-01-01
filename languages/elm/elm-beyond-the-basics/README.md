# Course: Elm Beyond the Basics

Course notes

## Review

Quick recap of the basics of Elm.

The basic cycle is Model -> View -> Update.

```
elm package install elm-lang/Html
elm reactor
```

## The Elm Architecture

A realistic size up should be broken up into several modules and a pattern we
can use is to have one module per page. Each page module has its own
model-update-view sections. There is a Main module that also has model-update-view
sections that delegate to the corresponding page modules.

The name of the module for each page must match its filename. The modules need to expose their
model-view-update functions.

## Effects

Impure things with side effects like HTTP, websockets, local storage (anything that talks to the outside world). Most of Elm programs are built in pure functions as those are testable, composable, and cacheable etc.

In Elm we offload state to the Html.App module. Effects are handled via messages in the update function. Instead of having the update function return just the Model though we now return (Model, Cmd Msg). Commands (Cmd) are just data structures with instructions on what to do. The dirty work is handled by the framework/libraries. A command will either succeed or fail.
