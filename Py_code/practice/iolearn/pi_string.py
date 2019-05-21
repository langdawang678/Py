filename='pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

age = input('input your age there :')
if age in pi_string:
    print("yes,your age is in pi")
else:
    print("no")