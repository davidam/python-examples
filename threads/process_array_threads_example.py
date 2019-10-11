#process_array_threads_example.py

import threading, time
from random import randint

start_time = time.time()
items_to_process = []

# Generate an array of random integers from 0-9
for num in range(300):
	random_number = randint(0,9)
	items_to_process.append(random_number)

# Create a function to process the items in the array/dictionary
def process_function():
	while len(items_to_process) != 0:
		item = items_to_process.pop()
		print item

# Create array to hold all of the threads
threads = []

# Create 3 threads to process the data in the array
for i in range(3):

	# create thread with target call of the function created above
	t = threading.Thread(target=process_function)

	#append to array of threads
	threads.append(t)
	t.start()
	
# Wait for all of the threads to finish
for thread in threads:
	thread.join()

end_time = time.time()
duration_in_seconds = end_time - start_time
print "The script ran in " + str(duration_in_seconds) + " seconds."