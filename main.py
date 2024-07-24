import random
from conversor import converter_afn_para_afd
from af import AF
from simulador import simular_afn, simular_afd
from minimizador import minimizar_afd

def criar_automato():
    tipo_automato = input("Digite o tipo de autômato (AFD/AFN): ").strip().upper()
    estados = set(input("Digite os estados (separados por espaço): ").strip().split())
    alfabeto = set(input("Digite o alfabeto (separados por espaço): ").strip().split())
    funcao_transicao = {}
    print("Digite a função de transição no formato 'estado símbolo novo_estado' (uma por linha, termine com uma linha vazia):")
    while True:
        transicao = input().strip()
        if not transicao:
            break
        estado, simbolo, novo_estado = transicao.split()
        if estado not in funcao_transicao:
            funcao_transicao[estado] = {}
        if simbolo not in funcao_transicao[estado]:
            funcao_transicao[estado][simbolo] = set()
        funcao_transicao[estado][simbolo].add(novo_estado)
    estado_inicial = input("Digite o estado inicial: ").strip()
    estados_aceitacao = set(input("Digite os estados de aceitação (separados por espaço): ").strip().split())

    return AF(estados, alfabeto, funcao_transicao, estado_inicial, estados_aceitacao), tipo_automato

def gerar_palavra(alfabeto, comprimento):
    return ''.join(random.choice(list(alfabeto)) for _ in range(comprimento))

def verificar_equivalencia(afn, afd, alfabeto, num_testes=100):
    for _ in range(num_testes):
        palavra = gerar_palavra(alfabeto, random.randint(1, 10))
        aceita_afn = simular_afn(afn, palavra)
        aceita_afd = simular_afd(afd, palavra)
        if aceita_afn != aceita_afd:
            print(f"Falha na equivalência para a palavra: {palavra}")
            return False
    return True


# Exemplo de uso
if __name__ == "__main__":
    automato, tipo_automato = criar_automato()
    if tipo_automato == 'AFN':
        afn = automato
        afd = converter_afn_para_afd(automato)
        print("AFN convertido para AFD com sucesso.")
        if verificar_equivalencia(afn, afd, afn.alfabeto):
            print("AFN e AFD são equivalentes.")
        else:
            print("AFN e AFD não são equivalentes.")
    cadeia = input("Digite a cadeia a ser verificada: ").strip()
    if simular_afd(automato, cadeia):
        print("Cadeia aceita")
    else:
        print("Cadeia rejeitada")