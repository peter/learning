use std::env;
use std::collections::HashMap;

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

fn main() {
    // Creating a HashMap
    // If you want values of different types you need to use an enum, see:
    // https://stackoverflow.com/questions/39146584/how-do-i-create-a-rust-hashmap-where-the-value-can-be-one-of-multiple-types
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
    let person = Person {
        name: "John".to_string(),
        age: 42,
    };
    dbg!(&person);
    println!("Person name={} age={}", person.name, person.age);    

}
