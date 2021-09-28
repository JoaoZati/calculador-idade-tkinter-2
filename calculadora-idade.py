import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

COR1 = '#3b3b3b'
COR2 = '#333333'


class CalculadoraIdade:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Calculadora de Idade')
        self.window.geometry('310x410')
        self.window.resizable(0, 0)

        self.frame_cima = self.frame_cima()
        self.frame_baixo = self.frame_baixo()

    def frame_cima(self):
        frame_cima = tk.Frame(self.window, width=310, height=140, pady=0, padx=0,
                              relief=tk.FLAT, bg=COR1)
        frame_cima.grid(row=0, column=0)

        label_calculadora = tk.Label(frame_cima, text="CALCULADORA", width=25, height=1, relief=tk.FLAT,
                                     padx=3, anchor='center', font=("Arial", 16), bg=COR1, fg="White")
        label_calculadora.place(x=0, y=30)

        label_de_idade = tk.Label(frame_cima, text="DE IDADE", width=12, height=1, relief=tk.FLAT,
                                  padx=3, anchor='center', font=("Arial", 35), bg=COR1, fg="orange")
        label_de_idade.place(x=0, y=70)

        return frame_cima

    def frame_baixo(self):
        frame_baixo = tk.Frame(self.window, width=310, height=270, pady=0, padx=0,
                               relief=tk.FLAT, bg=COR2)
        frame_baixo.grid(row=1, column=0)

        label_data_atual = tk.Label(frame_baixo, text="Data Atual:", height=1, relief=tk.FLAT,
                                    padx=0, pady=0, anchor='nw', font=("Arial", 11), bg=COR2, fg="White")
        label_data_atual.place(x=30, y=30)

        label_data_nascimento = tk.Label(frame_baixo, text="Data de nascimento:", height=1, relief=tk.FLAT,
                                         padx=0, pady=0, anchor='nw', font=("Arial", 11), bg=COR2, fg="White")
        label_data_nascimento.place(x=30, y=70)

        calendario_1 = DateEntry(frame_baixo, width=10, bg='darkblue', fg='White', borderwidth=2,
                                 data_patter='dd/mm/yy')
        calendario_1.place(x=180, y=30)

        calendario_2 = DateEntry(frame_baixo, width=10, bg='darkblue', fg='White', borderwidth=2,
                                 data_patter='dd/mm/yy')
        calendario_2.place(x=180, y=70)

        return frame_baixo

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    calculadora_idade = CalculadoraIdade()
    calculadora_idade.run()
