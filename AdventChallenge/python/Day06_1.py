import Inputs

sample = [3,4,3,1,2]

class Lanternfish:
    def __init__(self, age):
        self.age = age
    
    def create_new_check(self):
        if self.age < 0:
            self.age = 6
            return Lanternfish(8)

        else:
            return None

    def day_passed(self):
        self.age -= 1

lanternfish_lst = [Lanternfish(age) for age in Inputs.Day06()]

for day_n in range(0, 80):
    for lanternfish in lanternfish_lst.copy():
        lanternfish.day_passed()
        new_fish = lanternfish.create_new_check()

        if new_fish is not None:
            lanternfish_lst.append(new_fish)

print(len(lanternfish_lst))

'''
sample = 5934
answer = 352872'''
