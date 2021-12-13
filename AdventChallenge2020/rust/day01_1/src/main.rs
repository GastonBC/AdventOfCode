use puzzle_inputs;

fn main() {
    let puz_input = puzzle_inputs::inputs::day01();

    for n in &puz_input
    {
        let result = 2020-n;
        if puz_input.contains(&result)
        {
            println!("winning number is: {}", result*n);
            return;
        }
    }
}
