import Inputs

Input = Inputs.Day06()

for idx in range(0, len(Input)):
    sequence = Input[idx:idx+4]
    if len(set(sequence)) == 4:
        print(sequence, idx+4)

        assert idx+4 == 1896
        break

