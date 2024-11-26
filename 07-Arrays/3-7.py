arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
length = ""
for name in arr:
    if len(name) > len(length):
        length = name

print("Names: ", end="")
for name in arr:
    print(name, end=" ")
print()
print("Longest name:", length)

        