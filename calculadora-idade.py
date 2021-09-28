import tkinter as tk
from tkinter import ttk

COR1 = '#3b3b3b'
COR2 = '#333333'


class CalculadoraIdade:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Calculadora Idade')
        self.window.geometry('310x410')

        self.frame_cima = self.frame_cima()
        self.frame_baixo = self.frame_baixo()

    def frame_cima(self):
        frame_cima = tk.Frame(self.window, width=310, height=140, pady=0, padx=0,
                              relief=tk.FLAT, bg=COR1)
        frame_cima.grid(row=0, column=0)

        return frame_cima

    def frame_baixo(self):
        frame_baixo = tk.Frame(self.window, width=310, height=300, pady=0, padx=0,
                               relief=tk.FLAT, bg=COR2)
        frame_baixo.grid(row=1, column=0)

        return frame_baixo

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    calculadora_idade = CalculadoraIdade()
    calculadora_idade.run()
