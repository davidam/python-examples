#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,
import socket
import abc
from threading import *


def hostname():
    return socket.gethostname()


# Server Program

class SocketServer(object):
    def __init__(self, host=hostname(), port=5000):
        self.host, self.port = host, port
        self.connection = self.remote_host = self.remote_port = None
        self.run = False
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as exp:
            print('Failed to create server TCP socket object!!', exp)
        try:
            self.socket.bind((self.host, self.port))
        except socket.error as exp:
            print('Cannot bind server to ' + str(self.host) + ' on port ' + str(self.port), exp)

    def start(self):
        self.run = True
        self.socket.listen(0)
        while self.run:
            self.connection, self.remote_host = self.socket.accept()
            Thread(target=self.handle_connection, args=(self.connection,)).start()

    def stop(self):
        self.run = False

    @abc.abstractmethod
    def handle_connection(self, connection):
        pass


# Client Program

class SocketClient:
    def __init__(self):
        self.remote_host = self.remote_port = None
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as exp:
            print('Failed to create client TCP socket object!!', exp)

    def connect(self, remote_host=hostname(), remote_port=5000):
        self.remote_host, self.remote_port = remote_host, remote_port
        self.socket.connect((self.remote_host, self.remote_port))

    def send(self, data):
        self.socket.send(data)

    def receive(self, size=1024):
        return self.socket.recv(size)

    def close(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()


# Datagram Server Program

class DatagramServerSocket(object):
    def __init__(self, host=hostname(), port=5000):
        self.host, self.port = host, port
        self.run = False
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error as exp:
            print('Failed to create server UDP socket object!!', exp)
        try:
            self.socket.bind((self.host, self.port))
        except socket.error as exp:
            print('Cannot bind server to ' + str(self.host) + ' on port ' + str(self.port), exp)

    def start(self):
        self.run = True
        while self.run:
            d = self.receive()
            Thread(target=self.handle_data, args=(d,)).start()

    def stop(self):
        self.run = False

    @abc.abstractmethod
    def handle_data(self, data):
        pass

    def send(self, data, remote_address):
        self.socket.sendto(data, remote_address)

    def receive(self, size=1024):
        return self.socket.recvfrom(size)

    def close(self):
        self.socket.close()


# Datagram Client Program

class DatagramSocketClient:
    def __init__(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error as exp:
            print('Failed to create client UDP socket object!!', exp)

    def send(self, remote_host=hostname(), remote_port=5000, data=""):
        self.socket.sendto(data, (remote_host, remote_port))

    def receive(self, size=1024):
        return self.socket.recvfrom(size)[0]

    def close(self):
        self.socket.close()
