pub mod inputs 
{

    use std::fs;

    pub fn day01() -> Vec<i32>
    {
        let path = "../puzzle_inputs/src/txtfiles/day01.txt";

        let data = fs::read_to_string(path).expect("Unable to read file");
        let lines:Vec<i32> = data.lines().map(|x| x.parse::<i32>().unwrap()).collect();

        return lines;   
    }

    pub fn day02()
    {
        let path = "../puzzle_inputs/src/txtfiles/day02.txt";
        
    }
}
