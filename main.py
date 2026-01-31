import gi, sys
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from greeter import Greeter



def main(app):
    greeter_window = Greeter(application=app)
    greeter_window.present()


if __name__ == "__main__":
    app = Gtk.Application(application_id='org.gtk.Example')
    app.connect('activate', main)
    app.run(sys.argv)
