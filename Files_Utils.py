def open_file(path: str):
    try:
        f = open(path, "r", encoding="utf-8")
        content = f.read()
        f.close()
        return content
    except:
        raise ValueError(f'Erro ao tentar abrir o arquivo: {path}.')
    
def verify_file_content():
    entrada_content = open_file("entrada.txt").split('\n')
    palavra_content = open_file("palavras.txt").split('\n')
    
    print("Conteúdo de entrada.txt:")
    for line in entrada_content:
        print(line)
    
    print("\nConteúdo de palavras.txt:")
    for line in palavra_content:
        print(line)

def save_file(path: str, content: str):
    try:
        f = open(path, "w", encoding="utf-8")
        f.write(content)
        f.close()
    except:
        raise ValueError(f'Erro ao tentar salvar o arquivo: {path}.')