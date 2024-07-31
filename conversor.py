from af import AF

def converter_afn_para_afd(afn):
    novos_estados = []
    novas_transicoes = {}
    novos_estados_aceitacao = set()
    
    estado_inicial_afd = frozenset([afn.estado_inicial])
    novos_estados.append(estado_inicial_afd)
    estados_processados = set()

    estados_aceitacao_set = set(afn.estados_aceitacao)

    while novos_estados:
        estado_atual = novos_estados.pop(0)
        estados_processados.add(estado_atual)

        for simbolo in afn.alfabeto:
            novo_estado = set()
            for estado in estado_atual:
                if estado in afn.funcao_transicao and simbolo in afn.funcao_transicao[estado]:
                    novo_estado.update(afn.funcao_transicao[estado][simbolo])
            
            novo_estado = frozenset(novo_estado)
            if novo_estado and novo_estado not in estados_processados:
                novos_estados.append(novo_estado)
            
            novas_transicoes[(tuple(estado_atual), simbolo)] = tuple(novo_estado)
            
            if novo_estado & estados_aceitacao_set:
                novos_estados_aceitacao.add(tuple(novo_estado))

    novos_estados = [tuple(s) for s in estados_processados]
    novas_transicoes = {(tuple(k[0]), k[1]): tuple(v) for k, v in novas_transicoes.items()}
    novos_estados_aceitacao = [tuple(s) for s in novos_estados_aceitacao]
    estado_inicial_afd = tuple(estado_inicial_afd)

    return AF(
        estados=novos_estados,
        alfabeto=afn.alfabeto,
        funcao_transicao=novas_transicoes,
        estado_inicial=estado_inicial_afd,
        estados_aceitacao=novos_estados_aceitacao
    )
