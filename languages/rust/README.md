# Rust

## TODO

* [What is Rust?](https://en.wikipedia.org/wiki/Rust_(programming_language)) - Rust is a general-purpose multi-paradigm language that emphasizes performance, type safety and concurrency. Rust enforces memory safety without the use of a garbage collector. Rust has a "borrow checker" that trackes the lifetime of references in a project during compilation. Rust is popular for systems programming but offers some high-level functional programming constructs. Rust was created by Graydon Hoare at Mozilla in 2006 and has been adopted after its stable release in 2014 by large companies such as Amazon, Discord, [Dropbox](https://dropbox.tech/infrastructure/rewriting-the-heart-of-our-sync-engine), Meta, Google, and Microsoft.
* To install - use [rustup](https://www.rust-lang.org/tools/install). Rust has a 6-week rapid release process and is installed and upgraded with `rustup` at `~/.cargo/bin`.
* To create a new project - use the [Cargo](https://doc.rust-lang.org/cargo/) command `cargo new my-project`. Cargo is Rust’s build system and package manager. [Dependencies](https://doc.rust-lang.org/cargo/guide/dependencies.html) are specified in the `Cargo.toml` [TOML](https://github.com/toml-lang/toml) file. Rust libraries are called "Crates" and can be found at [crates.io](https://crates.io/). Use `cargo build` to build your project and `cargo run` to run it. To get a `.gitignore` file for Rust you can use `curl https://raw.githubusercontent.com/github/gitignore/main/Rust.gitignore > .gitignore`
* To compile and run a single Rust file - use `rustc my-program.rs && ./my-program`
* IDE - use VS Code with the [Rust extension](https://code.visualstudio.com/docs/languages/rust)
* [Parse command line arguments with clap](https://rust-cli.github.io/book/tutorial/cli-args.html)
* You can try Rust in the Browser at [play.rust-lang.org](https://play.rust-lang.org/)
* [Modules](https://doc.rust-lang.org/stable/book/ch07-02-defining-modules-to-control-scope-and-privacy.html)
* For debug printouts you can use the [dbg! macro](https://doc.rust-lang.org/std/macro.dbg.html)
* Rust can format your code automatically
* Rust will warn about unused imports and code by default
* Traits?
* Equality
* Truth
* Loops
* Conditionals
* [Scalar Types](https://doc.rust-lang.org/book/ch03-02-data-types.html) - integers, floats, booleans
* [UTF-8 Strings](https://doc.rust-lang.org/book/ch08-02-strings.html#storing-utf-8-encoded-text-with-strings)
* [Compound Types](https://doc.rust-lang.org/book/ch03-02-data-types.html#compound-types) - tuples and arrays. Arrays are fixed size and and accessing a value out of bounds yields a panic. [Vectors are dynamic arrays](https://www.cs.brandeis.edu/~cs146a/rust/doc-02-21-2015/book/arrays-vectors-and-slices.html)
* [Structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html)
* [HashMap and Vector literals](https://stackoverflow.com/questions/27582739/how-do-i-create-a-hashmap-literal)
* [Environment variables](https://doc.rust-lang.org/book/ch12-05-working-with-environment-variables.html)
* [enum](https://doc.rust-lang.org/std/keyword.enum.html#:~:text=Enums%20in%20Rust%20are%20similar,from%20a%20functional%20programming%20background.)
* Threads - see [recovering from panic](https://stackoverflow.com/questions/30824258/recovering-from-panic-in-another-thread#:~:text=Putting%20aside%20%22you%20should%20be,isolate%20them%2C%20then%20detect%20them.)
* Error handling
* Double quotes or single quotes? Rust uses [double quotes for strings and single quotes for chars](https://stackoverflow.com/questions/68231820/difference-between-double-quotes-and-single-quotes-in-rust#:~:text=The%20short%20answer%20is%20it,and%20double%20quotes%20for%20strings.)
* [Match expressions](https://doc.rust-lang.org/reference/expressions/match-expr.html)
* Union types
* Libraries - see [Cargo](https://doc.rust-lang.org/cargo/) and [crates.io](https://crates.io/)
* What is Rust good for? "Rust works well for processing large amounts of data and other CPU-intensive operations, such as executing algorithms" - see [When to use Rust and when to use Go](https://blog.logrocket.com/when-to-use-rust-when-to-use-golang/)
* To work with JSON - see [the Serde JSON library](https://github.com/serde-rs/json) and [this Serde JSON tutorial](https://blog.logrocket.com/json-and-rust-why-serde_json-is-the-top-choice/). There are [Serde libraries](https://serde.rs/) for other serialization formats as well (such as YAML, TOML, Avro etc)
* To build a REST API - see [Tokio](https://github.com/tokio-rs/tokio), [hyper](https://github.com/hyperium/hyper) and [warp](https://github.com/seanmonstar/warp)
* Null values - use the [The Option type](https://doc.rust-lang.org/std/option/) - see [Option example](https://doc.rust-lang.org/rust-by-example/std/option.html)

* How to learn Rust - see [The Rust Programming Language (rust-lang.org)](https://doc.rust-lang.org/book/) and [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
* How to stay up to date with Rust?
* What is Rust used for? It's used by Google to build the Android OS and it's used to build Webassembly applications in browsers.
* How popular is Rust?
* How mature is Rust?

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
* [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
* [Rust Tutorial by Derek Banas](https://www.youtube.com/watch?v=ygL_xcavzQ4&t=8113s)
