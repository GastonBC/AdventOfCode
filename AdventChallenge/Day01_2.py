import Inputs


measurements = Inputs.Day01_2()

increase_count = 0

for idx, m in enumerate(measurements):

    if idx == len(measurements)-3:
        break

    a = measurements[idx] + measurements[idx+1] + measurements[idx+2]
    b = measurements[idx+1] + measurements[idx+2] + measurements[idx+3]

    if b > a:
        increase_count += 1

print(increase_count)
