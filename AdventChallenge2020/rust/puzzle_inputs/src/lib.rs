pub mod inputs 
{
    use std::fs;

    pub fn day01() -> Vec<u32>
    {
        let data = fs::read_to_string("day01.txt").expect("Unable to read file");
        let lines:Vec<u32> = data.lines().map(|x| x.parse::<u32>().unwrap()).collect();

        return lines;   
    }
}
