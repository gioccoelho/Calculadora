# Importando o Tkinter
import tkinter as tk

# Definindo as cores
BUTTON_GREY = '#ECEFF1'
BUTTON_ORANGE = '#FFAB40'
FONT_WHITE = '#FEFFFF'
DISPLAY_BLUE = '#38576B'

# Definindo as variáveis
all_values_math = ''
all_values_digit = '0'
last_digit = '0'
decimals = 0

# Definindo as funções


def clear_screen():
    global all_values_digit
    global all_values_math
    all_values_digit = '0'
    all_values_math = ''
    app_labeldigit.config(text=all_values_digit)
    app_labelmath.config(text=all_values_math)


def evaluate(digit):
    global all_values_digit
    global all_values_math
    global math
    global last_digit

    last_ocurrence = 0
    math = 0

    if last_digit in ('+', '-', '*', '/', '%'):
        all_values_math = all_values_math[:-1] + digit
    elif last_digit == '=':
        if digit in ('+', '-', '*', '/', '%'):
            all_values_math = str(math) + digit
        elif digit == '=':
            for char in '+-*/%':
                if all_values_math.rfind(char) > last_ocurrence:
                    last_ocurrence = all_values_math.rfind(char)
            if last_ocurrence != 0:
                all_values_math = str(math) + all_values_math[last_ocurrence:]
                math = eval(all_values_math[:-1])
    else:
        all_values_math += all_values_digit + digit
        math = eval(all_values_math[:-1])

    app_labelmath.config(text=all_values_math)
    all_values_digit = ''
    app_labeldigit.config(text=format_decimal(
        math, decimals))
    last_digit = digit

# Função que recebe o valor de input do usuário


def updatedigit(digit):
    global all_values_digit
    global decimalsisDecimal
    global last_digit
    global decimals

    isDecimal = 0

    if last_digit == '=':
        clear_screen()

    if digit in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        if len(all_values_digit) == 1 and all_values_digit == '0':
            all_values_digit = digit
        else:
            all_values_digit += digit
            if isDecimal:
                decimals += 1
        app_labeldigit.config(text=format_decimal(
            float(all_values_digit), decimals))
    else:
        if not isDecimal:
            isDecimal = True
            app_labeldigit.config(text=format_decimal(
                float(all_values_digit), decimals) + '.')
            all_values_digit += '.'

    last_digit = digit

# Função para alterar a quantidade de decimais


def format_decimal(value, decimal_places):
    format_string = "{:,." + str(decimal_places) + "f}"
    return format_string.format(value)


# Definindo os parâmentros para a janela
window = tk.Tk()
window.title('Calculator')
window.geometry('235x335')
window.config(bg='#3b3b3b')

# Criando os frames, um frame para display (onde vai ser mostrado o input) e
# um para os botões
frame_displaymath = tk.Frame(window, width=235, height=25)
frame_displaymath.grid(row=0, column=0)

frame_displaydigit = tk.Frame(window, width=235, height=50)
frame_displaydigit.grid(row=1, column=0)

frame_buttons = tk.Frame(window, width=235, height=268)
frame_buttons.grid(row=2, column=0)

# Criando os labels
app_labelmath = tk.Label(frame_displaymath,
                         width=37, height=2, padx=7, relief='flat', anchor='e',
                         justify='right', font=('Ivy 8'), bg=DISPLAY_BLUE,
                         fg=FONT_WHITE)
app_labelmath.place(x=0, y=0)

app_labeldigit = tk.Label(frame_displaydigit, text='0',
                          width=16, height=2, padx=7, relief='flat',
                          anchor='e', justify='right', font=('Ivy 18'),
                          bg=DISPLAY_BLUE, fg=FONT_WHITE)
app_labeldigit.place(x=0, y=0)

# Criando botões

# Botão C (Clear), % (Porcentagem) e / (Divisão)
button_c = tk.Button(frame_buttons, text="C", width=11, height=2,
                     bg=BUTTON_GREY, font=('Ivy 13 bold'), relief='raised',
                     overrelief='ridge', command=lambda: clear_screen())
button_c.place(x=0, y=0)

button_percentage = tk.Button(frame_buttons, text='%',
                              width=5, height=2, bg=BUTTON_GREY,
                              font=('Ivy 13 bold'), relief='raised',
                              overrelief='ridge',
                              command=lambda: evaluate('%'))
button_percentage.place(x=118, y=0)

button_d = tk.Button(frame_buttons, text='/', width=5,
                     height=2, bg=BUTTON_ORANGE, fg=FONT_WHITE,
                     font=('Ivy 13 bold'),  relief='raised',
                     overrelief='ridge', command=lambda: evaluate('/'))
