from AF import AF
from AFN_to_AFD import AFN_to_AFD
from AFNDE_to_AFN import AFNDE_to_AFN
from copy import deepcopy
from graphviz import Digraph

def open_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def save_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def get_line_content(line):
    try:
        return set(line.strip().split(' '))
    except:
        raise ValueError(f'Erro ao tentar ler a linha: {line}.')

def add_transitions_pattern(Q, A, T):
    try:
        for state in Q:
            if state not in T:
                T[state] = {}
            for letter in A:
                if letter not in T[state]:
                    T[state][letter] = set()
            if 'ê' not in T[state]:
                T[state]['ê'] = set()
        return T
    except Exception as e:
        raise ValueError(f'Erro ao tentar transformar as transições em um dicionário: {e}')

def transform_transaction(aux_T, T):
    for transaction in aux_T:
        current_state = transaction[0]
        letter = transaction[1]
        next_state = transaction[2]
        if current_state not in T:
            T[current_state] = {}
        if letter not in T[current_state]:
            T[current_state][letter] = set()
        T[current_state][letter].add(next_state)
    return T

def verify_and_parse_files():
    content_file = open_file("entrada.txt").split('\n')
    content_words = open_file("palavras.txt").split('\n')

    if len(content_file) < 3:
        raise ValueError("Arquivo entrada.txt deve ter pelo menos três linhas (estados, estado inicial e estados finais).")

    for line in content_file[3:]:
        if len(line.strip().split()) != 3:
            raise ValueError(f"Transição inválida: {line}")

    return content_file, content_words

if __name__ == "__main__":
    try:
        content_file, content_words = verify_and_parse_files()

        A = {'1', '0'}
        Q = get_line_content(content_file[0])
        q = content_file[1].strip()
        F = get_line_content(content_file[2])
        T = {}
        aux_T = []

        content_transition = content_file[3:]
        line_count = 0

        for line in content_transition:
            transaction = line.strip().split()
            if len(transaction) == 3:
                aux_T.append(
                    (transaction[0], transaction[1], transaction[2])
                )
            else:
                raise ValueError(f'Não foi possível identificar a transição na linha: {line_count}.')
            line_count += 1

        print(f"Estados: {Q}")
        print(f"Estado inicial: {q}")
        print(f"Estados finais: {F}")
        print(f"Transições auxiliares: {aux_T}")

        T = add_transitions_pattern(Q, A, T)
        T = transform_transaction(aux_T, T)

        print(f"Transições finais: {T}")

        M_AFNDE = AF(A, Q, q, T, F)
        print(f"AFNDE: {M_AFNDE}")

        M_AFN = AFNDE_to_AFN(M_AFNDE)
        print(f"AFN: {M_AFN}")

        M_AFD = AFN_to_AFD(M_AFN)
        print(f"AFD: {M_AFD}")

        P = [word.strip() for word in content_words if word.strip()]

        for word in P:
            M_AFD.check_words(word)

        save_file("saida.txt", M_AFD.all_checks_str)

        afd_table = "{}\n".format(" ".join(M_AFD.Q))
        afd_table += "{}\n".format(M_AFD.q)
        afd_table += "{}\n".format(" ".join(M_AFD.F))

        for state, transitions in M_AFD.T.items():
            for symbol, next_state in transitions.items():
                afd_table += "{} {} {}\n".format(state, symbol, next_state)

        save_file("afd_tabela.txt", afd_table)

        afn_graph = Digraph("AFN")
        afn_graph.attr(rankdir="LR")

        initial_state = q
        final_states = F

        for state, transitions in M_AFNDE.T.items():
            if state == initial_state:
                afn_graph.node(state, label=state, shape="circle", color="red")
            elif state in final_states:
                afn_graph.node(state, label=state, shape="doublecircle", color="red")
            else:
                afn_graph.node(state, label=state)

        for state, transitions in M_AFNDE.T.items():
            for symbol, next_states in transitions.items():
                for next_state in next_states:
                    afn_graph.edge(state, next_state, label=symbol)

        afn_graph.render("AFN", format="png")

        afd_graph = Digraph("AFD")
        afd_graph.attr(rankdir="LR")

        final_states_afd = M_AFD.F

        for state, transitions in M_AFD.T.items():
            if state == initial_state:
                afd_graph.node(state, label=state, shape="circle", color="red")
            elif state in final_states_afd:
                afd_graph.node(state, label=state, shape="doublecircle", color="red")
            else:
                afd_graph.node(state, label=state)

        for state, transitions in M_AFD.T.items():
            for symbol, next_state in transitions.items():
                afd_graph.edge(state, next_state, label=symbol)

        afd_graph.render("AFD", format="png")

    except Exception as e:
        print("Ocorreu um erro:")
        print(e)
