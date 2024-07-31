def simular_afn(afn, cadeia):
    print(f"Simulando AFN com cadeia: {cadeia}")
    print(f"Estado inicial: {afn.estado_inicial}")
    estados_atuais = {afn.estado_inicial}
    for simbolo in cadeia:
        print(f"Estados atuais: {estados_atuais}, símbolo: {simbolo}")
        novos_estados = set()
        for estado in estados_atuais:
            if simbolo in afn.funcao_transicao.get(estado, {}):
                novos_estados.update(afn.funcao_transicao[estado][simbolo])
        estados_atuais = novos_estados
    return bool(estados_atuais & afn.estados_aceitacao)

def simular_afd(afd, cadeia):
    print(f"Simulando AFD com cadeia: {cadeia}")
    print(f"Estado inicial: {afd.estado_inicial}")
    estado_atual = afd.estado_inicial
    for simbolo in cadeia:
        print(f"Estado atual: {estado_atual}, símbolo: {simbolo}")
        if estado_atual in afd.funcao_transicao and simbolo in afd.funcao_transicao[estado_atual]:
            estado_atual = list(afd.funcao_transicao[estado_atual][simbolo])[0]
        else:
            print("Transição não encontrada, cadeia rejeitada.")
            return False
    print(f"Estado final: {estado_atual}")
    return estado_atual in afd.estados_aceitacao


