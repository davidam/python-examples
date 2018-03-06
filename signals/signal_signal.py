import signal
import os
import time

def receive_signal(signum, stack):
    print('Received: %s', signum)

signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

print('My PID is: %s', os.getpid())

while True:
    print('Waiting...')
    time.sleep(3)
