use puzzle_inputs;

fn main() {
    let mut increase_count = 0;
    
    let measurements = puzzle_inputs::inputs::day01();
    
    for (idx, _) in measurements.iter().enumerate()
    {
        if idx == measurements.iter().count()-3
        {
            break;
        }

        let a = measurements[idx] + measurements[idx+1] + measurements[idx+2];
        let b = measurements[idx+1] + measurements[idx+2] + measurements[idx+3];
  
        if b > a
        {
            increase_count += 1;
        }
    }
    println!("Answer {}", increase_count)
}