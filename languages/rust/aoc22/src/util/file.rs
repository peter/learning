use std::fs::File;
use std::io::{BufRead, BufReader, Lines, Result};
use std::path::Path;

pub fn read_lines<P>(filename: P) -> Result<Lines<BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(BufReader::new(file).lines())
}
