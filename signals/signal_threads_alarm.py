import signal
import time
import threading

def signal_handler(num, stack):
    print(str(time.ctime()) + ' Alarm in ' + str(threading.currentThread()))

signal.signal(signal.SIGALRM, signal_handler)

def use_alarm():
    print(str(time.ctime()) + ' Setting alarm in ' + str(threading.currentThread()))
    signal.alarm(1)
    print(str(time.ctime()) + ' Sleeping in ' + str(threading.currentThread()))
    time.sleep(3)
    print(str(time.ctime()) + ' Done with sleep')

# Start a thread that will not receive the signal
alarm_thread = threading.Thread(target=use_alarm, name='alarm_thread')
alarm_thread.start()
time.sleep(0.1)

# Wait for the thread to see the signal (not going to happen!)
print(str(time.ctime()) + ' Waiting for ' + str(alarm_thread))
alarm_thread.join()

print(str(time.ctime()) + ' Exiting normally')
