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
        
        let mut tmp_pass = 0;

        for (idx, pass_ch) in pass.chars().enumerate()
        {
            if (idx+1 == mn && ch == pass_ch)|| 
               (idx+1 == mx && ch == pass_ch)
            {
                tmp_pass += 1;
            }
        }

        if tmp_pass == 1
        {
            valid_passes += 1;
        }

    }

    println!("{} valid passwords", valid_passes)
}

// 321 valid passwords