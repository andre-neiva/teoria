import random
from conversor import converter_afn_para_afd
from af import AF
from simulador import simular_afn, simular_afd
from minimizador import minimizar_afd
import tkinter as tk
from tkinter import messagebox

def criar_automato(estados, alfabeto, transicoes, estado_inicial, estados_aceitacao):
    funcao_transicao = {}
    for transicao in transicoes:
        estado, simbolo, novo_estado = transicao
        if estado not in funcao_transicao:
            funcao_transicao[estado] = {}
        if simbolo not in funcao_transicao[estado]:
            funcao_transicao[estado][simbolo] = set()
        funcao_transicao[estado][simbolo].add(novo_estado)

    automato = {
        'estados': set(estados),
        'alfabeto': set(alfabeto),
        'funcao_transicao': funcao_transicao,
        'estado_inicial': estado_inicial,
        'estados_aceitacao': set(estados_aceitacao)
    }
    tipo_automato = 'AFN'  # Supondo que estamos criando um AFN
    return automato, tipo_automato

def gerar_palavra(alfabeto, comprimento):
    return ''.join(random.choice(list(alfabeto)) for _ in range(comprimento))

def verificar_equivalencia(afn, afd, alfabeto):
    for _ in range(100):  # Testar com 100 palavras aleatórias
        palavra = gerar_palavra(alfabeto, random.randint(1, 10))
        aceita_afn = simular_afn(afn, palavra)
        aceita_afd = simular_afd(afd, palavra)
        if aceita_afn != aceita_afd:
            print(f"Falha na equivalência para a palavra: {palavra}")
            return False
    return True

def gerar_palavra(alfabeto, comprimento):
    return ''.join(random.choice(list(alfabeto)) for _ in range(comprimento))

# Função para criar o autômato com os dados fornecidos pelo usuário
def criar_automato_interface():
    estados = entrada_estados.get().strip().split()
    alfabeto = entrada_alfabeto.get().strip().split()
    transicoes = entrada_transicoes.get("1.0", tk.END).strip().split('\n')
    estado_inicial = entrada_estado_inicial.get().strip()
    estados_aceitacao = entrada_estados_aceitacao.get().strip().split()

    transicoes_formatadas = []
    for transicao in transicoes:
        partes = transicao.split()
        if len(partes) == 3:
            transicoes_formatadas.append((partes[0], partes[1], partes[2]))

    global automato, tipo_automato
    automato, tipo_automato = criar_automato(estados, alfabeto, transicoes_formatadas, estado_inicial, estados_aceitacao)
    messagebox.showinfo("Sucesso", "Autômato criado com sucesso!")

# Função para verificar a cadeia inserida pelo usuário
def verificar_cadeia():
    cadeia = entrada_cadeia.get().strip()
    if tipo_automato_var == 'AFN':
        resultado = simular_afn(automato, cadeia)
    else:
        resultado = simular_afd(automato, cadeia)

    if resultado:
        messagebox.showinfo("Resultado", "Cadeia aceita")
    else:
        messagebox.showinfo("Resultado", "Cadeia rejeitada")

# Função para inicializar a interface gráfica
def iniciar_interface():
    global entrada_estados, entrada_alfabeto, entrada_transicoes, entrada_estado_inicial, entrada_estados_aceitacao, entrada_cadeia, tipo_automato_var

    root = tk.Tk()
    root.title("Verificador de Cadeias")

    tk.Label(root, text="Estados (separados por espaço):").pack(pady=5)
    entrada_estados = tk.Entry(root, width=50)
    entrada_estados.pack(pady=5)

    tk.Label(root, text="Alfabeto (separado por espaço):").pack(pady=5)
    entrada_alfabeto = tk.Entry(root, width=50)
    entrada_alfabeto.pack(pady=5)

    tk.Label(root, text="Transições (uma por linha, formato: estado_atual símbolo estado_destino):").pack(pady=5)
    entrada_transicoes = tk.Text(root, width=50, height=10)
    entrada_transicoes.pack(pady=5)

    tk.Label(root, text="Estado Inicial:").pack(pady=5)
    entrada_estado_inicial = tk.Entry(root, width=50)
    entrada_estado_inicial.pack(pady=5)

    tk.Label(root, text="Estados de Aceitação (separados por espaço):").pack(pady=5)
    entrada_estados_aceitacao = tk.Entry(root, width=50)
    entrada_estados_aceitacao.pack(pady=5)

    tk.Label(root, text="Tipo de Autômato:").pack(pady=5)
    tipo_automato_var = tk.StringVar(value="AFN")
    tk.Radiobutton(root, text="AFN", variable=tipo_automato_var, value="AFN").pack(pady=5)
    tk.Radiobutton(root, text="AFD", variable=tipo_automato_var, value="AFD").pack(pady=5)

    tk.Button(root, text="Criar Autômato", command=criar_automato_interface).pack(pady=10)

    tk.Label(root, text="Digite a cadeia a ser verificada:").pack(pady=10)
    entrada_cadeia = tk.Entry(root, width=50)
    entrada_cadeia.pack(pady=10)

    tk.Button(root, text="Verificar", command=verificar_cadeia).pack(pady=10)

    root.mainloop()

# Exemplo de uso
if __name__ == "__main__":
    iniciar_interface()