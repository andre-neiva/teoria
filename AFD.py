from AF import AF

class AFD(AF): # Essa classe herda de AF, e define um autômato finito determinístico
    def __init__(self, A: set, Q: set, q: str, T: set, F: set) -> None:
        super().__init__(A, Q, q, T, F) # Chama o construtor da classe pai
        self.all_checks_str = "" # Inicializa a string que armazenará os checks

    def check_words(self, word): # Verifica se a palavra é aceita pelo autômato
        transactions = self.T # Pega as transações
        current_state = self.q
        for symbol in word: 
            if current_state != transactions[current_state].get(symbol)!= None: # Se o estado atual não for None
                current_state = transactions[current_state][symbol] # Atualiza o estado atual
            else: # Se o estado atual for None
                current_state = None # Atualiza o estado atual para None
        if current_state in self.F: # Se o estado atual estiver no conjunto de estados finais
            self.all_checks_str += f"A palavra {word} foi aceita\n" # Adiciona a palavra aceita na string
        else:
            self.all_checks_str += f"A palavra {word} não foi aceita\n"