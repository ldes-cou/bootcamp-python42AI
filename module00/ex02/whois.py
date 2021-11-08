import sys

user_input = sys.argv[1]

if len(sys.argv) > 2:
    print("There are too many arguments")
    exit()
try:
    int(user_input)
except ValueError:
    print("you need to enter an integer", sys.argv[1])
    exit()
if (int(sys.argv[1])) == 0:
    print("{0} I'm Zero".format(sys.argv[1]))
elif (int(sys.argv[1]) % 2) == 0:
    print("{0} I'm Even".format(sys.argv[1]))
else:
    print("{0} I'm Odd".format(sys.argv[1]))
