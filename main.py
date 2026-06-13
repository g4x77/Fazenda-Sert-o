from rich.console import Console

import auth
import fazenda
import cliente

console = Console()


def menu_rebanho():
    continuar = True
    while continuar:
        console.print("--- GERENCIAR REBANHO ---")
        console.print("  1 - Listar animais")
        console.print("  2 - Cadastrar animal")
        console.print("  3 - Buscar animal")
        console.print("  4 - Atualizar status")
        console.print("  5 - Remover animal")
        console.print("  0 - Voltar")
        opcao = input("  Opcao: ")

        if opcao == "1":
            fazenda.listar_animais()
        elif opcao == "2":
            fazenda.cadastrar_animal()
        elif opcao == "3":
            fazenda.buscar_animal()
        elif opcao == "4":
            fazenda.atualizar_status_animal()
        elif opcao == "5":
            fazenda.remover_animal()
        elif opcao == "0":
            continuar = False
        else:
            console.print("  Opcao invalida.")


def menu_producao():
    continuar = True
    while continuar:
        console.print("--- PRODUCAO E ESTOQUE ---")
        console.print("  1 - Registrar ordenha do dia")
        console.print("  2 - Ver historico de ordenhas")
        console.print("  3 - Adicionar produto ao estoque")
        console.print("  4 - Ver estoque atual")
        console.print("  0 - Voltar")
        opcao = input("  Opcao: ")

        if opcao == "1":
            fazenda.registrar_ordenha()
        elif opcao == "2":
            fazenda.listar_ordenhas()
        elif opcao == "3":
            fazenda.adicionar_produto_estoque()
        elif opcao == "4":
            fazenda.listar_estoque()
        elif opcao == "0":
            continuar = False
        else:
            console.print("  Opcao invalida.")


def menu_adm(usuario):
    continuar = True
    while continuar:
        console.print("Logado como ADM: " + usuario["login"])
        console.print("  1 - Gerenciar Rebanho")
        console.print("  2 - Producao e Estoque")
        console.print("  3 - Relatorio Geral da Fazenda")
        console.print("  4 - Historico de Movimentacao")
        console.print("  0 - Logout")
        opcao = input("  Opcao: ")

        if opcao == "1":
            menu_rebanho()
        elif opcao == "2":
            menu_producao()
        elif opcao == "3":
            fazenda.relatorio_geral()
        elif opcao == "4":
            fazenda.listar_historico()
        elif opcao == "0":
            console.print("  Ate logo, " + usuario["login"])
            continuar = False
        else:
            console.print("  Opcao invalida.")


def menu_loja():
    continuar = True
    while continuar:
        console.print("--- LOJA ---")
        console.print("  1 - Ver produtos disponiveis")
        console.print("  2 - Comprar produto")
        console.print("  3 - Ver animais para venda")
        console.print("  0 - Voltar")
        opcao = input("  Opcao: ")

        if opcao == "1":
            cliente.ver_estoque_cliente()
        elif opcao == "2":
            cliente.comprar_produto()
        elif opcao == "3":
            cliente.ver_animais_venda()
        elif opcao == "0":
            continuar = False
        else:
            console.print("  Opcao invalida.")


def menu_cliente(usuario):
    continuar = True
    while continuar:
        console.print("Logado como CLIENTE: " + usuario["login"])
        console.print("  1 - Ver estoque e comprar")
        console.print("  2 - Agendar retirada")
        console.print("  3 - Meus agendamentos")
        console.print("  4 - Calcular frete")
        console.print("  0 - Logout")
        opcao = input("  Opcao: ")

        if opcao == "1":
            menu_loja()
        elif opcao == "2":
            cliente.agendar_retirada(usuario["login"])
        elif opcao == "3":
            cliente.listar_meus_agendamentos(usuario["login"])
        elif opcao == "4":
            cliente.calculadora_frete()
        elif opcao == "0":
            console.print("  Ate logo, " + usuario["login"])
            continuar = False
        else:
            console.print("  Opcao invalida.")


rodando = True

while rodando:
    console.print("============================================")
    console.print("   FAZENDA SERTAO - Sistema de Gestao")
    console.print("============================================")
    console.print("  1 - Fazer login")
    console.print("  2 - Cadastrar usuario")
    console.print("  0 - Sair")
    opcao = input("  Opcao: ")

    if opcao == "1":
        usuario = auth.fazer_login()
        if usuario != None:
            if usuario["perfil"] == "ADM":
                menu_adm(usuario)
            else:
                menu_cliente(usuario)

    elif opcao == "2":
        auth.cadastrar_usuario()

    elif opcao == "0":
        console.print("  Encerrando sistema. Ate logo!")
        rodando = False

    else:
        console.print("  Opcao invalida.")