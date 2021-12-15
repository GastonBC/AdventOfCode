mod submarine;
pub use submarine::submarine::Submarine;

use puzzle_inputs;

fn main() 
{
    let mut sub = Submarine::new();

    for (action, val) in puzzle_inputs::inputs::day02()
    {
        match action.as_str()
        {
            "forward" => sub.forward(val),
            "down" => sub.down(val),
            "up" => sub.up(val),
            _ => panic!("Unresolved pattern")
        }
    }

    println!("Submarine forwards distance: {}", sub.x);
    println!("Submarine depth: {}", sub.y);
    println!("Result: {}", sub.x*sub.y);
}