class AF:
    def __init__(self, estados, alfabeto, funcao_transicao, estado_inicial, estados_aceitacao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.funcao_transicao = funcao_transicao
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao

    def transicao(self, estado, simbolo):
        if estado in self.funcao_transicao and simbolo in self.funcao_transicao[estado]:
            return self.funcao_transicao[estado][simbolo]
        return set()

    def aceita(self, cadeia):
        estados_atuais = {self.estado_inicial}
        for simbolo in cadeia:
            novos_estados = set()
            for estado in estados_atuais:
                novos_estados.update(self.transicao(estado, simbolo))
            estados_atuais = novos_estados
        return bool(estados_atuais & self.estados_aceitacao)
    
'''A classe AF representa um Autômato Finito, uma estrutura matemática usada para modelar sistemas com estados finitos.
O método __init__ inicializa uma instância da classe com cinco parâmetros: estados, que é um conjunto de estados do autômato;
alfabeto, que é o conjunto de símbolos que o autômato pode processar; funcao_transicao, que é um dicionário que define as
transições entre estados com base em símbolos; estado_inicial, que é o estado onde o autômato começa; e estados_aceitacao,
que é o conjunto de estados de aceitação do autômato.

O método transicao é responsável por retornar o próximo estado ou conjunto de estados para um dado estado e símbolo.
Ele verifica se o estado atual e o símbolo estão definidos na função de transição. Se estiverem, ele retorna o estado
ou estados resultantes; caso contrário, retorna um conjunto vazio.

O método aceita determina se uma cadeia de símbolos é aceita pelo autômato. Ele começa no estado inicial e processa cada
símbolo da cadeia, atualizando o conjunto de estados atuais com base nas transições definidas. No final, verifica se algum
dos estados atuais está no conjunto de estados de aceitação. Se estiver, a cadeia é aceita, e o método retorna True;
caso contrário, retorna False.'''