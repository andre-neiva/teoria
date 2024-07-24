from af import AF
def minimizar_afd(afd):
    estados = list(afd.estados)
    n = len(estados)
    tabela = [[False] * n for _ in range(n)]

    # Marcar pares de estados distinguíveis
    for i in range(n):
        for j in range(i + 1, n):
            if (estados[i] in afd.estados_aceitacao) != (estados[j] in afd.estados_aceitacao):
                tabela[i][j] = True

    # Propagar distinções
    mudanca = True
    while mudanca:
        mudanca = False
        for i in range(n):
            for j in range(i + 1, n):
                if not tabela[i][j]:
                    for simbolo in afd.alfabeto:
                        trans_i = afd.funcao_transicao.get(estados[i], {}).get(simbolo)
                        trans_j = afd.funcao_transicao.get(estados[j], {}).get(simbolo)
                        if trans_i and trans_j:
                            idx_i = estados.index(trans_i)
                            idx_j = estados.index(trans_j)
                            if tabela[min(idx_i, idx_j)][max(idx_i, idx_j)]:
                                tabela[i][j] = True
                                mudanca = True

    # Fusão de estados equivalentes
    novos_estados = []
    estado_map = {}
    for i in range(n):
        for j in range(i + 1, n):
            if not tabela[i][j]:
                estado_map[estados[j]] = estados[i]

    for estado in estados:
        if estado not in estado_map:
            novos_estados.append(estado)

    nova_funcao_transicao = {}
    for estado in novos_estados:
        nova_funcao_transicao[estado] = {}
        for simbolo in afd.alfabeto:
            trans = afd.funcao_transicao.get(estado, {}).get(simbolo)
            if trans:
                nova_funcao_transicao[estado][simbolo] = estado_map.get(trans, trans)

    novo_estado_inicial = estado_map.get(afd.estado_inicial, afd.estado_inicial)
    novos_estados_aceitacao = {estado_map.get(estado, estado) for estado in afd.estados_aceitacao}

    return AF(set(novos_estados), afd.alfabeto, nova_funcao_transicao, novo_estado_inicial, novos_estados_aceitacao)