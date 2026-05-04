from tkinter import *

class Calculator:
    def __init__(self, master):
        master.title("Calculator")

        self.equation = StringVar()
        self.entry_value = ''

        Entry(master, textvariable=self.equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4).grid(row=0, column=0, columnspan=4)

        buttons = [
            ('1',1,0), ('2',1,1), ('3',1,2), ('+',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
            ('7',3,0), ('8',3,1), ('9',3,2), ('*',3,3),
            ('0',4,0), ('C',4,1), ('=',4,2), ('/',4,3),
        ]

        for (text, row, col) in buttons:
            if text == '=':
                Button(master, text=text, padx=20, pady=20, command=self.solve).grid(row=row, column=col)
            elif text == 'C':
                Button(master, text=text, padx=20, pady=20, command=self.clear).grid(row=row, column=col)
            else:
                Button(master, text=text, padx=20, pady=20,
                       command=lambda t=text: self.show(t)).grid(row=row, column=col)

    def show(self, value):
        self.entry_value += value
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set('')

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()