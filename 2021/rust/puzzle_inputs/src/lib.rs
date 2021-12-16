pub mod inputs 
{
    use std::fs;
    
    pub fn day01() -> Vec<i32>
    {
        let path = "../../txtfiles/day01.txt";
        let data = fs::read_to_string(path).expect("Unable to read file");
        data.lines().map(|x| x.parse::<i32>().unwrap()).collect()
    }
    
    pub fn day02() -> Vec<(String, i32)>
    {
        let path = "../../txtfiles/day02.txt";
        let data = fs::read_to_string(path).expect("Unable to read file");

        let mut out_vec: Vec<(String, i32)> = Vec::new();
        
        for line in data.lines()
        {
            let mut iter = line.split_whitespace();
            out_vec.push((iter.next().unwrap().to_string(), iter.next().unwrap().parse::<i32>().unwrap()))
        }

        return out_vec;
    }

    pub fn day03() -> Vec<Vec<char>>
    {
        let path = "../../txtfiles/txtfiles/day03.txt";
        let data = fs::read_to_string(path).expect("Unable to read file");
        data.lines().map(|x| x.to_string().chars().collect()).collect()
    }

    pub fn day10() -> Vec<String>
    {
        let path = "../../txtfiles/day10.txt";
        let data = fs::read_to_string(path).expect("Unable to read file");
        data.lines().map(|x| x.to_string()).collect()
    }
}
