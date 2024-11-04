//usr/bin/env go run "$0" "$@" ; exit

// USAGE:
//
// ./cli.go --help
// APP_ENV=staging ./cli.go --name=Peter --age 25

package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	// Command-line arguments
	args := os.Args
	fmt.Println("Program name:", args[0])
	fmt.Println("Hello, World!")
	if len(args) > 1 {
		fmt.Println("Command-line arguments:", args[1:])
	} else {
		fmt.Println("No command-line arguments passed")
	}

	// Command-line flags
	name := flag.String("name", "World", "A name to say hello to")
	age := flag.Int("age", 0, "Age of the person")
	flag.Parse()
	fmt.Printf("Hello, %s! You are %d years old.\n", *name, *age)

	// Environment variables
	appEnv := os.Getenv("APP_ENV")
	if appEnv == "" {
		appEnv = "staging"
	}
	fmt.Printf("APP_ENV=%s\n", appEnv)
}
