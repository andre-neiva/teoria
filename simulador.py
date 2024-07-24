
def simular_afn(afn, palavra):
    estados_atuais = {afn.estado_inicial}
    for simbolo in palavra:
        novos_estados = set()
        for estado in estados_atuais:
            if simbolo in afn.funcao_transicao.get(estado, {}):
                novos_estados.update(afn.funcao_transicao[estado][simbolo])
        estados_atuais = novos_estados
    return bool(estados_atuais & afn.estados_aceitacao)

def simular_afd(afd, palavra):
    estado_atual = afd.estado_inicial
    for simbolo in palavra:
        if simbolo in afd.funcao_transicao.get(estado_atual, {}):
            estado_atual = list(afd.funcao_transicao[estado_atual][simbolo])[0]
        else:
            return False
    return estado_atual in afd.estados_aceitacao