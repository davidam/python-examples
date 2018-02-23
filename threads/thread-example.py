import threading

def fun1():
    print(1)

def fun2():
    print(2)
    
t = threading.Thread(target = fun1)
t.start()

t = threading.Thread(target = fun2)
t.start()

