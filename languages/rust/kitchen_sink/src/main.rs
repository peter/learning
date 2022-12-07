use std::env;
use std::collections::HashMap;

fn main() {
    let config = HashMap::from([
        ("FOOBAR", 2), ("BLABLA", 4)
    ]);

    println!("Env var FOOBAR={}", env::var("FOOBAR").unwrap_or("default value".to_string()));

    println!("config={:?}", config);

    config.get("FOOBAR").map(|v| println!("config.FOOBAR={}", v));
    println!("config.FOOBAR={}", config.get("FOOBAR").unwrap_or(&123));

    println!("config.FOOOOBAR={}", config.get("FOOOOBAR").unwrap_or(&0));
}
