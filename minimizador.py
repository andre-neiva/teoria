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



'''A função minimizar_afd é responsável por minimizar um Autômato Finito Determinístico (AFD). O objetivo da minimização
é reduzir o número de estados do AFD, mantendo seu comportamento original. A função começa convertendo os estados do AFD
em uma lista e inicializando uma tabela para marcar pares de estados distinguíveis. A tabela é uma matriz booleana onde
cada entrada indica se um par de estados é distinguível.

Primeiramente, a função marca os pares de estados distinguíveis com base nos estados de aceitação. Se um estado está
em estados_aceitacao e o outro não, eles são marcados como distinguíveis. Em seguida, a função propaga essas distinções.
Para cada par de estados não marcados como distinguíveis, a função verifica as transições para cada símbolo do alfabeto.
Se as transições levam a estados que já foram marcados como distinguíveis, o par atual também é marcado como distinguível.

Após propagar as distinções, a função identifica e funde estados equivalentes. Ela cria um mapeamento de estados equivalentes,
onde estados indistinguíveis são mapeados para um estado representativo. Em seguida, a função constrói um novo conjunto de
estados e uma nova função de transição, substituindo os estados equivalentes pelos seus representantes.

Finalmente, a função ajusta o estado inicial e os estados de aceitação do AFD minimizado, utilizando o
mapeamento de estados equivalentes. O resultado é um novo AFD com um conjunto reduzido de estados, mas que aceita
a mesma linguagem que o AFD original. A função retorna uma nova instância da classe AF representando o AFD minimizado.'''