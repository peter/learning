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
