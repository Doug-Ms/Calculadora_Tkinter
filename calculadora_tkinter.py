#importação de Biblioteçãs
from tkinter import *
from tkinter import ttk

#Definição de Cores
cor1 = '#5bb8eb'
cor2 = '#000000'
cor3 = '#ffffff'
cor4 = '#ff8f0e'
cor5 = '#ababab'

#Criando a janela
janela = Tk()
janela.title('Calculadora Tkinter')
janela.geometry('235x310')
janela.config(bg=cor1)

#Criando Frames
frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor2)
frame_corpo.grid(row=1, column=0)

#variavel todos valores 
todos_valores = ''

#Criando label
valor_texto = StringVar()

#Criação de Funções
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
#Passando valores para tela
    valor_texto.set(todos_valores)

#Função Calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#Função Limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor2, fg=cor3)
app_label.place(x=0, y=0)

#Criando Botões
b_1 = Button(frame_corpo, command=limpar_tela, text='C', width=11, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_1.bind('<KeyPress-c>', lambda event: entrar_valores('C'))

b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text='%', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_2.bind('<KeyPress-percent>', lambda event: entrar_valores('%'))

b_3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text='/', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)
b_3.bind('<KeyPress-slash>', lambda event: entrar_valores('/'))

b_4 = Button(frame_corpo, command= lambda: entrar_valores('7'), text='7', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_4.bind('<KeyPress-7>', lambda event: entrar_valores('7'))


b_5 = Button(frame_corpo, command= lambda: entrar_valores('8'), text='8', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_5.bind('<KeyPress-8>', lambda event: entrar_valores('8'))

b_6 = Button(frame_corpo, command= lambda: entrar_valores('9'), text='9', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_6.bind('<KeyPress-9>', lambda event: entrar_valores('9'))

b_7 = Button(frame_corpo, command= lambda: entrar_valores('*'), text='*', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)
b_7.bind('<KeyPress-asterisk>', lambda event: entrar_valores('*'))

b_8 = Button(frame_corpo, command= lambda: entrar_valores('4'), text='4', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_8.bind('<KeyPress-4>', lambda event: entrar_valores('4'))


b_9 = Button(frame_corpo, command= lambda: entrar_valores('5'), text='5', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_9.bind('<KeyPress-5>', lambda event: entrar_valores('5'))

b_10 = Button(frame_corpo, command= lambda: entrar_valores('6'), text='6', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_10.bind('<KeyPress-6>', lambda event: entrar_valores('6'))

b_11 = Button(frame_corpo, command= lambda: entrar_valores('-'), text='-', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)
b_11.bind('<KeyPress-minus>', lambda event: entrar_valores('-'))

b_12 = Button(frame_corpo, command= lambda: entrar_valores('1'), text='1', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_12.bind('<KeyPress-1>', lambda event: entrar_valores('1'))

b_13 = Button(frame_corpo, command= lambda: entrar_valores('2'), text='2', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_13.bind('<KeyPress-2>', lambda event: entrar_valores('2'))

b_14 = Button(frame_corpo, command= lambda: entrar_valores('3'), text='3', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_14.bind('<KeyPress-3>', lambda event: entrar_valores('3'))

b_15 = Button(frame_corpo, command= lambda: entrar_valores('+'), text='+', width=5, height=2, bg=cor1, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)
b_15.bind('<KeyPress-plus>', lambda event: entrar_valores('+'))

b_16 = Button(frame_corpo, command= lambda: entrar_valores('0'), text='0', width=11, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_16.bind('<KeyPress-0>', lambda event: entrar_valores('0'))

b_17 = Button(frame_corpo, command= lambda: entrar_valores('.'), text='.', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_17.bind('<KeyPress-period>', lambda event: entrar_valores('.'))

b_18 = Button(frame_corpo, command= calcular, text='=', width=5, height=2, bg=cor4, fg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)
b_18.bind('<KeyPress-Return>', lambda event: entrar_valores('='))

# Função para capturar os eventos de teclado
def capturar_teclado(event):
    tecla = event.char
    if tecla.isdigit() or tecla in ['+', '-', '*', '/', '.']:
        entrar_valores(tecla)
    elif event.keysym == 'Delete':
        limpar_tela()
    elif event.keysym == 'Return':
        calcular()
    elif event.keysym == 'comma':
        entrar_valores('.')

# Registrar eventos de teclado
janela.bind('<Key>', capturar_teclado)

janela.mainloop()
#By Doug-Ms 👾😵‍💫