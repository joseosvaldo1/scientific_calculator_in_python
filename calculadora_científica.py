from tkinter import *
import itertools
import math

class Calculadora():
    def __init__(self, window):
        self.input_ = "0"
        self.soma = Celula()
        caixa_texto = Texto(window, self.input_)

        def novo_botao(text, row, column, function, width=5, height=1, bg="grey"):
            return Botao(window, text, row, column, function, width, height, bg)

        def input_numero(numero):
            return lambda: self.Numero(numero)

        buttons = {}

        numbers_positions = list(itertools.product([3, 4, 5], [2, 3, 4]))
        for numero in range(1, 10):
            buttons.update({str(numero): (*numbers_positions[numero - 1], input_numero(numero))})

        buttons.update({"0": (5, 5, input_numero(0))})

        buttons.update({
            "pi()": (2, 1, self.Pi),
            "x²": (2, 2, self.Pow),
            "log10()": (2, 3, self.Log10),
            "%": (2, 4, self.Percentual),
            "raiz()": (2, 5, self.Raiz_Quadrada),
            "clear": (2, 6, self.clear_, 5, 1, "orange"),
            "sen()": (3, 1, self.Seno),
            "cos()": (4, 1, self.Cosseno),
            "tg()": (5, 1, self.Tangente),
            "+": (3, 6, self.Soma),
            "-": (4, 6, self.Subtracao),
            "×": (5, 6, self.Multiplicacao),
            "÷": (6, 6, self.Divisao),
            "=": (3, 5, self.Igual),
            "^": (4,5, self.Potencia)
        })

        for button in buttons.keys():
            novo_botao(button, *buttons[button])

    def clear_(self):
        self.input_ = "0"
        caixa_texto = Texto(window, self.input_)

    def Raiz_Quadrada(self):
        temporario = math.sqrt(float(self.input_))
        self.input_ = str(temporario)
        caixa_texto = Texto(window, self.input_)

    def Seno(self):
        temporario = ((int(self.input_)) * 2 * math.pi) / (360)
        self.input_ = math.sin(temporario)
        caixa_texto = Texto(window, self.input_)

    def Cosseno(self):
        temporario = ((int(self.input_)) * 2 * math.pi) / (360)
        self.input_ = math.cos(temporario)
        caixa_texto = Texto(window, self.input_)

    def Tangente(self):
        temporario = ((int(self.input_)) * 2 * math.pi) / (360)
        self.input_ = math.tan(temporario)
        caixa_texto = Texto(window, self.input_)

    def Log10(self):
        temporario = math.log10(int(self.input_))
        self.input_ = temporario
        caixa_texto = Texto(window, self.input_)

    def Pi(self):
        self.input_ = math.pi
        caixa_texto = Texto(window, self.input_)

    def Pow(self):
        self.input_ = math.pow(float(self.input_), 2)
        caixa_texto = Texto(window, self.input_)

    def Percentual(self):
        self.input_ = (float(self.input_) / 100)
        caixa_texto = Texto(window, self.input_)

    def Igual(self):
        self.soma._numero_B = self.input_
        soma = self.soma
        operacao = {"soma": soma.soma,
                    "subtracao": soma.subtracao,
                    "multiplicacao": soma.multiplicacao,
                    "divisao": soma.divisao,
                    "potencia": soma.potencia}
        if self.soma._sinal == "divisao" and float(self.soma._numero_B) == 0:
            caixa_texto = Texto(window, "Erro: divisão por zero")
        else:
            v = operacao[self.soma._sinal]()
            caixa_texto = Texto(window, v)
            self.input_ = v

    def Soma(self):
        self.soma._numero_A = self.input_
        self.soma._sinal = "soma"
        self.input_ = "0"

    def Multiplicacao(self):
        self.soma._numero_A = self.input_
        self.soma._sinal = "multiplicacao"
        self.input_ = "0"

    def Divisao(self):
        self.soma._numero_A = self.input_
        self.soma._sinal = "divisao"
        self.input_ = "0"

    def Subtracao(self):
        self.soma._numero_A = self.input_
        self.soma._sinal = "subtracao"
        self.input_ = "0"

    def Potencia(self):
        self.soma._numero_A = self.input_
        self.soma._sinal = "potencia"
        self.input_ = "0"

    def Numero(self, numero):
        self.input_ += str(numero)
        caixa_texto = Texto(window, self.input_)


class Botao():
    def __init__(self, frame, text_botao, linha, coluna, comando, width=5, height=1, bg="grey"):
        self.button = Button(frame, text=text_botao, fg="black", bg=bg, command=comando,
                             font=("Arial", "16", "bold"))
        self.button["width"] = width
        self.button["height"] = height
        self.button.grid(row=linha, column=coluna)


class Celula():
    def __init__(self):
        self._numero_A = None
        self._numero_B = None
        self._sinal = None

    def soma(self):
        return float(self._numero_A) + float(self._numero_B)

    def subtracao(self):
        return float(self._numero_A) - float(self._numero_B)

    def multiplicacao(self):
        return float(self._numero_A) * float(self._numero_B)

    def divisao(self):
        if float(self._numero_B) != 0:
            return float(self._numero_A) / float(self._numero_B)
        else:
            return "Erro: divisão por zero"

    def potencia(self):
        return math.pow(float(self._numero_A), float(self._numero_B))


class Texto():
    def __init__(self, window, texto):
        self.texto = Label(window, text=round(float(texto), 5), font=("Arial", "24", "bold"))
        self.texto["height"] = 2
        self.texto["width"] = 2
        self.texto.grid(row=1, column=1, columnspan=6, sticky=W + E + N + S)

window = Tk()
window.title("Calculadora")
window.geometry("450x290")
m = Calculadora(window)
window.mainloop()
