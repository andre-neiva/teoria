
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

'''As funções simular_afn e simular_afd são utilizadas para simular autômatos finitos não determinísticos
(AFN) e autômatos finitos determinísticos (AFD), respectivamente. Ambas as funções recebem dois parâmetros:
o autômato (afn ou afd) e a palavra a ser processada.

A função simular_afn começa inicializando o conjunto de estados atuais com o estado inicial do AFN.
Para cada símbolo na palavra, ela cria um novo conjunto de estados (novos_estados). Em seguida, para cada
estado no conjunto de estados atuais, verifica se há uma transição definida para o símbolo atual. Se houver,
os estados resultantes dessa transição são adicionados ao conjunto de novos estados. Após processar todos os
estados atuais para o símbolo atual, o conjunto de estados atuais é atualizado para os novos estados. No final,
a função retorna True se houver interseção entre os estados atuais e os estados de aceitação do AFN, indicando
que a palavra é aceita pelo autômato.

A função simular_afd é mais simples devido à natureza determinística do AFD. Ela começa definindo o estado
atual como o estado inicial do AFD. Para cada símbolo na palavra, verifica se há uma transição definida para
o símbolo no estado atual. Se houver, o estado atual é atualizado para o estado resultante da transição.
Se não houver transição definida, a função retorna False, indicando que a palavra não é aceita pelo autômato.
Após processar todos os símbolos da palavra, a função retorna True se o estado atual estiver entre os estados
de aceitação do AFD, indicando que a palavra é aceita pelo autômato.

Essas funções são fundamentais para a simulação de autômatos finitos, permitindo verificar se uma determinada
palavra é aceita por um autômato, seja ele determinístico ou não determinístico.'''