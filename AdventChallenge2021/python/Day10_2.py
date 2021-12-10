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

def get_points(ch_stack):
    score = 0
    for ch in ch_stack:
        score = score * 5
        prizes = {
                    '(': 1,
                    '[': 2,
                    '{': 3,
                    '<': 4
                }

        char_points = prizes.get(ch, 0)
        score += char_points    
    return score


def check(chunks):
    stack = []
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']

    for ch in chunks:
        if ch in opening:
            stack.append(ch)

        elif ch in closing:
            idx = closing.index(ch)

            # Correctly closed chunk is the last item in the list
            if opening.index(stack[-1]) == idx:
                stack.pop(-1)
                continue

            # incorrectly closed chunk
            else:
                print(f"Unbalanced")
                return 0
        
    # finally check if closings are missing by the remaining stack leftovers
    if stack.count != 0:
        rev_stack = reversed(stack)   # Need to reverse the order so the last one is the
        score = get_points(rev_stack) # first checked

        print(f"Incomplete. Points {score}")
        return score
    else:
        print("All good")
        return 0

puz_input = Inputs.Day10()

points = []

for chnks in puz_input:
    chnk_score = check(chnks)
    if chnk_score != 0:
        points.append(check(chnks))

points.sort()
mid_idx = round((len(points)-1)/2)
middle_score = points[mid_idx]

print(f"Answer is {middle_score}")

'''
Answer is 3042730309
'''