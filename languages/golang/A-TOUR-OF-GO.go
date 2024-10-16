package main

// One folder in a go src directory typically corresponds to a single package
// Within a package files can access unexported functions, variables, and types

// myproject/
//   └── utils/
//       ├── math.go  (contains `package utils`)
//       └── string.go  (contains `package utils`)
//   └── main.go  (contains `package main`)
//
// In main.go:
// import "./utils"

// In Go, functions (as well as variables, types, and constants) are exported from a package
// when they are capitalized. Go follows a simple convention where any identifier
// (function, variable, or type) whose name starts with an uppercase letter is exported
// and accessible from outside the package, while those that start with a lowercase letter
// are unexported and only accessible within the package itself.

import (
	"fmt"
	"math"
	"math/rand"
	"reflect"
	"runtime"
	"time"
)

func add(a int, b int) int {
	return a + b
}

func checkType(i interface{}) {
	switch v := i.(type) {
	case int:
		fmt.Printf("i is of type int with value: %d\n", v)
	case string:
		fmt.Printf("i is of type string with value: %s\n", v)
	case float64:
		fmt.Printf("i is of type float64 with value: %f\n", v)
	default:
		fmt.Printf("i is of an unknown type: %T\n", v)
	}
}

func Sqrt(x float64) float64 {
	z := 1.0
	for i := 0; i < 10; i++ {
		z -= (z*z - x) / (2 * z)
		error := math.Abs((z*z - x) / x)
		fmt.Printf("Sqrt i=%d z=%f error=%f\n", i, z, error)
	}
	return z
}

func printSlice(name string, slice []int) {
	fmt.Printf("slice=%s len=%d cap=%d %v\n", name, len(slice), cap(slice), slice)
}

