use puzzle_inputs;

fn main() {
    let puz_input = puzzle_inputs::inputs::day02();
    let mut valid_passes = 0;
    
    for line in puz_input
    {
        let split = line.split(" ");
        let vec: Vec<&str> = split.collect();

        // Parse into useful variables
        let mn = vec[0].split("-").collect::<Vec<&str>>()[0].parse::<usize>().unwrap();
        let mx = vec[0].split("-").collect::<Vec<&str>>()[1].parse::<usize>().unwrap();
        let ch = vec[1].chars().next().unwrap();
        let pass = vec[2];
        
        let pass_occ = pass.matches(ch).count();

        if mn <= pass_occ && mx >= pass_occ
        {
            valid_passes += 1;
        }
    }

    println!("{} valid passwords", valid_passes)
}
