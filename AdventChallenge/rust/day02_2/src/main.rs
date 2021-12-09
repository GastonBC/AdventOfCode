struct Submarine
{
    x: i32,
    y: i32,
    aim: i32
}

fn new_sub() -> Submarine
{
    Submarine {x: 0, y: 0, aim: 0}
}

impl Submarine
{
    fn forward(&mut self, value: i32)
    {
        self.x += value;
        self.y += self.aim*value;
    }

    fn up(&mut self, value: i32)
    {
        // Up and down are backwards because it's a submarine
        self.aim -= value;
    }

    fn down(&mut self, value:i32)
    {
        self.aim += value;
    }
}

use puzzle_inputs;

fn main() 
{
    let mut sub = new_sub();

    for (action, val) in puzzle_inputs::inputs::day02()
    {
        match action 
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