// A package named main must include a function called main() where the program execution begins.
func main() {
	fmt.Println("Hello, World!")
	fmt.Println("The time is", time.Now())
	fmt.Println("My favorite number is", rand.Intn(10))
	// See Printf format string here: https://pkg.go.dev/fmt
	fmt.Printf("You have %g problems\n", math.Sqrt(7))
	fmt.Printf("19 + 17 = %d\n", add(19, 17))

	// Variables
	// A var statement can be at package or function level
	var i int
	var c, python, java bool
	fmt.Println(i, c, python, java)

	// If an initializer is present, the type can be omitted; the variable will take the type of the initializer.
	var x = 5
	fmt.Println(x)

	// Short variable declarations
	// Inside a function, the := short assignment statement can be used in place of a var declaration with implicit type.
	k := true
	fmt.Println(k)

	// Go basic types:
	// bool
	// string
	// int  int8  int16  int32  int64
	// uint uint8 uint16 uint32 uint64 uintptr
	// byte // alias for uint8
	// rune // alias for int32
	// 	 // represents a Unicode code point
	// float32 float64

	// Variables declared without an explicit initial value are given their zero value.
	// The zero value is:
	// 0 for numeric types,
	// false for the boolean type, and
	// "" (the empty string) for strings.

	// Type conversions
	// The expression T(v) converts the value v to the type T.
	kFloat := float64(x)
	fmt.Println(kFloat)

	// Checking the type of a variable
	fmt.Printf("The type of 5 is %T\n", 5)
	fmt.Println("The type of 5 is", reflect.TypeOf(5))
	var a interface{} = "Hello, Go!"
	str, ok := a.(string)
	if ok {
		fmt.Printf("a is of type string with value: %s\n", str)
	} else {
		fmt.Println("a is not of type string")
	}

	// In Go, interface{} is a special type that represents the empty interface.
	// It can hold values of any type because all types in Go implicitly implement
	// the empty interface. This makes interface{} a way to store or pass around
	// data of any type without knowing the exact type at compile time.

	// Constants
	// Constants are declared like variables, but with the const keyword.
	// Constants can be character, string, boolean, or numeric values.
	// Constants cannot be declared using the := syntax.
	const Pi = 3.14
	fmt.Println("Happy", Pi, "Day")
	const (
		// Create a huge number by shifting a 1 bit left 100 places.
		// In other words, the binary number that is 1 followed by 100 zeroes.
		Big = 1 << 100
		// Shift it right again 99 places, so we end up with 1<<1, or 2.
		Small = Big >> 99
	)

	// For
	// Go has only one looping construct, the for loop.
	// The basic for loop has three components separated by semicolons:
	// the init statement: executed before the first iteration
	// the condition expression: evaluated before every iteration
	// the post statement: executed at the end of every iteration
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println("sum", sum)
	// The init and post statements are optional.
	for sum < 1000 {
		sum += sum
	}

	// For is Go's "while"
	for sum < 1000 {
		sum += sum
	}

	// Forever
	// for {
	// }

	// If with a short statement
	// if v := math.Pow(x, n); v < lim {
	// 	return v
	// }

	fmt.Println(Sqrt(10))

	// Switch
	// A switch statement is a shorter way to write a sequence of if - else statements.
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}

	// Time
	fmt.Println("Current time", time.Now())

	// Defer
	// A defer statement defers the execution of a function until the surrounding function returns.
	// Deferred function calls are pushed onto a stack. When a function returns, its deferred calls are executed in last-in-first-out order.
	for i := 0; i < 3; i++ {
		defer fmt.Println("deferred", i)
	}

	// Pointers
	// Go has pointers. A pointer holds the memory address of a value.
	// The type *T is a pointer to a T value. Its zero value is nil.
	// The & operator generates a pointer to its operand.
	// The * operator denotes the pointer's underlying value.
	// Unlike C, Go has no pointer arithmetic.
	value := 42
	pointer := &value
	fmt.Println("pointer value is *pointer", *pointer)
	*pointer = *pointer - 20
	fmt.Println("after reassigning value at *pointer value is changed to", value)

	// Structs
	// A struct is a collection of fields.
	type Vertex struct {
		X int
		Y int
	}
	vertex := Vertex{1, 2}
	fmt.Println("vertex", vertex)
	vertex.X = 4
	fmt.Println("changed vertex", vertex)
	// Struct fields can be accessed through a struct pointer.
	vertexPointer := &vertex
	vertexPointer.X = 16
	fmt.Println("changed vertex with pointer", vertex)
	nextVertexPointer := &Vertex{X: 10, Y: 20}
	fmt.Println("nextVertexPointer", nextVertexPointer)

	// Arrays
	// The type [n]T is an array of n values of type T.
	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println("primes", primes)

	// Slices
	// An array has a fixed size. A slice, on the other hand, is a dynamically-sized,
	// flexible view into the elements of an array. In practice, slices are much more common than arrays.
	// a[low : high]
	// This selects a half-open range which includes the first element, but excludes the last one.
	// The following expression creates a slice which includes elements 1 through 3 of a:
	// a[1:4]
	var primesSlice []int = primes[1:4]
	fmt.Println("primesSlice", primesSlice)

	// Slices are like references to arrays
	// A slice does not store any data, it just describes a section of an underlying array.
	// Changing the elements of a slice modifies the corresponding elements of its underlying array.
	// Other slices that share the same underlying array will see those changes.

	// This is an array literal:
	// [3]bool{true, true, false}
	// And this creates the same array as above, then builds a slice that references it:
	// []bool{true, true, false}
	q := []int{2, 3, 5, 7, 11, 13}
	fmt.Println("q", q)

	s := []struct {
		i int
		b bool
	}{
		{2, true},
		{3, false},
		{5, true},
		{7, true},
		{11, false},
		{13, true},
	}
	fmt.Println("s", s)

	// Slice defaults
	// For the array
	// var a [10]int
	// these slice expressions are equivalent:
	// a[0:10]
	// a[:10]
	// a[0:]
	// a[:]

	// Slice length and capacity
	// The length and capacity of a slice s can be obtained using the expressions len(s) and cap(s).
	// The length of a slice is the number of elements it contains.
	// The capacity of a slice is the number of elements in the underlying array, counting from the first element in the slice.

	// Nil slices
	var nilSlice []int
	fmt.Printf("nilSlice len=%d cap=%d %v\n", len(nilSlice), cap(nilSlice), nilSlice)
	if nilSlice == nil {
		fmt.Println("nilSlice is nil!")
	}

	// Creating a slice with make

	// Appending to a slice
	var growingSlice []int
	printSlice("growingSlice", growingSlice)
	growingSlice = append(growingSlice, 2, 4, 8, 16)
	printSlice("growingSlice", growingSlice)

	// Range
	// The range form of the for loop iterates over a slice or map.
	// When ranging over a slice, two values are returned for each iteration. The first is the index, and the second is a copy of the element at that index.
	for index, value := range growingSlice {
		fmt.Printf("for range index=%d value=%d\n", index, value)
	}
	// for i, _ := range pow
	// for _, value := range pow
	// If you only want the index, you can omit the second variable.
	// for i := range pow

	// Maps
	// A map maps keys to values.
	// The zero value of a map is nil. A nil map has no keys, nor can keys be added.
	// The make function returns a map of the given type, initialized and ready for use.
	m := make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40, -74,
	}
	fmt.Println("map -> Bell Labs", m["Bell Labs"])

	// Map literals
	// Map literals are like struct literals, but the keys are required.
	m = map[string]Vertex{
		"Bell Labs": {
			40, -74,
		},
		"Google": {
			37, -122,
		},
	}
	fmt.Println("map literal", m)

	// Mutating maps
	// m[key] = elem

	// Retrieve an element:
	// elem = m[key]

	// Delete an element:
	// delete(m, key)

	// Test that a key is present with a two-value assignment:
	// elem, ok = m[key]
	// If key is in m, ok is true. If not, ok is false.
	// If key is not in the map, then elem is the zero value for the map's element type.

	// Function values
	// Functions are values too. They can be passed around just like other values.
	// Function values may be used as function arguments and return values.
	compute := func(fn func(float64, float64) float64) float64 {
		return fn(3, 4)
	}
	add := func(a, b float64) float64 {
		return a + b
	}
	fmt.Println("compute add (higher order function)", compute(add))

	// Go supports closures (capturing variables from outside its scope)
	outsideVar := 10
	// Define a closure that captures the variable `x`
	closure := func(y int) int {
		outsideVar += 5
		return outsideVar + y
	}
	fmt.Println("closure(5)", closure(5))
	fmt.Println("closure(5)", closure(5))

	adder := func() func(int) int {
		sum := 0
		return func(x int) int {
			sum += x
			return sum
		}
	}

	increment := adder()
	fmt.Println("increment(1)", increment(1))
	fmt.Println("increment(1)", increment(1))
	fmt.Println("increment(1)", increment(1))

	fibonacci := func(n int) int {
		if n <= 1 {
			return n
		}
		a, b := 0, 1
		for i := 2; i <= n; i++ {
			a, b = b, a+b
		}
		return b
	}

	for i := 0; i < 10; i++ {
		fmt.Printf("fibonacci(%d)=%d\n", i, fibonacci(i))
	}

	// Methods
	// Go does not have classes. However, you can define methods on types.
	// A method is a function with a special receiver argument.
	// The receiver appears in its own argument list between the func keyword and the method name.
	// func (v Vertex) Abs() float64 {
	// 	return math.Sqrt(v.X*v.X + v.Y*v.Y)
	// }
	// v := Vertex{3, 4}
	// fmt.Println(v.Abs())

	// Methods are functions
	// Remember: a method is just a function with a receiver argument.
	// Here's Abs written as a regular function with no change in functionality.
	// func Abs(v Vertex) float64 {
	// 	return math.Sqrt(v.X*v.X + v.Y*v.Y)
	// }

	// You can declare a method on non-struct types, too.
	// In this example we see a numeric type MyFloat with an Abs method.
	type MyFloat float64

	// Pointer receivers
	// Methods with pointer receivers can modify the value to which the receiver points
	// (as Scale does here). Since methods often need to modify their receiver,
	// pointer receivers are more common than value receivers.
	// func (v *Vertex) Scale(f float64) {
	// 	v.X = v.X * f
	// 	v.Y = v.Y * f
	// }

	// With a value receiver, the Scale method operates on a copy of the original Vertex value.
	// (This is the same behavior as for any other function argument.)
	// The Scale method must have a pointer receiver to change the Vertex value declared in the main function.

	// Methods and pointer indirection
	// Comparing the previous two programs, you might notice that functions with a pointer argument must take a pointer:
	// func ScaleFunc(v *Vertex, f float64) {
	// 	v.X = v.X * f
	// 	v.Y = v.Y * f
	// }
	// var v Vertex
	// ScaleFunc(v, 5)  // Compile error!
	// ScaleFunc(&v, 5) // OK

	// while methods with pointer receivers take either a value or a pointer as the receiver when they are called:
	// func (v *Vertex) Scale(f float64) {
	// 	v.X = v.X * f
	// 	v.Y = v.Y * f
	// }
	// var v Vertex
	// v.Scale(5)  // OK
	// p := &v
	// p.Scale(10) // OK

	// Functions that take a value argument must take a value of that specific type
	// methods with value receivers take either a value or a pointer as the receiver when they are called:

	// Choosing a value or pointer receiver
	// There are two reasons to use a pointer receiver.

	// The first is so that the method can modify the value that its receiver points to.
	// The second is to avoid copying the value on each method call. This can be more efficient if the receiver is a large struct, for example.
	// In general, all methods on a given type should have either value or pointer receivers, but not a mixture of both. (We'll see why over the next few pages.)

	// Interfaces
	// An interface type is defined as a set of method signatures.
	// A value of interface type can hold any value that implements those methods.
	type Abser interface {
		Abs() float64
	}
	// Interfaces are implemented implicitly
	// A type implements an interface by implementing its methods. There is no explicit declaration of intent, no "implements" keyword.
	// Implicit interfaces decouple the definition of an interface from its implementation,
	// which could then appear in any package without prearrangement.
	// type I interface {
	// 	M()
	// }
	// type T struct {
	// 	S string
	// }
	// This method means type T implements the interface I,
	// but we don't need to explicitly declare that it does so.
	// func (t T) M() {
	// 	fmt.Println(t.S)
	// }
	// func main() {
	// 	var i I = T{"hello"}
	// 	i.M()
	// }

	// Interface values
	// Under the hood, interface values can be thought of as a tuple of a value and a concrete type
	// Calling a method on an interface value executes the method of the same name on its underlying type.

	// Interface values with nil underlying values
	// If the concrete value inside the interface itself is nil, the method will be called with a nil receiver.
	// In some languages this would trigger a null pointer exception, but in Go it is common to write methods that gracefully handle being called with a nil receiver (as with the method M in this example.)

	// Nil interface values
	// Calling a method on a nil interface is a run-time error because there is no type inside the interface tuple to indicate which concrete method to call.
}
