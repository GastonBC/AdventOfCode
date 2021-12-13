pub mod submarine
{
    pub struct Submarine
    {
        pub x: i32,
        pub y: i32,
        pub aim: i32
    }

    impl Submarine
    {

        pub fn new() -> Self
        {
            Self {x: 0, y: 0, aim: 0}
        }

        pub fn forward(&mut self, value: i32)
        {
            self.x += value;
            self.y += self.aim*value;
        }
    
        pub fn up(&mut self, value: i32)
        {
            // Up and down are backwards because it's a submarine
            self.aim -= value;
        }
    
        pub fn down(&mut self, value:i32)
        {
            self.aim += value;
        }
    }
}