import produto
import venda
import procedures
import views
import Login
import createdelete
import cliente

def inicializar_banco():
    """
    Verifica e cria o banco de dados se necessário
    """
    print("\n" + "=" * 40)
    print("   INICIALIZANDO SISTEMA E-COMMERCE")
    print("=" * 40)
    print("\nVerificando banco de dados...")

    HOST = 'localhost'
    USER = 'root'
    PASSWORD = input("Digite a senha do root do MySQL: ")

    success = createdelete.create_database_from_file(HOST, USER, PASSWORD)

    if success:
        print("\n✓ Sistema pronto para uso!")
        return True
    else:
        print("\n✗ Erro ao inicializar o banco de dados.")
        return False


def menu():
    cargo = Login.login()

    if cargo is None:
        return

    if cargo == 1:
        usuario = "ceo_ecommerce"
        senha = "Ceo123456"
        print("\nLogado como CEO.")
    elif cargo == 2:
        usuario = "gerente_ecommerce"
        senha = "Gerente123"
        print("\nLogado como Gerente.")
    elif cargo == 3:
        usuario = "funcionario_ecommerce"
        senha = "SenhaFunc123"
        print("\nLogado como Funcionário.")
    else:
        print("Cargo inválido.")
        return

    while True:
        print("\n" + "=" * 40)
        print("       *MENU PRINCIPAL*  E-COMMERCE")
        print("=" * 40)
        print("\n    CLIENTES    ")
        print("1: Cadastramento de cliente")
        print("2: Lista dos clientes")

        print("\n    PRODUTOS    ")
        print("3: Cadastramento de produto")
        print("4: Lista dos produtos")

        print("\n    VENDAS    ")
        print("5: Registramento de venda")
        print("6: Lista das vendas")

        print("\n    PROCESSOS    ")
        print("7: Reajustar Salário")
        print("8: Sorteio de Prêmio")
        print("9: Estatísticas de Venda ")

        print("\n    CHECAGENS    ")
        print("10: Vendas Por Vendedor")
        print("11: Clientes Especiais")
        print("12: Produtos Vendidos")

        print("\n    BANCO DE DADOS    ")
        print("13 - Deletar banco de dados!")

        print("\n--- SISTEMA ---")
        print("0 - Sair")
        print("=" * 40)

        opc = input("\nEscolha uma opção: ").strip()

        if opc == "1":
            cliente.cadastrar_cliente(usuario, senha)
        elif opc == "2":
            cliente.listar_clientes(usuario, senha)
        elif opc == "3":
            produto.cadastrar_produto(usuario, senha)
        elif opc == "4":
            produto.listar_produtos(usuario, senha)
        elif opc == "5":
            venda.registrar_venda(usuario, senha)
        elif opc == "6":
            venda.listar_vendas(usuario, senha)
        elif opc == "7":
            procedures.executar_reajuste(usuario, senha)
        elif opc == "8":
            procedures.executar_sorteio(usuario, senha)
        elif opc == "9":
            procedures.executar_estatisticas(usuario, senha)
        elif opc == "10":
            views.ver_vendas_vendedor(usuario, senha)
        elif opc == "11":
            views.ver_clientes_especiais(usuario, senha)
        elif opc == "12":
            views.ver_produtos_vendidos(usuario, senha)
        elif opc == "13":
            print("\n  CUIDADO: Isso irá DELETAR todo o banco de dados!")
            confirmacao = input("Digite 'DELETAR' para continuar: ")
            if confirmacao == "DELETAR":
                senha_root = input("Digite a senha do root do MySQL: ")
                createdelete.drop_database('localhost', 'root', senha_root, 'ECOMMERCE')
                print("\n✓ Banco de dados deletado. Encerrando sistema...")
                break
            else:
                print("Operação cancelada.")
        elif opc == "0":
            print("\nSistema encerrado. Até logo!")
            break
        else:
            print("\n  Opção inválida! Escolha uma opção do menu.")


if __name__ == "__main__":
    if inicializar_banco():
        menu()
    else:
        print("\nNão foi possível iniciar o sistema.")