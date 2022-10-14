import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from openpyxl import Workbook
from openpyxl.chart import ( LineChart, Reference )
from openpyxl.chart.axis import DateAxis
import random

def make_xsls():
    values_count = 70

    wb = Workbook()
    worksheet = wb.create_sheet("Hello", 0)


    worksheet['A1'] = "Date"
    worksheet['B1'] = "Value"

    for i in range(values_count):
        worksheet.cell(row=2+i, column=1, value=i)

    for i in range(values_count):
        worksheet.cell(row=2+i, column=2, value=random.randrange(10,100))

    chart = LineChart()
    chart.title = "Values over time"
    chart.style = 1
    chart.y_axis.title = "Value"
    chart.x_axis.title = "Day No"
    chart.width = 50
    chart.height= 10
    data = Reference(worksheet, min_col=2, min_row=2, max_col=2, max_row=1+values_count)
    chart.add_data(data, titles_from_data=False)
    worksheet.add_chart(chart, "D3")

    wb.save('form1.xlsx')

# Sa fac ca aici:
# https://python-gtk-3-tutorial.readthedocs.io/en/latest/layout.html#id3

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello")

        box_v = Gtk.Box(orientation="vertical", spacing=0)
        self.add(box_v)
        
        box = Gtk.Box(spacing=10, margin=10)
        box_v.pack_start(box, True, True, 10)

        label = Gtk.Label( label="Input audio file", halign=Gtk.Align.START )
        box.pack_start(label, True, True, 10)

        self.audio_file_entry = Gtk.Entry(width_chars=30)
        box.pack_start(self.audio_file_entry, True, True, 10)

        # Rand 2 - Category 1
        boxh_cat_1 = Gtk.Box(spacing=10, margin=10)
        box_v.pack_start(boxh_cat_1, True, True, 0)
        # checkbox si label
        ck_cat_1 = Gtk.CheckButton()
        boxh_cat_1.pack_start(ck_cat_1, True, True, 10)
        label_cat_1 = Gtk.Label( label="Category 1", halign=Gtk.Align.START )
        boxh_cat_1.pack_start(label_cat_1, True, True, 0)


        # Rand 3 - Sub-Category 1-1
        boxh_subcat_1_1 = Gtk.Box(spacing=10, margin=0, margin_left=40)
        box_v.pack_start(boxh_subcat_1_1, True, True, 0)
        # checkbox si label
        ck_subcat_1_1 = Gtk.CheckButton()
        boxh_subcat_1_1.pack_start(ck_subcat_1_1, True, True, 10)
        label_subcat_1 = Gtk.Label( label="Subcategory 1-1", halign=Gtk.Align.START )
        boxh_subcat_1_1.pack_start(label_subcat_1, True, True, 0)


        self.button = Gtk.Button(label="Generate", margin=20, margin_top=40)
        self.button.connect("clicked", self.on_button_clicked)
        box_v.pack_start(self.button, True, True, 0)

        self.audio_file_entry.set_text("some-audio.wav")

    def on_button_clicked(self, widget):
        print("to do")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
