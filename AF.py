class AF:
    def __init__(self, estados, alfabeto, funcao_transicao, estado_inicial, estados_aceitacao):
        self.estados = estados
        self.alfabeto = alfabeto
        self.funcao_transicao = funcao_transicao
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao

    def __repr__(self):
        return (f"AF(estados={self.estados}, alfabeto={self.alfabeto}, "
                f"funcao_transicao={self.funcao_transicao}, estado_inicial={self.estado_inicial}, "
                f"estados_aceitacao={self.estados_aceitacao})")
