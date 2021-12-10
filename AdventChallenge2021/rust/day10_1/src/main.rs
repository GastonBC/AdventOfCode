use std::collections::HashMap;
use puzzle_inputs;

fn get_points(ch: &char) -> i32
{
    let prizes: HashMap<char, i32> = HashMap::from([
                                (')', 3),
                                (']', 57),
                                ('}', 1197),
                                ('>', 25137),
                               ]);

    match prizes.get(&ch)
    {
        Some(&prize) => prize,
        None => 0
    }
                    
}

fn check(chunks: &str) -> i32
{
    let mut stack: Vec<char> = Vec::new();

    let open_close_ch: HashMap<char, char> = HashMap::from([
        ('(', ')'),
        ('[', ']'),
        ('{', '}'),
        ('<', '>'),
        ]);

    for ch in chunks.chars()
    {
        // It's an opening char
        if open_close_ch.contains_key(&ch)
        {
            stack.push(ch)
        }

        // It's a closing character. Last char in stack MUST be equal to it's closing counter
        else
        {
            match stack.last()
            {
                Some(opening_ch) =>
                { 
                    // Get the closing char. unwrap is safe to use because it was checked when added
                    let closing_ch = open_close_ch.get(opening_ch).unwrap();
                    
                    // Correctly closed chunk
                    if &ch == closing_ch
                    {
                        // Pop removes the last element of the vector
                        stack.pop();
                        continue;
                    }

                    // Incorrectly closed chunk. Corrupted string
                    else
                    {
                        println!("Unbalanced {} - {} points", ch, get_points(&ch));
                        return get_points(&ch);
                    }
                 }
                
                // No items left on the stack means there cannot be a closing character
                None => 
                {
                    println!("Unbalanced {} - {} points", ch, get_points(&ch));
                    return get_points(&ch);
                }
            }
        }
    }

    // loop has ended
    // An empty stack means all chunks closed correctly
    if stack.len() != 0
    {
        println!("Incomplete");
        return 0;
    }
    // Items remaining in the stack mean some chunks were not closed
    else
    {
        println!("All good");
        return 0;
    }

    
}


fn main() {

    let sample = vec![r"[({(<(())[]>[[{[]{<()<>>",
                      r"[(()[<>])]({[<{<<[]>>(",
                      r"{([(<{}[<>[]}>{[]{[(<()>",
                      r"(((({<>}<{<{<>}{[]{[]{}",
                      r"[[<[([]))<([[{}[[()]]]",
                      r"[{[{({}]{}}([{[{{{}}([]",
                      r"{<[[]]>}<{[{[{[]{()[[[]",
                      r"[<(<(<(<{}))><([]([]()",
                      r"<{([([[(<>()){}]>(<<{{",
                      r"<{([{{}}[<[[[<>{}]]]>[]]"];
    

    let puz_input = puzzle_inputs::inputs::day10();
    let mut score = 0;

    for chunk in puz_input
    {
        score += check(chunk);
    }
    println!("Answer is {}", score)
}

/*
Answer is 311949
*/

