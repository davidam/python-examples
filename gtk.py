from gi.repository import Gtk

ventana = Gtk.Window(title="Ventana principal")
ventana.connect("delete-event", Gtk.main_quit)
ventana.show_all()
Gtk.main()
