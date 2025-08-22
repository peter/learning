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

* [Official Go Documentation](https://go.dev/doc/#learning)

* [A Tour of Go](https://go.dev/tour/list)
* [How to Write Go Code](https://go.dev/doc/code)
* [Effective Go](https://go.dev/doc/effective_go)

[Best Resources to Learn Golang (Video by Melkey)](https://www.youtube.com/watch?v=qT14b1pxtiI):

* [Go by Example](https://gobyexample.com)
* [Effective Go](https://go.dev/doc/effective_go)
* [Let's Go Book](https://lets-go.alexedwards.net)
* [Let's Go Further Book](https://lets-go-further.alexedwards.net)

* [Wiki tutorial](https://go.dev/doc/articles/wiki)
* [Generics tutorial](https://go.dev/doc/tutorial/generics)

* [Go Course on FreeCodeCamp/boot.dev](https://youtu.be/un6ZyFkqFKo?si=xUiY4_MwbDZ_SUXN) (with [source code on Github](git@github.com:bootdotdev/fcc-learn-golang-assets.git))
* [Golang Web Server and RSS Scraper | Full Tutorial / boot.dev](https://www.youtube.com/watch?v=dpXhDzgUSe4&t=3364s)
* [Learn HTTP Servers in Go / boot.dev](https://www.boot.dev/courses/learn-http-servers-golang)
* [DIY Golang Web Server: No Dependencies Needed - with thread safe mutex cache](https://www.youtube.com/watch?v=eqvDSkuBihs)
* [Go from Zero to Hero: Learn Golang in 15 minutes](https://www.youtube.com/watch?v=P7dCWOjRwJA&t=0s)

* [Awesome Go](https://awesome-go.com)
* [Awesome Go with Popularity](https://github.com/amanbolat/awesome-go-with-stars?tab=readme-ov-file)

* [Building a NoSQL database in Go](https://betterprogramming.pub/build-a-nosql-database-from-the-scratch-in-1000-lines-of-code-8ed1c15ed924)

TODO:

* How structs can be extended, see https://github.com/nofeaturesonlybugs/sqlh
* [sqlx CRUD](https://github.com/jmoiron/sqlx)
* CRUD API with Fiber

* [SQLC, Go-Migrate, pgx tutorial](https://medium.com/gravel-engineering/using-sqlc-for-orm-alternative-in-golang-ft-go-migrate-pgx-b9e35ec623b2)
* [pgx CRUD](https://www.toolify.ai/ai-news/mastering-golang-crud-with-pgx-182374)

Tutorials:

* How to Build a CLI App in Go - Tutorial: [Video](https://www.youtube.com/watch?v=g16Zf0KQEWI) / [Code](https://github.com/patni1992/CLI-Todo-App-In-Go) / [Blog Post](https://codingwithpatrik.dev/posts/how-to-build-a-cli-todo-app-in-go/)
* [How to Code Hangman in Go](https://codingwithpatrik.dev/posts/go-golang-hangman)

## Making Parallel HTTP Requests

https://medium.com/insiderengineering/concurrent-http-requests-in-golang-best-practices-and-techniques-f667e5a19dea

Here is the equivalent of a JavaScript Promise.allSettled implementation in Go:

```go
package main

import (
	"errors"
	"fmt"
	"sync"
	"time"
)

// Result holds the outcome of each task
type Result struct {
	Value interface{}
	Error error
}

// Task is a function type that returns a result and an error
type Task func() (interface{}, error)

// allSettled runs tasks concurrently and collects all results, regardless of success or failure.
func allSettled(tasks []Task) []Result {
	var wg sync.WaitGroup
	results := make([]Result, len(tasks))

	// Execute each task in a goroutine
	for i, task := range tasks {
		wg.Add(1)

		go func(i int, task Task) {
			defer wg.Done()
			value, err := task()
			results[i] = Result{Value: value, Error: err}
		}(i, task)
	}

	// Wait for all tasks to complete
	wg.Wait()
	return results
}

func main() {
	tasks := []Task{
		func() (interface{}, error) {
			time.Sleep(1 * time.Second)
			return "Task 1 result", nil
		},
		func() (interface{}, error) {
			time.Sleep(2 * time.Second)
			return nil, errors.New("Task 2 failed")
		},
		func() (interface{}, error) {
			time.Sleep(1 * time.Second)
			return "Task 3 result", nil
		},
	}

	// Run all tasks concurrently and gather results
	results := allSettled(tasks)

	// Print results
	for i, result := range results {
		if result.Error != nil {
			fmt.Printf("Task %d failed with error: %v\n", i+1, result.Error)
		} else {
			fmt.Printf("Task %d succeeded with result: %v\n", i+1, result.Value)
		}
	}
}
```

## HTTP Requests with Retries

https://kdthedeveloper.medium.com/golang-http-retries-fbf7abacbe27

https://brandur.org/fragments/go-http-retry

https://github.com/avast/retry-go

```go
err := retry.Do(
	func() error {
		resp, err := http.Get(url)
		if err != nil {
			return err
		}
		defer resp.Body.Close()
		body, err = ioutil.ReadAll(resp.Body)
		if err != nil {
			return err
		}
		return nil
	},
)

const RetryCount = 3

func backoff(retries int) time.Duration {
	return time.Duration(math.Pow(2, float64(retries))) * time.Second
}

func shouldRetry(err error, resp *http.Response) bool {
	if err != nil {
		return true
	}

	if resp.StatusCode == http.StatusBadGateway ||
		resp.StatusCode == http.StatusServiceUnavailable ||
		resp.StatusCode == http.StatusGatewayTimeout {
		return true
	}

	return false
}
```

## Routing with Go Standard Library

* [Release Notes](https://go.dev/blog/routing-enhancements)
* [http ServeMux API Docs](https://pkg.go.dev/net/http#ServeMux)

```go
http.HandleFunc("GET /posts/{id}", handlePost2)
idString := req.PathValue("id")
```

## Libraries for Postgres

* [pgx - PostgreSQL Driver and Toolkit](https://github.com/jackc/pgx)
* [Goose - a database migration tool](https://github.com/pressly/goose)
* [sqlc - generates type-safe code from SQL](https://github.com/sqlc-dev/sqlc)

The pgx driver is a low-level, high performance interface that exposes PostgreSQL-specific features such as LISTEN / NOTIFY and COPY. It also includes an adapter for the standard database/sql interface.

## JSON Logging

https://www.highlight.io/blog/5-best-logging-libraries-for-go

* https://github.com/uber-go/zap and https://github.com/maoueh/zap-pretty
* https://github.com/rs/zerolog
* https://github.com/Sirupsen/logrus

You can also do JSON logging with the Go standard library (probably less performant):

```go
import (
	"encoding/json"
	"fmt"
	"log"
	"os"
)

type LogLevel string

const (
	InfoLevel  LogLevel = "info"
	ErrorLevel LogLevel = "error"
)

func StructuredLog(level LogLevel, message string, data map[string]interface{}) {
	// Add common log fields
	data["level"] = level
	data["message"] = message

	// Serialize to JSON
	entryJSON, err := json.Marshal(data)
	if err != nil {
		log.Printf("Error marshalling JSON: %v", err)
		return
	}

	// Output the log entry
	log.Println(string(entryJSON))
}

StructuredLog(InfoLevel, "User login", map[string]interface{}{
		"userID": 12345,
		"source": "main.go",
})
```


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

## What is a Go Package?

From [How to Write Go Code](https://go.dev/doc/code):

Go programs are organized into packages. A package is a collection of source files in the same directory that are compiled together. Functions, types, variables, and constants defined in one source file are visible to all other source files within the same package.

## What is a Go Module?

From [How to Write Go Code](https://go.dev/doc/code):

A repository contains one or more modules. A module is a collection of related Go packages that are released together. A Go repository typically contains only one module, located at the root of the repository. A file named go.mod there declares the module path: the import path prefix for all packages within the module. The module contains the packages in the directory containing its go.mod file as well as subdirectories of that directory, up to the next subdirectory containing another go.mod file (if any).

## Import Paths

From [How to Write Go Code](https://go.dev/doc/code):

An import path is a string used to import a package. A package's import path is its module path joined with its subdirectory within the module. For example, the module github.com/google/go-cmp contains a package in the directory cmp/. That package's import path is github.com/google/go-cmp/cmp. Packages in the standard library do not have a module path prefix.

## Slices

[Go By Example - Slices](https://gobyexample.com/slices):

Unlike arrays, slices are typed only by the elements they contain (not the number of elements). An uninitialized slice equals to nil and has length 0.

```go
// Using a Slice Literal
s := []int{1, 2, 3, 4, 5}

// Using make
s := make([]int, 5)  // Creates a slice of length 5, capacity 5, with all elements initialized to 0.
s := make([]int, 3, 5)  // Creates a slice of length 3 and capacity 5.

// Slicing an Array or Another Slice
arr := [5]int{1, 2, 3, 4, 5}
s := arr[1:4]  // Creates a slice from elements 2, 3, 4 of the array.
```

Slices are dynamic: They can grow or shrink as needed.
Slices do not store data directly: They are references to arrays.

## Go Workspaces

n earlier versions of Go (before Go Modules were introduced), a Go workspace had a specific structure. It usually consisted of three main directories: src (go source code), pkg (compiled package objects), bin (compiled binaries).

Go Modules (Introduced in Go 1.11+):
Starting from Go 1.11, Go introduced Go Modules, which modernized dependency management and reduced the need for a strict workspace structure. With Go Modules:

You no longer need to keep your Go code inside the GOPATH directory.
A module is a collection of related Go packages, and it's defined by a go.mod file, which tracks the module's dependencies.

## Strings and Single Quotes vs Double Quotes vs Backticks

* Double quotes (") for strings
* Backticks (`) for raw string literals
* Single quotes (') for runes (characters)

```go
name := "Go programming"

query := `SELECT * FROM "users" WHERE "name" = 'John'`

letter := 'A'  // Rune for the letter A
```

# Naming Convention for Go Files

https://stackoverflow.com/questions/25161774/what-are-conventions-for-filenames-in-go

* File names that begin with "." or "_" are ignored by the go tool
* Files with the suffix _test.go are only compiled and run by the go test tool.
* Files with os and architecture specific suffixes automatically follow those same constraints, e.g. name_linux.go will only build on linux, name_amd64.go will only build on amd64. This is the same as having a //+build amd64 line at the top of the file

In addition to the answer provided by JimB, regular file names are lower case, short, and without any sort of underscore or space. Generally, file names follow the same convention as package names. See the Package Names section of Effective Go.

## Having Several Go Scripts in the Same Folder with package main and main function

Yields warning "main redeclared in this block".

https://github.com/golangci/golangci-lint/issues/1370

https://stackoverflow.com/questions/66970531/vs-code-go-main-redeclared-in-this-block/66970599

Separating them into their own directories is the only solution.

In Go, a directory is a package, and a package can only have one function with a given name (with the exception of init(), which is a special case). You think of all your .go files in a directory as separate, but Go does not; it sees a single package, and that package declares multiple functions called main, which is not permitted.

## What is a valid package name in go?

* Lowercase letters
* Short, meaningful, and simple
* Avoid special characters
* Avoid collisions with Go standard library
* Singular
* Package name same as directory name
* Package names cannot contain dashes or underscores
* If you need to separate words in a package name, the common convention is to use camelCase or concatenated lowercase words without any separators

## Can I import a Single Function from a Go Module? Using Import Aliases

In Go, you cannot import a single function directly from a module; instead, you must import the entire package, as Go imports are done at the package level, not at the function or individual symbol level.

If a package has a long or confusing name, you can create an alias:

```go
import (
    t "time" // Alias "time" as "t"
)
```

## Thread Safe Cache with Mutex

* [DIY Golang Web Server: No Dependencies Needed - with thread safe mutex cache](https://www.youtube.com/watch?v=eqvDSkuBihs)
* [Go from Zero to Hero: Learn Golang in 15 minutes](https://www.youtube.com/watch?v=P7dCWOjRwJA&t=0s)

## What is a "Shebang" you can use to Invoke Go Scripts Directly?

Put the script in a file like `bin/my-amazing-script/main.go` and use a shebang so you can invoke the script directly (or simply use `go run bin/my-amazing-script/main.go` to invoke it):

```go
//usr/bin/env go run "$0" "$@" ; exit
package main
import "fmt"
func main() {
	fmt.Println("script starting...")
}
```

## HTTP Clients

https://www.reddit.com/r/golang/comments/z23tct/those_who_use_an_http_client_on_top_ofinstead_of/

https://github.com/go-resty/resty

Built in http client has no timeout by default?

https://medium.com/@nate510/don-t-use-go-s-default-http-client-4804cb19f779

## Postgres and Database Drivers / Query Builders

pgx
https://github.com/jackc/pgx

SQLC
https://github.com/sqlc-dev/sqlc

Bun
https://github.com/uptrace/bun?tab=readme-ov-file

https://github.com/lib/pq
go get github.com/lib/pq

## Example Open Source Golang Projects

Open Telementry

Uptrace Monitoring
https://github.com/uptrace/uptrace

## How do Initialize a new Go Module

```sh
# mkdir module-dir
# cd module-dir
# create main.go file
go mod init github.com/seenthis-ab/storylines-2.0/bin/migrate-user-roles
```

Clean up unused dependencies:

```sh
go mod tidy
```

## Testing

From [How to Write Go Code](https://go.dev/doc/code):

Go has a lightweight test framework composed of the go test command and the testing package.

You write a test by creating a file with a name ending in _test.go that contains functions named TestXXX with signature func (t *testing.T). The test framework runs each such function; if the function calls a failure function such as t.Error or t.Fail, the test is considered to have failed.

```go
package morestrings

import "testing"

func TestReverseRunes(t *testing.T) {
    cases := []struct {
        in, want string
    }{
        {"Hello, world", "dlrow ,olleH"},
        {"Hello, 世界", "界世 ,olleH"},
        {"", ""},
    }
    for _, c := range cases {
        got := ReverseRunes(c.in)
        if got != c.want {
            t.Errorf("ReverseRunes(%q) == %q, want %q", c.in, got, c.want)
        }
    }
}
```

## Hot Reload

You can use the [Air library](https://github.com/air-verse/air) for hot reload or [fswatch](https://medium.com/@litanin/golang-hot-reload-makefile-that-works-50abf7668949):

```sh
go install github.com/air-verse/air@latest
air init
air
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

proposal: Go 2: Error handling that is compact and composeable · Issue #55026 · golang/go · GitHub
https://github.com/golang/go/issues/55026

Best Practices for Error Handling in Go - JetBrains Guide
https://www.jetbrains.com/guide/go/tutorials/handle_errors_in_go/best_practices/

Error handling in Go web apps shouldn't be so awkward - Boldly Go
https://boldlygo.tech/posts/2024-01-08-error-handling/

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

## How do I do a "select for update skip locked" query in a transaction with pgx in Go?

```go
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/jackc/pgx/v4/pgxpool"
)

func main() {
	// Initialize a connection pool
	connString := "postgres://username:password@localhost:5432/database"
	dbpool, err := pgxpool.Connect(context.Background(), connString)
	if err != nil {
		log.Fatalf("Unable to connect to database: %v\n", err)
	}
	defer dbpool.Close()

	// Start a transaction
	ctx := context.Background()
	tx, err := dbpool.Begin(ctx)
	if err != nil {
		log.Fatalf("Failed to begin transaction: %v\n", err)
	}
	defer func() {
		if err != nil {
			tx.Rollback(ctx)
		} else {
			tx.Commit(ctx)
		}
	}()

	// Execute the SELECT FOR UPDATE SKIP LOCKED query
	rows, err := tx.Query(ctx, `
SELECT id, task_data
FROM tasks
WHERE status = 'pending'
ORDER BY created_at
LIMIT 5
FOR UPDATE SKIP LOCKED
`)
	if err != nil {
		log.Fatalf("Query failed: %v\n", err)
	}
	defer rows.Close()

	// Process the selected rows
	for rows.Next() {
		var id int
		var taskData string
		err = rows.Scan(&id, &taskData)
		if err != nil {
			log.Fatalf("Failed to scan row: %v\n", err)
		}

		// Here, you can process the task as needed
		fmt.Printf("Processing task ID %d with data: %s\n", id, taskData)
	}

	// Check for any errors during iteration
	if err = rows.Err(); err != nil {
		log.Fatalf("Row iteration error: %v\n", err)
	}

	fmt.Println("Completed processing tasks.")
}
```

## Can I combine a service that is a scheduler that runs a job Every minute with a pool of workers that works off a queue using postgres?

Yes, you can design a system that combines a scheduler with a worker pool using PostgreSQL as a queue, and this is a common pattern for handling scheduled tasks and worker pools efficiently. Here’s a high-level overview of how you can implement this:

1. Scheduler
	•	Use a scheduler (like cron, Celery Beat, or custom logic in Python, Go, etc.) to enqueue a task every minute. This scheduler would insert tasks into a PostgreSQL table.

	•	Each job entry in PostgreSQL would represent a task in the queue. You can include columns like id, task_name, status (e.g., pending, in_progress, completed), and scheduled_at.

2. PostgreSQL as a Task Queue
	•	Use a PostgreSQL table as a queue by inserting tasks that the worker pool will later pick up.

	•	Index the task table on the status column to quickly query for pending tasks.

	•	Optionally, implement locking or row-based selection to handle multiple workers. PostgreSQL’s FOR UPDATE SKIP LOCKED is useful for this, as it allows a worker to take one job without interfering with others.

3. Worker Pool
	•	Create a pool of workers that continuously poll the task queue in PostgreSQL for new jobs.

	•	Each worker can select a pending task, set its status to in_progress, and process it.

	•	Once the worker completes the task, it updates the task’s status to completed (or failed, if an error occurs).

4. Considerations
	•	Concurrency: To avoid race conditions, ensure that workers only select jobs that aren’t already being processed by another worker. FOR UPDATE SKIP LOCKED helps here.

	•	Retries: You can design retry logic by checking the task status. For example, a worker can retry tasks marked as failed.

	•	Clean-up: Depending on the volume, periodically clean up the queue by archiving or removing completed jobs.

Sample Table Schema

```sql
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    job_type TEXT NOT NULL,
	job_data jsonb,
    status TEXT CHECK (status IN ('pending', 'in_progress', 'completed', 'failed')) DEFAULT 'pending',
    scheduled_at TIMESTAMPTZ DEFAULT NOW(),
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    error jsonb
);
```

This approach allows your scheduler to enqueue tasks regularly, and workers to pick them up and process them efficiently.
