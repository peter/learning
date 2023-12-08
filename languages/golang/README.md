# The Go Language

## The Pitch for Go

* A simple and easy to learn language
* Static/strong typing
* Garbage collected
* High performance
* High concurrency support built into the language
* Low memory footprint (significantly lower than Java, slightly higher than C or Rust)
* Is deployed as a single binary without any dependencies
* Fast compiles
* Good developer tooling
* Comprehensive standard library with http/networking, testing etc.
* Created and backed by Google and is very popular

## Hello World

From the [getting started page]((https://go.dev/doc/tutorial/getting-started)):

```sh
mkdir hello
cd hello
go mod init example/hello
```

```golang
// file hello.go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

```sh
go run .
```

## Resources

Learning Go:

* [Tutorial: Get started with Go](https://go.dev/doc/tutorial/getting-started)
* [Official Go Learning Portal](https://go.dev/learn/)
* [Learn Go in Y minutes](https://learnxinyminutes.com/docs/go/)
* [The Golang Handbook – A Beginner's Guide to Learning Go](https://www.freecodecamp.org/news/learn-golang-handbook/)
* [Go by Example](https://gobyexample.com/)
* [Go Standard library Documentation](https://pkg.go.dev/std)
* [Learn Go Programming - Golang Tutorial for Beginners](https://www.youtube.com/watch?v=YS4e4q9oBaU&t=537s)

Building REST APIs with Go:

* [Build a RESTful CRUD API with Golang Gin and Gorm](https://lemoncode21.medium.com/build-a-restful-crud-api-with-golang-gin-and-gorm-e1e976ef5b9f)
* [Optimizing GoLang APIs with Gin, New Relic, and Swagger](https://blog.stackademic.com/optimizing-golang-apis-with-gin-new-relic-and-swagger-a-comprehensive-guide-d60cea368fbe)

Frameworks and libraries:

* [Gin Web Framework](https://github.com/gin-gonic/gin)
* [GORM (ORM)](https://github.com/go-gorm/gorm)
