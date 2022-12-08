use std::collections::{HashMap};
use crate::util::file::read_lines;

// See: https://adventofcode.com/2022/day/7

pub fn day7(env: &[String]) {
    let filename = &env[0];
    let lines = match read_lines(filename) {
        Ok(lines) => lines,
        Err(e) => {
            println!("ERROR: could not read filename {filename}: {e}");
            return;
        },
    };
    let debug = env.contains(&"--debug".to_owned());

    let mut path: Vec<String> = Vec::new();
    let mut dirs: HashMap<String, usize> = HashMap::new();
    let mut is_ls = false;
    for line in lines {
        if let Ok(data) = line {
            let parts: Vec<String> = data.split(" ").map(|s| s.to_string()).collect();
            let is_call = parts[0] == "$";
            if is_call {
                if is_ls {
                    is_ls = false;
                    // handle
                }
                let cmd = parts[1].to_string();
                match cmd.as_str() {
                    "cd" => {
                        let arg = parts[2].to_string();
                        match arg.as_str() {
                            "." => {}
                            ".." => {
                                path.pop();
                                if debug {
                                    println!("path {:?}", path)
                                }
                            }
                            _ => {
                                path.push(arg.clone());
                                if debug {
                                    println!("path {:?}", path)
                                }
                            }
                        }
                    }
                    "ls" => is_ls = true,
                    _ => panic!("Unknown command {}", cmd),
                }
            } else {
                if is_ls {
                    let dir_or_size = parts[0].to_string();
                    let name = parts[1].to_string();
                    if dir_or_size == "dir" {
                        if debug {
                            println!("dir {}", name);
                        }
                    } else {
                        let size = dir_or_size.parse::<usize>().unwrap();
                        for i in 0..path.len() {
                            let path_str = if i == 0 {
                                "/".to_string()
                            } else {
                                ["/".to_string(), path[1..i + 1].join("/")].concat()
                            };
                            *dirs.entry(path_str).or_insert(0) += size;
                        }
                        if debug {
                            println!("file {} size {}", name, size);
                        }
                    }
                } else {
                    panic!("Unknown entry in non-ls mode {}", data);
                }
            }
        }
    }
    if debug {
        for x in dirs.iter() {
            println!("{:?}", x)
        }
    }
    println!(
        "Total dir size {}",
        dirs.iter()
            .filter(|&(_, v)| *v <= 100000)
            .map(|(_, v)| v)
            .sum::<usize>()
    );
}
