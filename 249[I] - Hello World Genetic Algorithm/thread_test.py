import threading
from queue import Queue
import time

lock = threading.Lock()

#Print item pulled from queue
def do_work(num):
	#Pretend to do work
	#time.sleep(0.1)
	with lock:
		print(num)
		print("Current thread:", str(threading.current_thread()).split(",")[0].split("-")[1]) #Prints just the thread number, not identifier. The order the threads were created in is the number starting at 1
		print("Thread ident:", threading.get_ident())
#Pull items from queue to process
def worker():
	while True:
		item = q.get()
		do_work(item)
		q.task_done()

if __name__ == "__main__":
	thread_num = 4
	queue_num = 10
	thread_list = []
	#Create threads
	for i in range(thread_num):
		t = threading.Thread(target = worker)
		t.daemon = True
		thread_list.append(t)
	print("Created", thread_num,"threads")
	#Create queue
	q = Queue()
	#Fill queue
	for i in range(queue_num):
		q.put(i)
	print("Queue filled with 0 -", queue_num-1)
	print("Starting threads")
	
	#Start threads
	for i in thread_list:
		i.start()

	#Block until task is done
	q.join()
