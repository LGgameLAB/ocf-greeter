import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GdkPixbuf

class Greeter(Gtk.Window):
    '''
        The greeter/welcome page application
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_components()


    def load_components(self):
        BTN_WIDTH = 30 # Number of characters wide
        WADDLES = "assets/penguin.png"


        self.set_title("Welcome")
        self.set_default_size(300, 200)

        btn = Gtk.Button(label="Hello, World!")
        # self.set_child(btn)


        # Create Boxes
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.btn_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.btn_box.set_margin_bottom(15)
        self.btn_box.set_margin_top(15)
        self.btn_box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.column1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.column2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Images
        penguin_buffer = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                filename=WADDLES,
                width=1000,
                height=1000,
                preserve_aspect_ratio=True
        )
        waddles = Gtk.Image()
        waddles.set_from_pixbuf(penguin_buffer) #

        # Labels
        self.text1 = Gtk.Label(
            label="\nWelcome to the OCF!\n")

        # Layout
        self.set_child(self.box)
        self.box.append(self.text1)
        self.box.append(waddles)
        self.box.append(self.btn_box)
        self.box.append(self.btn_box2)
        self.btn_box.append(self.column1)
        self.btn_box.append(self.column2)
        
        # Buttons
        # Send you to desktop customization
        self.btn1 = Gtk.LinkButton(
            uri="https://bestdocs.ocf.io/user-docs/desktop-customization/",
            label="🖌️ Customize Desktop".center(BTN_WIDTH))
        self.column1.append(self.btn1)

        # Link to Discord
        self.btn2 = Gtk.LinkButton(
            uri="https://www.ocf.berkeley.edu/docs/contact/",
            label="💬 Contact Us".center(BTN_WIDTH))
        self.column1.append(self.btn2)
       
        # Link to Berkeley News
        self.btn3 = Gtk.LinkButton(
            uri="https://news.berkeley.edu/",
            label="📰 Berkeley News".center(BTN_WIDTH))
        self.column2.append(self.btn3)
    
        # Link to Berkeley News
        self.btn4 = Gtk.LinkButton(
            uri="https://www.ocf.berkeley.edu/docs/services/lab/printing/",
            label="📰 Printing Policy".center(BTN_WIDTH))
        self.column2.append(self.btn4)

        # Close window
        self.close_btn = Gtk.Button(label="close".center(9) )
        self.close_btn.connect('clicked', lambda x: self.close())
        self.btn_box2.set_halign(Gtk.Align.CENTER)
        self.btn_box2.append(self.close_btn)
