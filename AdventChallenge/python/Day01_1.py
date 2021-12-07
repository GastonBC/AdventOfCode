import Inputs

measurements = Inputs.Day01()

increase_count = 0

for idx, m in enumerate(measurements):
    if idx == 0:
        continue

    if m > measurements[idx-1]:
        increase_count += 1

print(increase_count)

'''1715'''

# visualization
import matplotlib.pyplot as plt
sample = Inputs.Day01()

for x in range(len(sample)):
    if x == 0:
        continue

    point1 = (x-1, sample[x-1])
    point2 = (x, sample[x])

    x_values = [point1[0], point2[0]]

    y_values = [point1[1], point2[1]]


    plt.plot(x_values, y_values)

plt.show()
# visualization