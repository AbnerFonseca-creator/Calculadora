import tkinter as tk

root = tk.Tk()
root.title("Calculadora Suprema")
root.geometry("300x450")
root.configure(bg="#1e1e1e")

texto_visor = tk.StringVar(value="0")
num_anterior = 0
operacao = None
limpar_ecra = False

def clique_num(num):
    global limpar_ecra
    atual = texto_visor.get()
    if atual == "0" or limpar_ecra:
        texto_visor.set(num)
        limpar_ecra = False
    elif len(atual) < 8:
        texto_visor.set(atual + num)

def clique_op(op_escolhida):
    global num_anterior, operacao, limpar_ecra
    try:
        num_anterior = int(texto_visor.get())
        operacao = op_escolhida
        limpar_ecra = True
    except:
        texto_visor.set("ERR")

def calcular():
    global num_anterior, operacao, limpar_ecra
    if operacao is None: return
    try:
        num_atual = int(texto_visor.get())
        if operacao == "+": res = num_anterior + num_atual
        elif operacao == "-": res = num_anterior - num_atual
        elif operacao == "*": res = num_anterior * num_atual
        elif operacao == "/": res = num_anterior // num_atual if num_atual != 0 else "ERR"
        
        if res != "ERR" and len(str(res)) > 8: res = "ERR"
        texto_visor.set(str(res))
        operacao = None
        limpar_ecra = True
    except:
        texto_visor.set("ERR")

def limpar():
    texto_visor.set("0")
    global num_anterior, operacao; num_anterior = 0; operacao = None

# --- INTERFACE ---
visor = tk.Label(root, textvariable=texto_visor, font=("Arial", 32), bg="#1e1e1e", fg="white", anchor="e", padx=20)
visor.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=30)

botoes = [
    ('7', 2, 0, lambda: clique_num("7")), ('8', 2, 1, lambda: clique_num("8")), ('9', 2, 2, lambda: clique_num("9")), ('/', 1, 3, lambda: clique_op("/")),
    ('4', 3, 0, lambda: clique_num("4")), ('5', 3, 1, lambda: clique_num("5")), ('6', 3, 2, lambda: clique_num("6")), ('*', 2, 3, lambda: clique_op("*")),
    ('1', 4, 0, lambda: clique_num("1")), ('2', 4, 1, lambda: clique_num("2")), ('3', 4, 2, lambda: clique_num("3")), ('-', 3, 3, lambda: clique_op("-")),
    ('AC', 1, 0, limpar), ('0', 5, 0, lambda: clique_num("0")), ('+', 4, 3, lambda: clique_op("+")), ('=', 5, 3, calcular)
]

for (txt, lin, col, cmd) in botoes:
    tk.Button(root, text=txt, font=("Arial", 14), bg="#333", fg="white", command=cmd).grid(row=lin, column=col, sticky="nsew", padx=2, pady=2)

for i in range(4): root.grid_columnconfigure(i, weight=1)
for i in range(6): root.grid_rowconfigure(i, weight=1)

root.mainloop()