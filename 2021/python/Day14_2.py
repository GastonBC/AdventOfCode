import Inputs


sample = '''NNCB
        CH -> B
        HH -> N
        CB -> H
        NH -> C
        HB -> C
        HC -> B
        HN -> C
        NN -> C
        BH -> H
        NC -> B
        NB -> B
        BN -> B
        BB -> N
        BC -> B
        CC -> N
        CN -> C'''

def poly_length(poly):
    counter = 0
    for pair in poly:
        counter += poly[pair]
    # +1 because the last character doesn't have two pairs assigned
    return counter+1


puz_input = Inputs.Day14()
# puz_input = sample

rules = dict()
rules_count = dict()
ch_occ = dict()

input_template = puz_input.splitlines()[0]
input_rules = puz_input.splitlines()[1:]

# make rules count dict
for line in input_rules:
    line = line.replace(" ", "")
    
    inp_rule = line.split("->")
    cond = inp_rule[0]
    res_ = inp_rule[1]
    

    # The polymer process division
    result = ([cond[0]+res_, res_+cond[1]])
    rules[cond] = result
    rules_count[cond] = 0
    

# Template line, after the dicts initialization
# to be able to add counters easy
input_template = input_template.replace(" ", "")
i=0
while i < len(input_template)-1:
    cond = input_template[i]+input_template[i+1]
    rules_count[cond] += 1
    i += 1
            
steps = 40

for step in range(steps):

    rule_count_copy = rules_count.copy()
    for rl in rule_count_copy:

        if rule_count_copy[rl] > 0:
            
            res = rules[rl]

            # the new elements count will each new poly count plus
            # the original poly count
            rules_count[res[0]] += rule_count_copy[rl]
            rules_count[res[1]] += rule_count_copy[rl]

            # The original pair gets used
            rules_count[rl] -= rule_count_copy[rl]

# For each character in every pair, add it's count to 
# the character occurrences dict
for rl in rules_count:
    # first char
    ch_occ[rl[0]] = ch_occ.get(rl[0], 0) + rules_count[rl]
    # second 
    ch_occ[rl[1]] = ch_occ.get(rl[1], 0) + rules_count[rl]


# Round .5 values up
from math import ceil

mx = ceil(max(ch_occ.values())/2)
mn = ceil(min(ch_occ.values())/2)

print("Answer is:", mx-mn)


print("String lenght:", poly_length(rules_count))

# Correct answers
assert mx-mn == 3816397135460
assert poly_length(rules_count) == 20890720927745