#impotar a biblioteca tkinter para criar interfaces graficas
from tkinter import * #o * importa tudo da biblioteca
from tkinter import ttk

#4 etapa definir cores que vou usar
cor1 = "#6b4b70" #roxo escuro
cor2 = "#b8326a" #rosa escuro fosco
cor3 = "#363391" #azul fosco
cor4 = "#e6e7f0" #cinza claro
cor5 = "#070808" #preto


#criar a janela
janela = Tk()

#nomear a janela
janela.title("Calculadora")
#2 etepa para configurar tamananho da janela, larg x alt
janela.geometry("235x310")
janela.config(bg=cor1) # bg é background
#3 etapa, dividir a nossa janela para a parte que sera o "visor/display" e a parte dos botoes, serão dois frames
frame_tela = Frame(janela, width=235, height=50, bg=cor2) #width é a largura e height é altura, poderia colocar o visor com background diferente
frame_tela.grid(row=0, column=0)#como é uma grade usamos o grid, row 0 seria a primeira linha e colum 0 a primiera coluna


frame_corpo = Frame(janela, width=235, height=268)  #onde coloco os botoes
frame_corpo.grid(row=1, column=0)


#nessa etapa vai mostrar na tela  tudo q clicarmos, repetidamente
todos_valores = ''#todo valor sera reusado, concatena tudo q eu colocar nas expressoes abaixo sera tudo guardado aqui

valor_texto = StringVar() #vai receber valor para enviar para o texto do visor

#colocando as funçoes
def entrar_valores(event):#def para definir funçoes pode conter qualquer nome, só quer dizer q vai executar uma função
    global todos_valores
    todos_valores = todos_valores + str(event) #onde recebe todos os valores
    valor_texto.set(todos_valores) #passando valor para tela da calculadora

#função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))


#função limpar tela
def limpar_tela():
    global todos_valores#assim, qualquer modificação q eu fizer aqui vai funcionar nas outras funçoes
    todos_valores = ''
    valor_texto.set("")

#criando label
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '), bg=cor2, fg=cor4) #flat pra ficar tudo maiusculo e anchor para mostrar o resultado no cantinho e padx para margem e justify quase o mesmo q anchor
app_label.place(x=0, y=0)

#criando botoes
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)#fonte e puxa o botão mais para frente e over para efeito do mouse em cima
b_1.place(x=0, y=0) #x horizontal e y vertical
b_2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #fg é a cor da fonte
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command = lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, command = lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, command = lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #fg é a cor da fonte
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo, command = lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command = lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, command = lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, command = lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #fg é a cor da fonte
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, command = lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command = lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, command = lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, command = lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #fg é a cor da fonte
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, command = lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)#fonte e puxa o botão mais para frente e over para efeito do mouse em cima
b_16.place(x=0, y=208) #x horizontal e y vertical
b_17 = Button(frame_corpo, command = lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=208)
b_18 = Button(frame_corpo, command = calcular, text="=", width=5, height=2, bg=cor3, fg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #fg é a cor da fonte
b_18.place(x=177, y=208)




#codigo para executar a janela
janela.mainloop()