use std::collections::HashMap;
use puzzle_inputs;
// This one focuses on the incomplete lines


fn get_points(ch_stack: &Vec<char>) -> i64
{
    let mut score: i64 = 0;
    let prizes: HashMap<char, i64> = HashMap::from([
                                ('(', 1),
                                ('[', 2),
                                ('{', 3),
                                ('<', 4),
                               ]);

    for ch in ch_stack
    {
        score = score*5;
        match prizes.get(&ch)
        {
            Some(&prize) => score += prize,
            None => score += 0
        }
    }
    return score;
}

fn check(chunks: &str) -> i64
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
                        println!("Unbalanced");
                        return 0
                    }
                 }
                
                // No items left on the stack means there cannot be a closing character
                None => 
                {
                    println!("Unbalanced");
                    return 0
                }
            }
        }
    }

    // loop has ended
    // An empty stack means all chunks closed correctly
    if stack.len() != 0
    {
        stack.reverse();
        let score = get_points(&stack);
        println!("Incomplete");
        return score;
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
    let mut scores: Vec<i64> = Vec::new();

    for chunk in puz_input
    {
        let score = check(chunk);
        if score != 0
        {
            scores.push(score);
        }
    }

    // Sort the vector. Unstable means it may not preserve the order of equal elements
    // since we don't care about the order of those, use unstable because it's faster
    scores.sort_unstable();

    // Get middle result
    let idx = (scores.len()-1)/2;

    println!("Answer is {}", scores[idx])
}

/*
Answer is 311949
*/

