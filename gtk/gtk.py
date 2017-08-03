from gi.repository import Gtk

def boton_pulsado(elboton):
    print("El boton pone " + elboton.get_label())
    print("Has hecho clic")

ventana = Gtk.Window(title="Ventana principal")
ventana.connect("delete-event", Gtk.main_quit)
ventana.set_title("Nuevo titulo")
boton = Gtk.Button(label="Haz clic")
boton.connect("clicked", boton_pulsado)
ventana.add(boton)
ventana.show_all()
Gtk.main()
