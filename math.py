set_num = int(input("Enter number of sets: "))

exercise ={}
for num in range(1, set_num +1):
  exercise["set{0}".format(num)] = input("Enter weight for set" + str(num) + ": ")

print(exercise)