import asyncio
from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk

INTERVAL = 0.05

class Window:
    def __init__(self):
        self.window = ThemedTk(theme="arc")
        self.window.title('PhaseSpace Mocap')
        self.window.geometry('360x480')
        self.counter = 0

        self.btn = Button(self.window, width=10, text="test", command=self.increase)
        self.btn.grid(row=1, column=1)
        self.str_var = StringVar()
        self.label = Label(textvariable=self.str_var, justify=LEFT)
        self.label.grid(row=1, column=2)

    def increase(self):
        self.counter += 1
        self.str_var.set(self.counter)


    async def run(self):
        try:
            while True:
                self.window.update()
                await asyncio.sleep(INTERVAL)
        except TclError as e:
            if "application has been destroyed" not in e.args[0]:
                raise

    def get_task(self):
        return asyncio.create_task(self.run())
