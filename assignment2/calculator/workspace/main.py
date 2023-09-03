import tkinter as tk
from calculator import Calculator

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self)
        self.display.grid(row=0, column=0, columnspan=4)

        self.buttons = []
        for i in range(9):
            self.buttons.append(tk.Button(self, text=str(i+1), command=lambda i=i: self.update_display(i+1)))
            self.buttons[i].grid(row=(i//3)+1, column=i%3)

        self.buttons.append(tk.Button(self, text='0', command=lambda: self.update_display(0)))
        self.buttons[9].grid(row=4, column=1)

        self.buttons.append(tk.Button(self, text='+', command=lambda: self.update_display('+')))
        self.buttons[10].grid(row=1, column=3)

        self.buttons.append(tk.Button(self, text='-', command=lambda: self.update_display('-')))
        self.buttons[11].grid(row=2, column=3)

        self.buttons.append(tk.Button(self, text='*', command=lambda: self.update_display('*')))
        self.buttons[12].grid(row=3, column=3)

        self.buttons.append(tk.Button(self, text='/', command=lambda: self.update_display('/')))
        self.buttons[13].grid(row=4, column=3)

        self.buttons.append(tk.Button(self, text='C', command=self.clear_display))
        self.buttons[14].grid(row=4, column=0)

        self.buttons.append(tk.Button(self, text='=', command=self.calculate))
        self.buttons[15].grid(row=4, column=2)

    def update_display(self, value):
        self.display.insert(tk.END, str(value))

    def clear_display(self):
        self.display.delete(0, tk.END)

    def calculate(self):
        expression = self.display.get()
        self.clear_display()
        try:
            self.display.insert(tk.END, str(eval(expression)))
        except Exception:
            self.display.insert(tk.END, 'Error')

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
