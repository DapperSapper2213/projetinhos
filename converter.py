def calc_1_2(val1):
    miles = val1 * 0.621371
    return float(miles)
def calc_2_1(val1):
    km = val1 * 1.60934
    return float(km)
    

print("What will you convert?\n1. Kilometers to miles\n2. Miles to kilometers")
decider = int(input(""))

if decider == 1:
    num1 = int(input("Great! Now, add the units!\n"))
    result = calc_1_2(num1)
    print(f"Here's the total conversion: {result:.2f}")
elif decider == 2:
    num1 = int(input("Great! Now, add the units!\n"))
    result = calc_2_1(num1)
    print(f"Here's the total conversion: {result:.2f}")
else:
    print("Wrong input!")
    exit(0)
input("Press 'Enter' to exit!")
