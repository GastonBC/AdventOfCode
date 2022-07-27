import Inputs

for idx, n in enumerate(Inputs.Day01()):
    for i in Inputs.Day01()[idx+1:]:
        if n+i == 2020:
            print(n*i)
            break
    else:
        continue  # only executed if the inner loop did NOT break
    break  # only executed if the inner loop DID break