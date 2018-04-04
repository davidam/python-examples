#!/usr/bin/python
# -*- coding: utf-8 -*-

class Listener:
     def __init__(self, name, subject):
         self.name = name
         subject.register(self)

     def notify(self, event):
         print(self.name + " received event " + event)


class Subject:
     def __init__(self):
         self.listeners = []
 
     def register(self, listener):
         self.listeners.append(listener)
 
     def unregister(self, listener):
         self.listeners.remove(listener)
 
     def notify_listeners(self, event):
         for listener in self.listeners:
             listener.notify(event)


subject = Subject()
listenerA = Listener("<listener A>", subject)
listenerA = Listener("<listener AA>", subject)
listenerB = Listener("<listener B>", subject)
# El objeto Subject ahora tiene dos "escuchadores" registrados
subject.notify_listeners("<events>")
