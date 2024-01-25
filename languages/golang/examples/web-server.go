package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, req *http.Request) {
	// if req.URL.Path != "/" {
	// 	http.NotFound(w, req)
	// 	return
	// }
	fmt.Fprintf(w, "Hi there, I love %s!", req.URL.Path[1:])
}

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
