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

## Debug Printouts

```golang
func printJson(prefix string, obj any) {
	jsonBytes, err := json.MarshalIndent(obj, "", "  ")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(prefix, string(jsonBytes))
}

func printStruct(prefix string, obj any) {
	fmt.Printf("%s %+v\n", prefix, obj)
}
```

## The go CLI

Running your code:

```sh
go run .
```

Installing dependencies:

```sh
go get .
go get github.com/gin-gonic/gin
go get gorm.io/gorm
go get gorm.io/driver/postgres
```

Clean up (remove) unused depenencies from `go.mod`:

```sh
go mod tidy
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
* [Golang Best Practices (Top 20)](https://medium.com/@golangda/golang-quick-reference-top-20-best-coding-practices-c0cea6a43f20)
* [20 Advanced Golang Interview Questions asked for a Senior Developer position](https://dsysd-dev.medium.com/20-advanced-questions-asked-for-a-senior-developer-position-interview-1a65203e5d5e)

Building REST APIs with Go:

* [Build a REST API in Go using Fiber + GORM](https://www.youtube.com/watch?v=dpx6hpr-wE8&t=1773s)
* [Create CRUD API in Golang using Fiber and GORM](https://github.com/wpcodevo/golang-fiber)
* [Build a RESTful CRUD API with Golang (Gorm/Gin/Postgres article + github code)](https://github.com/wpcodevo/golang-gorm-postgres)
* [Tutorial: Developing a RESTful API with Go and Gin (go.dev)](https://go.dev/doc/tutorial/web-service-gin)
* [Go REST Guide. Gin Framework (JetBrains)](https://www.jetbrains.com/guide/go/tutorials/rest_api_series/gin/)
* [Build a RESTful CRUD API with Golang Gin and Gorm](https://lemoncode21.medium.com/build-a-restful-crud-api-with-golang-gin-and-gorm-e1e976ef5b9f)
* [Optimizing GoLang APIs with Gin, New Relic, and Swagger](https://blog.stackademic.com/optimizing-golang-apis-with-gin-new-relic-and-swagger-a-comprehensive-guide-d60cea368fbe)
* [Performing CRUD Operations in PostgreSQL with Go (without an ORM)](https://edwinsiby.medium.com/performing-crud-operations-in-postgresql-with-go-42657761125c)
* [Go - SQL Databases in Golang with the database/sql package](https://www.youtube.com/watch?v=Y7a0sNKdoQk)

Deployment:

* [Getting Started on Heroku with Go](https://devcenter.heroku.com/articles/getting-started-with-go?singlepage=true#use-a-database)
* [Heroku Getting Started Example App on Github](https://github.com/heroku/go-getting-started)

Go Structs:

* [Struct Embedding (Inheritance)](https://gobyexample.com/struct-embedding)

JSON:

* [JSON tags in structs and omitempty](https://drstearns.github.io/tutorials/gojson/)

Frameworks and libraries:

* [Gin Web Framework](https://github.com/gin-gonic/gin)
* [GORM (ORM)](https://github.com/go-gorm/gorm)
* [Viper - Configuration Library](https://github.com/spf13/viper)
