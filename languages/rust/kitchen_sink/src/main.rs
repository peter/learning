use std::env;
use std::collections::HashMap;
use rand::Rng;

#[derive(Debug, PartialEq)]
struct Person {
    name: String,
    age: u8,
}

struct Number {
    odd: bool,
    value: i32,
}

fn get_thing() -> (String, i32) {
    ("OK".to_string(), 42)
}

fn random_number() -> f32 {
    rand::thread_rng().gen_range(0.0..1.0)
}

fn print_number(n: Number) {
    match n.value {
        1 => println!("One"),
        2 => println!("Two"),
        _ => println!("{}", n.value),
    }
}

fn main() {
    // Creating a HashMap
    // If you want values of different types you need to use an enum, see:
    // https://stackoverflow.com/questions/39146584/how-do-i-create-a-rust-hashmap-where-the-value-can-be-one-of-multiple-types
    // Variable bindings are immutable by default, which means their interior can't be mutated:
    // And also that they cannot be assigned to
    let config = HashMap::from([
        ("FOOBAR", 2),
        ("BLABLA", 3)
    ]);

    // Reading from a HashMap
    config.get("FOOBAR").map(|v| println!("map config.FOOBAR={}", v));
    println!("get.unwrap_or config.FOOBAR={}", config.get("FOOBAR").unwrap_or(&123));
    println!("get.unwrap_or config.FOOOOBAR={}", config.get("FOOOOBAR").unwrap_or(&0));

    // You can use the dbg! macro for debug printouts
    dbg!(config);

    // Creating a Vector - it needs to be mutable to be able to push to it
    let mut my_vector = vec![1, 2];
    my_vector.push(3);
    dbg!(&my_vector);

    // For loop with a tuple of index and value
    for (index, value) in my_vector.iter().enumerate() {
        println!("vector for loop my_values index={:?} value={:?}", index, value);
    }

    // Reading an environment variable
    let foobar = env::var("FOOBAR").unwrap_or("default value".to_string());
    println!("Env var FOOBAR={foobar}");

    // Creating a struct
    let person1 = Person {
        name: "John".to_string(),
        age: 42,
    };
    let person2 = Person {
        name: "John".to_string(),
        age: 42,
    };
    dbg!(&person1);
    println!("Person1 name={} age={}", person1.name, person1.age);
    println!("person1 == person2 {}", person1 == person2);

    // The underscore _ is a special name - or rather, a "lack of name". It basically means to throw away something:
    // this does *nothing* because 42 is a constant
    let _ = 42;
    // this calls `get_thing` but throws away its result
    let _ = get_thing();
    println!("{:?}", get_thing());

    // Names that start with an underscore are regular names, it's just that the compiler won't warn about them being unused:
    let _x = 42;

    // Separate bindings with the same name can be introduced - you can shadow a variable binding:
    let _x = _x + 3;
    // the assert_eq! will panic if the two values are not equal
    assert_eq!(_x, 45);
    // using `_x` after that line only refers to the second `_x`, the first `_x` no longer exists.


    // Rust has tuples, which you can think of as "fixed-length collections of values of different types".
    // Characters use single quotes and strings use double quotes
    let _pair = ('a', 17);

    // Tuples can be destructured when doing an assignment, This is especially useful when a function returns a tuple
    let (_some_string, _some_int) = get_thing();
    // Of course, when destructuring a tuple, _ can be used to throw away part of it:
    let (_, _some_int) = get_thing();

    // The semi-colon marks the end of a statement so statements can span multiple lines
    let vector = vec![1, 2, 3]
        .iter()
        .map(|x| x + 3)
        .fold(0, |x, y| x + y);
    dbg!(vector);
    // The fold function folds every element into an accumulator

    // The reduce and fold functions are similar but reduce does not take an initial value
    // and reduce returns a Result with None if the iterator is empty:
    // https://docs.rs/reduce/latest/reduce/
    let vector = vec![1, 2, 3]
        .iter()
        .map(|x| x + 3)
        .reduce(|x, y| x + y);
    dbg!(vector);
    let vector = vec![]
        .iter()
        .map(|x| x + 3)
        .reduce(|x, y| x + y);
    dbg!(vector);

    // Here is a void function
    fn greet() {
        println!("Hi from the void function!");
    }
    greet();    

    fn _fair_dice_roll() -> i32 {
        4
    }
    // "omitting the semicolon at the end of a function" is the same as returning

    // A pair of brackets declares a block, which has its own scope:
    let x = "outer";
    {
        let x = "inner";
        println!("in block x={}", x);
    }
    println!("after block x={}", x);

    // Blocks are also expressions, which mean they evaluate to.. a value.
    let _x = { 42 };
    let _x = {
        let y = 1; // first statement
        let z = 2; // second statement
        y + z // this is the *tail* - what the whole block will evaluate to
    };

    // if conditionals are also expressions:    
    fn _unfair_dice_roll() -> i32 {
        if random_number() < 0.5 {
            1
        } else {
            2
        }
    }
    println!("_unfair_dice_roll {}", _unfair_dice_roll());
    println!("random_number() {}", random_number());

    let number = Number { odd: true, value: 1 };
    println!("number.odd {}", number.odd);
    print_number(number);

    // A match has to be exhaustive: at least one arm needs to match.
    // _ can be used as a "catch-all" pattern
}
