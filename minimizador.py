from af import AF

def minimizar_afd(afd):
    estados = list(afd.estados)
    alfabeto = afd.alfabeto
    funcao_transicao = afd.funcao_transicao
    estado_inicial = afd.estado_inicial
    estados_aceitacao = afd.estados_aceitacao

    distincoes = {(s1, s2): False for s1 in estados for s2 in estados if s1 != s2}

    for s1 in estados:
        for s2 in estados:
            if (s1 in estados_aceitacao) != (s2 in estados_aceitacao):
                distincoes[(s1, s2)] = True
                distincoes[(s2, s1)] = True

    while True:
        novos_marcados = []
        for (s1, s2), distinto in distincoes.items():
            if not distinto:
                for simbolo in alfabeto:
                    t1 = funcao_transicao.get((s1, simbolo), None)
                    t2 = funcao_transicao.get((s2, simbolo), None)
                    if t1 and t2 and t1 != t2 and distincoes.get((t1, t2), False):
                        novos_marcados.append((s1, s2))
                        break
        if not novos_marcados:
            break
        for s1, s2 in novos_marcados:
            distincoes[(s1, s2)] = True
            distincoes[(s2, s1)] = True

    representativos = {}
    for s in estados:
        for r in representativos.values():
            if not distincoes.get((s, r), False):
                representativos[s] = r
                break
        else:
            representativos[s] = s

    novos_estados = set(representativos.values())
    nova_funcao_transicao = {}
    for estado, transicoes in funcao_transicao.items():
        estado_rep = representativos[estado]
        if estado_rep not in nova_funcao_transicao:
            nova_funcao_transicao[estado_rep] = {}
        for simbolo, destinos in transicoes.items():
            destino_rep = representativos[next(iter(destinos))]
            if simbolo not in nova_funcao_transicao[estado_rep]:
                nova_funcao_transicao[estado_rep][simbolo] = set()
            nova_funcao_transicao[estado_rep][simbolo].add(destino_rep)

    novo_estado_inicial = representativos[estado_inicial]
    novos_estados_aceitacao = {representativos[estado] for estado in estados_aceitacao}

    return AF(
        estados=list(novos_estados),
        alfabeto=alfabeto,
        funcao_transicao={(k[0], k[1]): v for k, v in nova_funcao_transicao.items()},
        estado_inicial=novo_estado_inicial,
        estados_aceitacao=list(novos_estados_aceitacao)
    )
