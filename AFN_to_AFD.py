from AF import AF
from AFD import AFD
from copy import deepcopy # Aqui foi importado o deepcopy para fazer uma cópia profunda de um objeto

def merge_dict(a: dict, b: dict): # Função que faz a união de dois dicionários
    keys = list(b.keys())
    new_dict = deepcopy(a)

    for key in keys:
        if key in a.keys(): # Se a chave estiver no dicionário a
            new_dict[key] = new_dict[key].union(b[key]) # Faz a união dos conjuntos
        else:
            new_dict[key] = b[key] # Se não, adiciona a chave ao dicionário
        
    return new_dict

def merge_states(states): # Função que faz a união de estados
    aux = list("".join(states)) # Concatena os estados
    aux = list(dict.fromkeys(aux)) # Remove os estados repetidos
    aux.sort() # Ordena os estados

    return "".join(aux) # Retorna os estados concatenados

def merge_transition(states, in_state, afn: AF):
    transition = {}
    for state in states:
        transition = merge_dict(transition, afn.T[state]) # Faz a união das transições

    afn.T[in_state] = transition # Adiciona as transições ao autômato

def has_transition_non_deterministic(afn: AF):   # Função que verifica se há transições não determinísticas
    for transitions in afn.T.values():           # Para cada transição nos valores do autômato
        for transition in transitions:           # Para cada transição em transições
            if len(transitions[transition]) > 1: # Se o tamanho da transição for maior que 1
                return True
    return False

def is_final_state(afn: AF, transition): # Função que verifica se o estado é final
    for state in afn.F:           # Para cada estado em F   
        if state in transition:   # Se o estado estiver na transição
            return True
    return False

def AFN_to_AFD(afn: AF): # Função que converte um autômato finito não determinístico em determinístico
    try:
        afn = deepcopy(afn) # Faz uma cópia profunda do autômato

        # Conversor
        while has_transition_non_deterministic(afn):
            afn_aux = deepcopy(afn)                                             # Faz uma cópia profunda do autômato
            for state, transitions in afn.T.items():                            # Para cada estado e transição do autômato
                for transition in transitions:                                  # Para cada transição em transições
                    if len(transitions[transition]) > 1:                        # Se o tamanho da transição for maior que 1
                        new_state = merge_states(transitions[transition])       # Faz a união dos estados
                        if new_state not in afn_aux.Q:                          # Se o novo estado não estiver em Q
                            afn_aux.Q.add(new_state)                            # Adiciona o novo estado a Q
                            afn_aux.T[new_state] = {}                           # Inicializa as transições do novo estado como um dicionário

                            merge_transition(
                                transitions[transition], new_state, afn_aux)    # Faz a união das transições
                            if is_final_state(afn, transitions[transition]):    # Se o estado for final
                                afn_aux.F.add(new_state)                        # Adiciona o estado a F

                        afn_aux.T[state][transition] = {new_state}              # Adiciona o novo estado à transição

            afn = afn_aux                                                       # Atualiza o autômato
        
        # Busca estados visitados
        visited_state = []
        state_queue = [afn.q]
        while state_queue:                                                      # Enquanto a fila de estados não estiver vazia
            current_state = state_queue.pop()                                   # Pega o estado atual
            if current_state not in visited_state:                              # Se o estado atual não estiver nos estados visitados
                visited_state.append(current_state)                             # Adiciona o estado atual aos estados visitados
                
            for transition in afn.T[current_state].values():                    # Para cada transição nos valores do estado atual
                if transition and list(transition)[0] not in visited_state + state_queue:      # Se a transição não estiver nos estados visitados e na fila de estados
                    state_queue.append(list(transition)[0])                     # Adiciona a transição à fila de estados

        # Retirar os estados não visitados
        for state in afn.Q.copy():                                          # Para cada estado em Q
            if state not in visited_state:                                  # Se o estado não estiver nos estados visitados
                afn.Q.discard(state)                                        # Remove o estado de Q
                afn.F.discard(state)                                        # Remove o estado de F
                del afn.T[state]                                            # Remove o estado de T

        for state in afn.Q:
            transitions = afn.T[state]
            for symbol in transitions.keys():
                transitions[symbol] = list(transitions[symbol])[0]

        afd = AFD(afn.A, afn.Q, afn.q, afn.T, afn.F) # Cria um autômato finito determinístico
        return afd # Retorna o autômato finito determiníst
    except Exception as e:
        raise ValueError(f"Erro ao converter AFN para AFD: {e}")

