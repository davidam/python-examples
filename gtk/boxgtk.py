from gi.repository import Gtk

def saludo(miboton):
    if miboton.get_label() == "Hola":
        print("Hola, buenos dias")
    else:
        print("Ciao, buenas noches")

ventana = Gtk.Window(title="Box")
ventana.connect("delete-event", Gtk.main_quit)
caja = Gtk.Box(spacing=10)
ventana.add(caja)
boton1 = Gtk.Button(label="Hola")
boton1.connect("clicked", saludo)
caja.pack_start(boton1, True, True, 0)

boton2 = Gtk.Button(label="Ciao")
boton2.connect("clicked", saludo)
caja.pack_start(boton2, True, True, 0)
ventana.show_all()
Gtk.main()
