import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import builder


class Form():
    def __init__(self, name, subcategories):
        self.name = name
        self.subcategories = subcategories
        self.subcategories_checkbox = []
        self.checkbox = None

    # name - string
    def add_subcategory(self, name):
        self.subcategories.append(name)

    # ck - Gtk.CheckButton
    def add_subcategory_checkbox(self, ck):
        self.subcategories_checkbox.append(ck)
    

class MyWindow(Gtk.Window):

    def __init__(self, forms):
        super().__init__(title="Hello")
        self.forms = forms

        box_v = Gtk.Box(orientation="vertical", spacing=0, margin=20)
        self.add(box_v)
        

        grid = Gtk.Grid(row_spacing=10, column_spacing=10, margin_right=10)

        # Fac randurile din grid pentru fiecare form si subcategory
        row = 0
        for form in self.forms:
            checkbox = Gtk.CheckButton()
            label = Gtk.Label( label=form.name, halign=Gtk.Align.START )
            grid.attach(checkbox, 0, row, 1, 1)
            grid.attach(label, 1, row, 2, 1)
            form.checkbox = checkbox

            for cat in form.subcategories:
                row += 1
                checkbox = Gtk.CheckButton()
                label = Gtk.Label( label=cat, halign=Gtk.Align.START )
                grid.attach(checkbox, 1, row, 1, 1)
                grid.attach(label, 2, row, 1, 1)
                form.add_subcategory_checkbox(checkbox)

            row += 1

        box_v.pack_start(grid, True, True, 0)


        # Butonul de Generare
        self.button = Gtk.Button(label="Generate", margin=10, margin_top=40)
        self.button.connect("clicked", self.on_button_clicked)
        box_v.pack_start(self.button, True, True, 0)


    def on_button_clicked(self, widget):
        for f in self.forms:
            if f.checkbox.get_active() == True:
                builder.make_form(f)


form_A = Form("A", ["Subcategory 1", "Subcategory 2", "Subcategory 3"])
form_B = Form("B", ["Subcategory 1", "Subcategory 2", "Subcategory 3", "Subcategory 4" ])

forms = [form_A, form_B]

win = MyWindow(forms)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
