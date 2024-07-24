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