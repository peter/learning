use serde_json::{Result, Value};
use serde::{Deserialize, Serialize};

fn untyped_example() -> Result<()> {
    // Some JSON input data as a &str. Maybe this comes from the user.
    let data = r#"
    {
        "name": "John Doe",
        "age": 43,
        "phones": [
            "+44 1234567",
            "+44 2345678"
        ]
    }"#;

    // Parse the string of data into serde_json::Value.
    let v: Value = serde_json::from_str(data).unwrap();

    // Access parts of the data by indexing with square brackets.
    // If there is no value at the given path then null is returned
    println!("untyped_example: call {} at the number {}", v["name"], v["phones"][0]);

    Ok(())
}

#[derive(Serialize, Deserialize, Debug)]
struct Person {
    name: String,
    country: Option<String>,
    age: u8,
    phones: Vec<String>,
}

fn typed_example() -> Result<()> {
    let data = r#"
    {
        "name": "John Doe",
        "age": 43,
        "phones": [
            "+44 1234567",
            "+44 2345678"
        ]
    }
    "#;

    let p: Person = serde_json::from_str(data).unwrap();

    // Array index access out of bounds will yield a panic, i.e. p.phones[99]
    println!("typed_example: call {} at the number {}", p.name, p.phones[1]);

    // let country = match p.country {
    //     Some(c) => c,
    //     None => "unknown".to_string(),
    // };
    // println!("typed_example: country variable match {}", country);

    // You can inline match expressions
    // println!("typed_example: country inlined match {}", (match p.country {
    //     Some(c) => c,
    //     None => "unknown".to_string(),
    // }));

    let default_country = "unknown country".to_string();
    println!("typed_example: country unwrap_or() {}", p.country.unwrap_or(default_country));

    Ok(())
}

fn main() {
    untyped_example().unwrap();
    typed_example().unwrap();
}