button_d.place(x=177, y=0)

# Botão 7, 8, 9 e * (Multiplicação)
button_7 = tk.Button(frame_buttons, text='7', width=5, height=2,
                     bg=BUTTON_GREY, font=('Ivy 13 bold'), relief='raised',
                     overrelief='ridge', command=lambda: updatedigit('7'))
button_7.place(x=0, y=52)

button_8 = tk.Button(frame_buttons, text='8',
                     width=5, height=2, bg=BUTTON_GREY,
                     font=('Ivy 13 bold'), relief='raised',
                     overrelief='ridge', command=lambda: updatedigit('8'))
button_8.place(x=59, y=52)

button_9 = tk.Button(frame_buttons, text='9',
                     width=5, height=2, bg=BUTTON_GREY,
                     font=('Ivy 13 bold'), relief='raised',
                     overrelief='ridge', command=lambda: updatedigit('9'))
button_9.place(x=118, y=52)

button_multiply = tk.Button(frame_buttons, text='*', width=5,
                            height=2, bg=BUTTON_ORANGE, fg=FONT_WHITE,
                            font=('Ivy 13 bold'),  relief='raised',
                            overrelief='ridge', command=lambda: evaluate('*'))
button_multiply.place(x=177, y=52)

# Botão 4, 5, 6 e - (Subtração)
button_4 = tk.Button(frame_buttons, text='4',
                     width=5, height=2, bg=BUTTON_GREY,
                     font=('Ivy 13 bold'), relief='raised',
                     overrelief='ridge', command=lambda: updatedigit('4'))
button_4.place(x=0, y=104)

button_5 = tk.Button(frame_buttons, text='5',
                     width=5, height=2, bg=BUTTON_GREY,
                     font=('Ivy 13 bold'), relief='raised',
                     overrelief='ridge', command=lambda: updatedigit('5'))
button_5.place(x=59, y=104)

button_6 = tk.Button(frame_buttons, text='6',
                     width=5, height=2, bg=BUTTON_GREY,
                     font=('Ivy 13 bold'), relief='raised',
                     overrelief='ridge', command=lambda: updatedigit('6'))
button_6.place(x=118, y=104)

button_subtract = tk.Button(frame_buttons, text='-', width=5,
                            height=2, bg=BUTTON_ORANGE, fg=FONT_WHITE,
                            font=('Ivy 13 bold'),  relief='raised',
                            overrelief='ridge',
                            command=lambda: evaluate('-'))
button_subtract.place(x=177, y=104)

# Botão 1, 2, 3 e + (Soma)
button_1 = tk.Button(frame_buttons, text='1',
                     width=5, height=2, bg=BUTTON_GREY,
                     font=('Ivy 13 bold'), relief='raised',
                     overrelief='ridge', command=lambda: updatedigit('1'))
button_1.place(x=0, y=156)

button_2 = tk.Button(frame_buttons, text='2',
                     width=5, height=2, bg=BUTTON_GREY,
                     font=('Ivy 13 bold'), relief='raised',
                     overrelief='ridge', command=lambda: updatedigit('2'))
button_2.place(x=59, y=156)

button_3 = tk.Button(frame_buttons, text='3',
                     width=5, height=2, bg=BUTTON_GREY,
                     font=('Ivy 13 bold'), relief='raised',
                     overrelief='ridge', command=lambda: updatedigit('3'))
button_3.place(x=118, y=156)

button_sum = tk.Button(frame_buttons, text='+', width=5,
                       height=2, bg=BUTTON_ORANGE, fg=FONT_WHITE,
                       font=('Ivy 13 bold'),  relief='raised',
                       overrelief='ridge', command=lambda: evaluate('+'))
button_sum.place(x=177, y=156)

# Botão 0, . (Separação) e = (Igual)
button_0 = tk.Button(frame_buttons, text="0", width=11, height=2,
                     bg=BUTTON_GREY, font=('Ivy 13 bold'), relief='raised',
                     overrelief='ridge', command=lambda: updatedigit('0'))
button_0.place(x=0, y=208)

button_point = tk.Button(frame_buttons, text='.',
                         width=5, height=2, bg=BUTTON_GREY,
                         font=('Ivy 13 bold'), relief='raised',
                         overrelief='ridge', command=lambda: updatedigit('.'))
button_point.place(x=118, y=208)

button_equals = tk.Button(frame_buttons, text='=', width=5,
                          height=2, bg=BUTTON_ORANGE, fg=FONT_WHITE,
                          font=('Ivy 13 bold'),  relief='raised',
                          overrelief='ridge', command=lambda: evaluate('='))
button_equals.place(x=177, y=208)

window.mainloop()
