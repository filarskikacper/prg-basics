import queue
que = queue.Queue()
while True:
    customer = input("Enter name of customer: ")
    que.put(customer)
    print(f'Number: {que.qsize()}')
