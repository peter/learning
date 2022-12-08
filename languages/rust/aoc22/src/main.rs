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

fn parse_env(args: &Vec<String>) -> Result<&[String], String> {
    if args.len() < 3 {
        return Err("Missing environment argument".to_string());
    }
    Ok(&args[2..])
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let day = match parse_day(&args) {
        Ok(day)  => day,
        Err(e) => {
            println!("ERROR: {}", e);
            return;
        },
    };
    let env = match parse_env(&args) {
        Ok(env)  => env,
        Err(e) => {
            println!("ERROR: {}", e);
            return;
        },
    };
    match day {
        7 => day7(env),
        _ => {
            println!("Have not implemented day {day} - sorry!");
            return;
        }
    }
}
