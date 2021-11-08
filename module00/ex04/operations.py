import sys

if len(sys.argv) != 3:
	if (len(sys.argv) > 3):
		print("InputError: too many arguments")
	elif (len(sys.argv) == 0):
		print("Usage: python operations.py <number1> <number2>\nExample: python operations.py 10 3")
	exit()
try:
	int(sys.argv[1])
except ValueError:
	print("InputError:  cd", sys.argv[1])
	exit()
try: 
	int(sys.argv[2])
except ValueError:
	print("this is not an integer", sys.argv[2])
	exit()
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print("Sum:		", num1 + num2)
print("Difference: 	", num1 - num2)
print("Product:	", num1	* num2)
try:
	num1 / num2
except ZeroDivisionError as err:
	print("Quotient: ", err)
	print("Remainder: ", err)
	exit()
print("Quotient:	", num1 / num2)
print("Remainder:	", num1 % num2)