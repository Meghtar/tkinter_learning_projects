from tkinter import *
from tkinter import ttk

from converter.Converter import Converter
from converter.TemperatureConverter import TemperatureConverter
from converter.single_tab import SingleTab
from converter.distance import distance_units
from converter.weight import weight_units
from converter.volume import volume_units
from converter.temperature import temperature_units


root = Tk()

root.geometry("300x150")
root.title("Converter")

tabControl = ttk.Notebook(root)

basic_converter = Converter
temperature_converter = TemperatureConverter

distance_tab = SingleTab(tabControl, basic_converter, distance_units)
weight_tab = SingleTab(tabControl, basic_converter, weight_units)
volume_tab = SingleTab(tabControl, basic_converter, volume_units)
temperature_tab = SingleTab(tabControl, temperature_converter, temperature_units)

tabControl.add(distance_tab, text="Distance")
tabControl.add(weight_tab, text="Weight")
tabControl.add(volume_tab, text="Volume")
tabControl.add(temperature_tab, text="Temperature")

tabControl.pack(expand=1, fill="both")

root.mainloop()
