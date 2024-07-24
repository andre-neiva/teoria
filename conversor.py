from af import AF

def converter_afn_para_afd(afn):
    novos_estados = []
    novas_transicoes = {}
    novos_estados_aceitacao = set()
    
    # Estado inicial do AFD é o conjunto contendo o estado inicial do AFN
    estado_inicial_afd = frozenset([afn.estado_inicial])
    novos_estados.append(estado_inicial_afd)
    estados_processados = set()

    while novos_estados:
        estado_atual = novos_estados.pop(0)
        estados_processados.add(estado_atual)

        for simbolo in afn.alfabeto:
            novo_estado = set()
            for estado in estado_atual:
                if (estado, simbolo) in afn.funcao_transicao:
                    novo_estado.update(afn.funcao_transicao[(estado, simbolo)])
            
            novo_estado = frozenset(novo_estado)
            if novo_estado and novo_estado not in estados_processados:
                novos_estados.append(novo_estado)
            
            novas_transicoes[(estado_atual, simbolo)] = novo_estado
            
            if novo_estado & set(afn.estados_aceitacao):
                novos_estados_aceitacao.add(novo_estado)

    novos_estados = list(estados_processados)
    
    return AF(
        estados=novos_estados,
        alfabeto=afn.alfabeto,
        funcao_transicao=novas_transicoes,
        estado_inicial=estado_inicial_afd,
        estados_aceitacao=list(novos_estados_aceitacao)
    )