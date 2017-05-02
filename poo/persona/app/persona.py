#!/usr/bin/python

class Persona(object):
    def __init__(self, miNIF, minombre, misapellidos):
        self.NIF = miNIF
        self.nombre = minombre
        self.apellidos = misapellidos

    def __str__(self):
        return self.NIF + ": " + self.apellidos + ", " + self.nombre

class Alumno(Persona):
    def __init__(self, miNIF, minombre, misapellidos, micurso):
        super(Alumno, self).__init__(miNIF, minombre, misapellidos)
        self.curso = micurso

    def __str__(self):
        return self.NIF + ": " + self.apellidos + ", " + self.nombre + " (curso :" + self.curso + ")"
