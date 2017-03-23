from gi.repository import Gtk

ventana = Gtk.Window(title="Table")
ventana.connect("delete-event", Gtk.main_quit)

tabla = Gtk.Table(3, 3)
ventana.add(tabla)
boton1 = Gtk.Button(label="Boton 1")
boton2 = Gtk.Button(label="Boton 2")
boton3 = Gtk.Button(label="Boton 3")
boton4 = Gtk.Button(label="Boton 4")
boton5 = Gtk.Button(label="Boton 5")
boton6 = Gtk.Button(label="Boton 6")

tabla.attach(boton1, 0, 1, 0, 1)
tabla.attach(boton2, 1, 3, 0, 1)
tabla.attach(boton3, 0, 1, 1, 3)
tabla.attach(boton4, 1, 3, 1, 2)
tabla.attach(boton5, 1, 2, 2, 3)
tabla.attach(boton6, 2, 3, 2, 3)

ventana.show_all()
Gtk.main()
