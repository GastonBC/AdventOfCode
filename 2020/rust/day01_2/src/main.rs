use puzzle_inputs;

fn main() {
    let puz_input = puzzle_inputs::inputs::day01();
    
    for n in &puz_input
    {
        for i in &puz_input
        {
            let part_res = 2020-n-i;

            if puz_input.contains(&part_res)
            {
                let result = part_res*n*i;
                println!("winning number is: {}", result);
                return;
            }
        }
    }
}
