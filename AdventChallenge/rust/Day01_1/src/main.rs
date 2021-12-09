use puzzle_inputs;

fn main() {
    
    let mut increase_count = 0;
    
    let measurements = puzzle_inputs::inputs::day01();
    for (idx, m) in measurements.iter().enumerate()
    {
        if idx == 0
        {
            continue;
        }
        if m > &measurements[idx-1]
        {
            increase_count += 1;
        }
    }
    println!("Answer {}", increase_count)
}
