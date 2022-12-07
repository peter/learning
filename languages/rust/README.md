# Rust

## TODO

* Paradigm?
* Equality
* Truth
* Loops
* Conditionals
* Basic types
* Aggregate types
* Error handling
* Match expressions
* Libraries
* How to learn
* How popular
* What is it used for? It's used by Google to build the Android OS and it's used to build Webassembly applications in browsers.
* What is Rust good for? "Rust works well for processing large amounts of data and other CPU-intensive operations, such as executing algorithms" - see [When to use Rust and when to use Go](https://blog.logrocket.com/when-to-use-rust-when-to-use-golang/)
* How to stay up to date
* How mature?
* How do you work with JSON? See [the Serde JSON library](https://github.com/serde-rs/json) and [this tutorial](https://blog.logrocket.com/json-and-rust-why-serde_json-is-the-top-choice/)
* Building a rest api? See [Tokio](https://github.com/tokio-rs/tokio), [hyper](https://github.com/hyperium/hyper) and [warp](https://github.com/seanmonstar/warp)
* Null values? [The Option type](https://doc.rust-lang.org/std/option/) - see [Option example](https://doc.rust-lang.org/rust-by-example/std/option.html)
* Union types?

## Installation

```sh
ls ~/.cargo/bin 
# cargo
# cargo-clippy
# cargo-fmt
# cargo-miri
# clippy-driver
# rls
# rust-gdb
# rust-gdbgui
# rust-lldb
# rustc
# rustdoc
# rustfmt
# rustup

rustc --version
# => rustc 1.65.0 (897e37553 2022-11-02)

rustup update
```

[Error: "ld: library not found"](https://stackoverflow.com/questions/70313347/ld-library-not-found-for-lpq-when-build-rust-in-macos?rq=1)

```sh
export RUSTFLAGS='-L /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib'
```

## Resources

* [The Rust Programming Language (rust-lang.org)](https://doc.rust-lang.org/book/)