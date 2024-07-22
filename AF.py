# AF = (A, Q, q, T, F)
class AF: # Automato Finito
    def __init__(self, A: set, Q: set, q: str, T: set, F: set) -> None:
        self.A = A
        self.Q = Q
        self.q = q
        self.T = T
        self.F = F

# Aqui foi definido o alfabeto, o conjunto de estados, o estado inicial, o conjunto de transições e o conjunto de estados finais