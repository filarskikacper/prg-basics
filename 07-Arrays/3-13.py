array = [15, 38, 7, 23, 14]

def occurs(number, array):
    if number in array:
        return True
    
number = int(input("Number: "))
print("Array:", array)
if occurs(number,array) == True:
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")