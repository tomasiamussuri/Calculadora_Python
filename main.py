# Import tkinter / Importar tkinter
from tkinter import *
from tkinter import ttk


# Colors / Cores
color1 = "#000000" #black/preto
color2 = "#FFFFFF" #white/branco
color3 = "#2E2E2E" #grey dark/cinza escuro
color4 = "#BDBDBD" #grey/cinza
color5 = "#FF8000" #orange/laranja
color6 = "#5858FA" #blue/azul


# Template / Modelo
window =Tk()
window.title("calculator")
window.geometry("235x310")
window.config(bg=color1)


# Creating Frames / Criando Quadros
frame_display = Frame(window, width=235, height=50, bg=color1)
frame_display.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=260, bg=color1)
frame_body.grid(row=1, column=0)


# Variables / Variaveis
all_values = ''
value_text = StringVar()


# Creating Functions / Criando Funções
def entry_value(event):
    global all_values

    all_values = all_values + str(event)
    
    # Passando resultado para Label
    value_text.set(all_values)

def calculate():
    result = eval(all_values)
    
    value_text.set(str(result))

def clear_display():
    global all_values
    all_values =''
    value_text.set("")


# Creating Label / Criando Etiqueta
app_label = Label(frame_display, textvariable=value_text, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=color3, fg=color2)
app_label.place(x=0, y=0)


# Creating Buttons / Criando Botões
button_1 = Button(frame_body, command=clear_display, text="C", width=12, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_1.place(x=0, y=0)

button_2 = Button(frame_body, command = lambda: entry_value('%'), text="%", width=6, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_2.place(x=118, y=0)

button_3 = Button(frame_body, command = lambda: entry_value('/'), text="/", width=6, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_3.place(x=177, y=0)

button_4 = Button(frame_body, command = lambda: entry_value('7'), text="7", width=6, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_4.place(x=0, y=52)

button_5 = Button(frame_body, command = lambda: entry_value('8'), text="8", width=6, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_5.place(x=59, y=52)

button_6 = Button(frame_body, command = lambda: entry_value('9'), text="9", width=6, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_6.place(x=118, y=52)

button_7 = Button(frame_body, command = lambda: entry_value('*'), text="*", width=6, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_7.place(x=177, y=52)

button_8 = Button(frame_body, command = lambda: entry_value('4'), text="4", width=6, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_8.place(x=0, y=104)

button_9 = Button(frame_body, command = lambda: entry_value('5'), text="5", width=6, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_9.place(x=59, y=104)

button_10 = Button(frame_body, command = lambda: entry_value('6'), text="6", width=6, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_10.place(x=118, y=104)

button_11 = Button(frame_body, command = lambda: entry_value('-'), text="-", width=6, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_11.place(x=177, y=104)

button_12 = Button(frame_body, command = lambda: entry_value('1'), text="1", width=6, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_12.place(x=0, y=156)

button_13 = Button(frame_body, command = lambda: entry_value('2'), text="2", width=6, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_13.place(x=59, y=156)

button_14 = Button(frame_body, command = lambda: entry_value('3'), text="3", width=6, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_14.place(x=118, y=156)

button_15 = Button(frame_body, command = lambda: entry_value('+'), text="+", width=6, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_15.place(x=177, y=156)

button_16 = Button(frame_body, command = lambda: entry_value('0'), text="0", width=12, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_16.place(x=0, y=208)

button_17 = Button(frame_body, command = lambda: entry_value('.'), text=".", width=6, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_17.place(x=118, y=208)

button_18 = Button(frame_body, command = calculate, text="=", width=6, height=2, bg=color5, fg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_18.place(x=177, y=208)


# Application / Aplicação
window.mainloop()

