from threading import Thread
def increment_counter():
    global counter
    for _ in range(100000):
        counter += 1

def decrement_counter():
    global counter
    for _ in range(100000):
        counter -= 1

#shared counter variable

#create two threads that modify a shared counter without synchronization
thread1 = Thread(target=increment_counter)
thread2 = Thread(target=decrement_counter)

#start the threads
thread1.start()
thread2.start()

#wait for both threads to finish
thread1.join()
thread2.join()

#print the final value of the counter
print("Final counter value:", counter)