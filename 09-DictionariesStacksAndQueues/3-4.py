import queue

number = int(input("Enter number: "))
bin = queue.LifoQueue()
while number > 0:
    bin.put(number%2)
    number //= 2

while not bin.empty():
    print(bin.get(), end="")