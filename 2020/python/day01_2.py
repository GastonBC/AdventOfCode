import Inputs

for idx, n in enumerate(Inputs.Day01()):
    for i in Inputs.Day01()[idx+1:]:
        for o in Inputs.Day01()[idx+2:]:
            if n+i+o == 2020:
                print(n*i*o)
                break
        else:
            continue
        break
    else:
        continue
    break