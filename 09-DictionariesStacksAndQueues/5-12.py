import queue
str = input("Enter any text: ")
length = len(str)
stack = queue.LifoQueue()
for char in str:
    stack.put(char)
for i in range(length):
    print(stack.get(), end='')