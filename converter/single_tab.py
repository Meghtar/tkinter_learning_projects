from tkinter import *
from tkinter import ttk

from converter.Converter import Converter


class SingleTab(Frame):
    def __init__(self, root, current_converter, values_map={}):
        Frame.__init__(self, root)
        self.values_map = values_map
        self.converter = current_converter

        self.input_frame = Frame(self)
        self.input_frame.pack()

        self.value_label = Label(self.input_frame, text="Value to convert")
        self.value_label.grid(row=0, column=0)

        self.initial_value = Entry(self.input_frame, width=20)
        self.initial_value.grid(row=1, column=0, padx=10)

        self.initial_unit_lbl = Label(self.input_frame, text="Initial unit")
        self.initial_unit_lbl.grid(row=0, column=1, padx=15)

        self.initial_unit = StringVar()

        self.value_label = Label(self.input_frame, text="Result value")
        self.value_label.grid(row=2, column=0)

        self.result_value = Entry(self.input_frame, width=20)
        self.result_value.grid(row=3, column=0, padx=10)

        self.initial_unit_choice = ttk.Combobox(self.input_frame, width=16, textvariable=self.initial_unit)
        self.initial_unit_choice['values'] = list(values_map.keys())
        self.initial_unit_choice.grid(row=1, column=1, padx=5)

        self.target_unit_lbl = Label(self.input_frame, text="Target unit")
        self.target_unit_lbl.grid(row=2, column=1, padx=15)

        self.target_unit = StringVar()

        self.target_unit_choice = ttk.Combobox(self.input_frame, width=16, textvariable=self.target_unit)
        self.target_unit_choice['values'] = list(values_map.keys())
        self.target_unit_choice.grid(row=3, column=1, padx=5)

        self.convert_button = ttk.Button(self, text="Convert", command=self.convert)
        self.convert_button.pack(pady=5)

    def convert(self):
        result = self.converter.convert(float(self.initial_value.get()), self.initial_unit.get(),
                                          self.target_unit.get(), self.values_map)
        self.result_value.delete('0', END)
        self.result_value.insert(INSERT, str(result))
