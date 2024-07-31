import random
from conversor import converter_afn_para_afd
from simulador import simular_afn, simular_afd
from minimizador import minimizar_afd
from af import AF
import tkinter as tk
from tkinter import messagebox

def formatar_automato(automato):
    result = []
    result.append(f"Estados: {automato.estados}")
    result.append(f"Alfabeto: {automato.alfabeto}")
    result.append("Função de Transição:")
    for estado, transicoes in automato.funcao_transicao.items():
        if isinstance(transicoes, dict):
            for simbolo, destinos in transicoes.items():
                result.append(f"  {estado} --{simbolo}--> {destinos}")
        else:
            result.append(f"  {estado} --{transicoes}")
    result.append(f"Estado Inicial: {automato.estado_inicial}")
    result.append(f"Estados de Aceitação: {automato.estados_aceitacao}")
    return "\n".join(result)

automato = None

def criar_automato(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
    funcao_transicao = {}
    for transicao in transicoes:
        estado, simbolo, novo_estado = transicao
        if estado not in funcao_transicao:
            funcao_transicao[estado] = {}
        if simbolo not in funcao_transicao[estado]:
            funcao_transicao[estado][simbolo] = set()
        funcao_transicao[estado][simbolo].add(novo_estado)

    automato = AF(
        estados=set(estados),
        alfabeto=set(alfabeto),
        funcao_transicao=funcao_transicao,
        estado_inicial=estado_inicial,
        estados_aceitacao=set(estados_aceitacao)
    )
    tipo_automato = tipo_automato_var.get()
    return automato, tipo_automato

def criar_automato_interface():
    global automato
    estados = entrada_estados.get().strip().split()
    alfabeto = entrada_alfabeto.get().strip().split()
    transicoes = entrada_transicoes.get("1.0", tk.END).strip().split('\n')
    estado_inicial = entrada_estado_inicial.get().strip()
    estados_aceitacao = entrada_estados_aceitacao.get().strip().split()
    tipo_automato = tipo_automato_var.get()

    if not estados:
        messagebox.showerror("Erro", "Por favor, insira os estados.")
        return
    if not alfabeto:
        messagebox.showerror("Erro", "Por favor, insira o alfabeto.")
        return
    if not transicoes or transicoes == ['']:
        messagebox.showerror("Erro", "Por favor, insira as transições.")
        return
    if not estado_inicial:
        messagebox.showerror("Erro", "Por favor, insira o estado inicial.")
        return
    if not estados_aceitacao:
        messagebox.showerror("Erro", "Por favor, insira os estados de aceitação.")

    transicoes_formatadas = []
    for transicao in transicoes:
        partes = transicao.split()
        if len(partes) == 3:
            transicoes_formatadas.append((partes[0], partes[1], partes[2]))
        else:
            messagebox.showerror("Erro", f"Transição inválida: {transicao}")
            return

    automato, tipo = criar_automato(estados, alfabeto, transicoes_formatadas, estado_inicial, estados_aceitacao)
    messagebox.showinfo("Sucesso", f"Automato {tipo_automato} criado com sucesso!")

def verificar_cadeia():
    global automato
    cadeia = entrada_cadeia.get().strip()
    if not automato:
        messagebox.showerror("Erro", "Automato não definido")
        return
    
    tipo_automato = tipo_automato_var.get()
    
    if tipo_automato == "AFD":
        resultado = simular_afd(automato, cadeia)
    else:  # Supondo que o outro tipo é AFN
        resultado = simular_afn(automato, cadeia)
    
    messagebox.showinfo("Resultado", f"A cadeia foi {'aceita' if resultado else 'rejeitada'} pelo autômato")

def minimizar_automato():
    global automato
    if not automato:
        messagebox.showerror("Erro", "Automato não definido")
        return
    
    tipo_automato = tipo_automato_var.get()
    
    if tipo_automato == "AFD":
        print("Minimizando o automato AFD:")
        print(formatar_automato(automato))
        automato_minimizado = minimizar_afd(automato)
        print("Automato minimizado:")
        print(formatar_automato(automato_minimizado))
        messagebox.showinfo("Sucesso", "Automato minimizado com sucesso!")
    else:
        messagebox.showerror("Erro", "A minimização só é suportada para AFDs")

def converter_afn_para_afd_interface():
    global automato
    if not automato:
        messagebox.showerror("Erro", "Automato não definido")
        return

    print("Convertendo AFN para AFD:")
    print(formatar_automato(automato))
    automato = converter_afn_para_afd(automato)
    print("Automato convertido para AFD:")
    print(formatar_automato(automato))
    messagebox.showinfo("Sucesso", "Automato convertido para AFD com sucesso!")

# Criação da interface gráfica com tkinter
janela = tk.Tk()
janela.title("Verificador de Cadeias")

# Componentes da interface
tk.Label(janela, text="Estados (separados por espaço):").pack()
entrada_estados = tk.Entry(janela)
entrada_estados.pack()

tk.Label(janela, text="Alfabeto (separado por espaço):").pack()
entrada_alfabeto = tk.Entry(janela)
entrada_alfabeto.pack()

tk.Label(janela, text="Transições (uma por linha, formato: estado_atual símbolo estado_destino):").pack()
entrada_transicoes = tk.Text(janela, height=10)
entrada_transicoes.pack()

tk.Label(janela, text="Estado Inicial:").pack()
entrada_estado_inicial = tk.Entry(janela)
entrada_estado_inicial.pack()

tk.Label(janela, text="Estados de Aceitação (separados por espaço):").pack()
entrada_estados_aceitacao = tk.Entry(janela)
entrada_estados_aceitacao.pack()

tk.Label(janela, text="Tipo de Autômato:").pack()
tipo_automato_var = tk.StringVar(value="AFN")
tk.Radiobutton(janela, text="AFN", variable=tipo_automato_var, value="AFN").pack()
tk.Radiobutton(janela, text="AFD", variable=tipo_automato_var, value="AFD").pack()

tk.Button(janela, text="Criar Autômato", command=criar_automato_interface).pack()

tk.Label(janela, text="Digite a cadeia a ser verificada:").pack()
entrada_cadeia = tk.Entry(janela)
entrada_cadeia.pack()

tk.Button(janela, text="Verificar", command=verificar_cadeia).pack()
tk.Button(janela, text="Converter AFN para AFD", command=converter_afn_para_afd_interface).pack()
tk.Button(janela, text="Minimizar AFD", command=minimizar_automato).pack()

janela.mainloop()

