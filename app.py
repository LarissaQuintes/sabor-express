import os

restaurantes = [{"nome": "Pizza Express", "categoria": "Pizza", "ativo": False},
                {"nome": "Suchi Taki", "categoria": "Japonês", "ativo": True},
                {"nome": "Lasanha italy", "categoria": "massa", "ativo": False}]
 
def exibir_nome_do_programa():
    """ Exibe o nome do programa na tela inicial com letras personalizadas"""

    print("""
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀""")


def exibir_opcoes():
    """Exibe as opções disponíveis no menu principal"""
    print()
    print("1. cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. ativar restaurante")
    print("4. sair\n")

def exibir_subtitulo(texto):
    """ Exibe substítulo personalizado na tela

    Input:
    - texto: str - O texto do subtítulo
    """
    os.system("cls")
    print(texto)
    linha = "-" *40
    print(linha)
    print()

def menu_principal():
    """Solicita uma tecla para voltar ao menu principal

    Outputs:
    -retornar ao menu principal
    """
    input("\nDigite ENTER para voltar ao menu principal")
    main()


def fechar_app():
    """Exibe a mensagem de finalização do aplicativo"""
    exibir_subtitulo("Saindo...")
    print("App finalizado com sucesso! 😎")
    print()

def opcao_invalida():
    """Exibe a mensagem de opção inválida

    Outputs:
    -Retornar ao menu principal
    """
    print("\nOpção invalida")
    menu_principal()

def cadastar_restaurante():
    """Essa função é responsável por cadastrar um novo 
    restaurante

    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    """
    exibir_subtitulo("Ｃａｄａｓｔｒｏ ｄｅ ｒｅｓｔａｕｒａｎｔｅ")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_do_restaurante = input(f"Digite a categoria que {nome_do_restaurante} mais se identifica: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria_do_restaurante, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    menu_principal()

def listar_restaurante():
    """Lista todos os resutautantes da lista restaurantes
    
    Outputs:
    - Exibe os restaurantes na tela
    """
    exibir_subtitulo("Ｌｉｓｔａ ｄｅ ｒｅｓｔａｕｒａｎｔｅｓ")
    print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(10)} | Status')
    linha = "-" * 40
    print(linha)
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        status = restaurante['ativo']
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f'👉 {nome_restaurante.ljust(16)} | {categoria.ljust(10)} | {ativo}')

    print()
    menu_principal()

def alterar_status():
    """Altera o status de um restaurante da lista
    
    Output:
    - Exibe a mensagem de alteração de status do restaurante
    """
    exibir_subtitulo("Ａｌｔｅｒａｎｄｏ ｓｔａｔｕｓ ｄｏ ｒｅｓｔａｕｒａｎｔｅ")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja alterar o status: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if(restaurante["nome"] == nome_do_restaurante):
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = (f"O restaurante {nome_do_restaurante} foi ativado com sucesso" if restaurante["ativo"] 
            else f"O restaurante {nome_do_restaurante} foi desativado com sucesso")
            print()
            print(mensagem)

    if not restaurante_encontrado:
         print(f"\nO restaurante {nome_do_restaurante} não foi encontrado")
            
    menu_principal()

def escolher_opcoes():
    """Solicita e executa a opção escolhida pelo usuário
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    """
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alterar_status()
        elif opcao_escolhida == 4:
            fechar_app()
        else: 
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    """ Função principal que inicia o programa"""
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
    main()