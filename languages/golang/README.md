# The Go Language

## What is Go?

[Wikipedia](https://en.wikipedia.org/wiki/Go_(programming_language)):

Go is a statically typed, compiled high-level programming language designed at Google[12] by Robert Griesemer, Rob Pike, and Ken Thompson.[4] It is syntactically similar to C, but also has memory safety, garbage collection, structural typing,[7] and CSP-style concurrency.[13] It is often referred to as Golang because of its former domain name, golang.org, but its proper name is Go.

There are two major implementations:

Google's self-hosting[15] "gc" compiler toolchain, targeting multiple operating systems and WebAssembly.[16]
gofrontend, a frontend to other compilers, with the libgo library. With GCC the combination is gccgo;[17] with LLVM the combination is gollvm.[18][a]
A third-party source-to-source compiler, GopherJS,[20] compiles Go to JavaScript for front-end web development.

Go was designed at Google in 2007 to improve programming productivity in an era of multicore, networked machines and large codebases.[21] The designers wanted to address criticisms of other languages in use at Google, but keep their useful characteristics:[22]

Static typing and run-time efficiency (like C)
Readability and usability (like Python)[23]
High-performance networking and multiprocessing
Its designers were primarily motivated by their shared dislike of C++.[24][25][26]

Go was publicly announced in November 2009,[27] and version 1.0 was released in March 2012.[28][29] Go is widely used in production at Google[30] and in many other organizations and open-source projects.

The Gopher mascot was introduced in 2009 for the open source launch of the language. The design, by Renée French, borrowed from a c. 2000 WFMU promotion

Go does not follow SemVer; rather, each major Go release is supported until there are two newer major releases. Unlike most software, Go calls the second number in a version the major, i.e., in 1.x x is the major version. [46] This is because Go plans to never reach 2.0, given that compatibility is one of language's major selling points.

## Install Go and Get Started

https://go.dev/doc/install

Open the package file you downloaded and follow the prompts to install Go.
The package installs the Go distribution to /usr/local/go. The package should put the /usr/local/go/bin directory in your PATH environment variable. You may need to restart any open Terminal sessions for the change to take effect.

Verify that you've installed Go by opening a command prompt and typing the following command:

```sh
go version
# => go version go1.23.1 darwin/arm64
```

https://go.dev/doc/tutorial/getting-started

```sh
mkdir go-test
cd go-test
go mod init peter/go-test
cat go.mod
# module peter/go-test

# go 1.23.1
```

```go
// hello.go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

```sh
go run .

go help
```

## The Pitch for Go

* A simple and easy to learn language
* Has interfaces, structs and first class functions but no class hierarchies
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

## Learning Path

[Best Resources to Learn Golang (Video by Melkey)](https://www.youtube.com/watch?v=qT14b1pxtiI):

* [A Tour of Go](https://go.dev/tour)
* [Go by Example](https://gobyexample.com)
* [Effective Go](https://go.dev/doc/effective_go)
* [Let's Go Book](https://lets-go.alexedwards.net)
* [Let's Go Further Book](https://lets-go-further.alexedwards.net)

* [Wiki tutorial](https://go.dev/doc/articles/wiki)
* [Generics tutorial](https://go.dev/doc/tutorial/generics)

* [Go Course on FreeCodeCamp/boot.dev](https://youtu.be/un6ZyFkqFKo?si=xUiY4_MwbDZ_SUXN) (with [source code on Github](git@github.com:bootdotdev/fcc-learn-golang-assets.git))

TODO:

* How structs can be extended, see https://github.com/nofeaturesonlybugs/sqlh
* [sqlx CRUD](https://github.com/jmoiron/sqlx)
* CRUD API with Fiber

* [SQLC, Go-Migrate, pgx tutorial](https://medium.com/gravel-engineering/using-sqlc-for-orm-alternative-in-golang-ft-go-migrate-pgx-b9e35ec623b2)
* [pgx CRUD](https://www.toolify.ai/ai-news/mastering-golang-crud-with-pgx-182374)

Tutorials:

* How to Build a CLI App in Go - Tutorial: [Video](https://www.youtube.com/watch?v=g16Zf0KQEWI) / [Code](https://github.com/patni1992/CLI-Todo-App-In-Go) / [Blog Post](https://codingwithpatrik.dev/posts/how-to-build-a-cli-todo-app-in-go/)
* [How to Code Hangman in Go](https://codingwithpatrik.dev/posts/go-golang-hangman)

## Creating a Hello World Project (Go Module)

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

## nil

The value `nil` is the zero-value for pointers, interfaces, and some other types.

## Parsing Arbitrary JSON Data

```go
jsonData := []byte(`{
        "name": "Bob",
        "age": 25,
        "email": "bob@example.com"
}`)

// Declare a map to hold the JSON data
var data map[string]interface{}

// Parse (unmarshal) the JSON into the map
err := json.Unmarshal(jsonData, &data)
if err != nil {
	log.Fatal(err)
}

// Access the parsed data
fmt.Println("Name:", data["name"])
fmt.Println("Age:", data["age"])
fmt.Println("Email:", data["email"])
```

## Error Handling

[Errors](https://go.dev/ref/spec#Errors) returned from functions can be ignored:

```go
func loadPage(title string) *Page {
	filename := title + ".txt"
	body, _ := os.ReadFile(filename)
	return &Page{Title: title, Body: body}
}
```

They can also be propagated:

```go
func loadPage(title string) (*Page, error) {
    filename := title + ".txt"
    body, err := os.ReadFile(filename)
    if err != nil {
        return nil, err
    }
    return &Page{Title: title, Body: body}, nil
}

// Creating an error with errors.New
if hs.Cfg.CertFile == "" {
    return nil, errors.New("cert_file cannot be empty when using HTTPS")
}
```

Wrapping errors:

```go
// NOTE: we wrap the error here to provide context as by default Go errors have no stacktrace
// Alternative error wrapping: https://github.com/pkg/errors
// Go2 error proposal: https://go.googlesource.com/proposal/+/master/design/go2draft.md
// See also: https://tpaschalis.me/golang-multierr/
return nil, fmt.Errorf("StorylinesGet - http.NewRequest returned error: %w", error)

// Similar example:
if err != nil {
    return nil, fmt.Errorf("failed to read certificate file: %w", err)
}
```

Checking error type:

* `errors.Is` checks if a specific error is part of the error tree
* `errors.As` checks if the error tree contains an error that can be assigned to a target type

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
* [Tutorial: Build a Wiki (go.dev)](https://go.dev/doc/articles/wiki/)
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

## OpenAPI Documentation

[Any good OpenAPI 3.x spec generator for a Go REST API?](https://www.reddit.com/r/golang/comments/udfujj/any_good_openapi_3x_spec_generator_for_a_go_rest)

From the [Grafana API README](https://github.com/grafana/grafana/tree/main/pkg/api):

"The OpenAPI v2 specification is generated automatically from the annotated Go code using [go-swagger](https://github.com/go-swagger/go-swagger) which scans the source code for [annotation rules](https://goswagger.io/use/spec.html). Refer to [this getting started guide](https://medium.com/@pedram.esmaeeli/generate-swagger-specification-from-go-source-code-648615f7b9d9) for getting familiar with the toolkit."
