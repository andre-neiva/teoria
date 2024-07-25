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

'''A função converter_afn_para_afd é responsável por converter um Autômato Finito Não-determinístico (AFN)
em um Autômato Finito Determinístico (AFD). Inicialmente, a função define três estruturas de dados: 
novos_estados, uma lista para armazenar os novos estados do AFD; novas_transicoes, um dicionário para armazenar
as novas transições do AFD; e novos_estados_aceitacao, um conjunto para armazenar os novos estados de aceitação do AFD.

O estado inicial do AFD é definido como um conjunto congelado (frozenset) contendo o estado inicial do AFN.
Este estado inicial é então adicionado à lista novos_estados. A função também mantém um conjunto
estados_processados para rastrear quais estados já foram processados.

A função entra em um loop while que continua até que não haja mais novos estados a serem processados.
Dentro do loop, o estado atual é removido da lista novos_estados e adicionado ao conjunto estados_processados.
Para cada símbolo no alfabeto do AFN, a função calcula o novo estado resultante das transições a partir do estado atual.
Se uma transição existe para um determinado símbolo, o estado resultante é adicionado ao conjunto novo_estado.

O novo_estado é então convertido em um frozenset e, se não estiver vazio e ainda não tiver sido processado,
é adicionado à lista novos_estados. As novas transições são registradas no dicionário novas_transicoes.
Se o novo_estado contiver qualquer estado de aceitação do AFN, ele é adicionado ao conjunto novos_estados_aceitacao.

Após o loop, a lista novos_estados é atualizada para conter todos os estados processados. 
Finalmente, a função retorna uma nova instância de AF (presumivelmente uma classe que 
representa um autômato finito), com os novos estados, alfabeto, função de transição, estado inicial e
estados de aceitação do AFD.'''