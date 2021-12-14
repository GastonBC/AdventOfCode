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

# make rules count dict
for line in puz_input.splitlines():
    line = line.replace(" ", "")
    if "->" in line:
        rule_ = line.split("->")
        res_ = rule_[1]
        cond = rule_[0]

        # The polymer process division
        result = ([cond[0]+res_, res_+cond[1]])
        rules[cond] = result
        rules_count[cond] = 0

        # Set up characters in the dict
        ch_occ[cond[0]] = 0
        ch_occ[cond[1]] = 0
        ch_occ[res_] = 0

# Template line, after the dicts initialization
# to be able to add counters easy
for line in puz_input.splitlines():
    line = line.replace(" ", "")
    if "->" not in line:
        for i, ch in enumerate(line):
            if i != len(line)-1:
                cond = ch+line[i+1]
                rules_count[cond] += 1
                
steps = 10

for step in range(steps):

    rule_count_copy = rules_count.copy()
    for rl in rule_count_copy:
        
        if rule_count_copy[rl] > 0:
            
            res = rules[rl]

            # the new elements count will each new poly count plus
            # the original poly count
            rules_count[res[0]] += rule_count_copy[rl]
            rules_count[res[1]] += rule_count_copy[rl]
            rules_count[rl] -= rule_count_copy[rl]

for rl in rules_count:
    # first char
    ch_occ[rl[0]] += rules_count[rl]

    # second 
    ch_occ[rl[1]] += rules_count[rl]


# Dumb proper decimal rounding method
from decimal import localcontext, Decimal, ROUND_HALF_UP
with localcontext() as ctx:
    ctx.rounding = ROUND_HALF_UP

    mx = Decimal(max(ch_occ.values())/2)
    mn = Decimal(min(ch_occ.values())/2)
    mx = mx.to_integral_value()
    mn = mn.to_integral_value()
    
    print("Answer is:", mx-mn)

'''
Answer is: 2584
'''