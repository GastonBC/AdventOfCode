import Inputs

sample = [  r"[({(<(())[]>[[{[]{<()<>>",
            r"[(()[<>])]({[<{<<[]>>(",
            r"{([(<{}[<>[]}>{[]{[(<()>",
            r"(((({<>}<{<{<>}{[]{[]{}",
            r"[[<[([]))<([[{}[[()]]]",
            r"[{[{({}]{}}([{[{{{}}([]",
            r"{<[[]]>}<{[{[{[]{()[[[]",
            r"[<(<(<(<{}))><([]([]()",
            r"<{([([[(<>()){}]>(<<{{",
            r"<{([{{}}[<[[[<>{}]]]>[]]"]

def get_points(ch):
    prizes = {
                ')': 3,
                ']': 57,
                '}': 1197,
                '>': 25137
             }
    return prizes.get(ch, 0)


def check(chunks):
    stack = []
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']

    for ch in chunks:
        if ch in opening:
            stack.append(ch)

        elif ch in closing:
            idx = closing.index(ch)

            # Correctly closed chunk
            if opening.index(stack[-1]) == idx:
                stack.pop(-1)
                continue

            # incorrectly closed chunk
            else:
                print(f"Unbalanced {ch} - {get_points(ch)} points")
                return get_points(ch)
        
    # finally check if closings are missing by the remaining stack leftovers
    if stack.count != 0:
        print("Incomplete")
        return 0
    else:
        print("All good")
        return 0

points = 0

puz_input = Inputs.Day10()

for chnks in puz_input:
    points += check(chnks)

print(f"Answer is {points}")

'''
Answer is 311949
'''