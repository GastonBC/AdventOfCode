pub mod inputs 
{

    use std::fs;

    pub fn day01() -> Vec<i32>
    {
        let path = "../../txtfiles/day01.txt";

        let data = fs::read_to_string(path).expect("Unable to read file");
        let lines:Vec<i32> = data.lines().map(|x| x.parse::<i32>().unwrap()).collect();

        return lines;   
    }

    pub fn day02() -> Vec<String>
    {
        let path = "../../txtfiles/day02.txt";
        let data = fs::read_to_string(path).expect("Unable to read file");
        let lines:Vec<String> = data.lines().map(|x| x.parse::<String>().unwrap()).collect();
        return lines;
    }
}
