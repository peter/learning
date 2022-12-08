use std::env;
use day7::day7;

pub mod util;
pub mod day7;

fn parse_day(args: &Vec<String>) -> Result<i32, String> {
    if args.len() < 2 {
        return Err("Missing day argument".to_string());
    }
    if let Ok(day) = args[1].parse::<i32>() {
        Ok(day)
    } else {
        Err("Could parse day argument as integer".to_string())
    }
}

fn parse_env(args: &Vec<String>) -> &[String] {
    if args.len() < 3 { &[] } else { &args[2..] }
}

fn execute(args: &Vec<String>) -> Result<(), String> {
    let day = match parse_day(&args) {
        Ok(day)  => day,
        Err(e) => return Err(e),
    };
    let env = parse_env(args);
    match day {
        7 => day7(env),
        _ => return Err("Have not implemented day {day} - sorry!".to_string())
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    match execute(&args) {
        Ok(_) => println!("OK"),
        Err(e) => println!("ERROR: {e}"),
    }
}
