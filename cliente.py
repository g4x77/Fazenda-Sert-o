from rich.console import Console
from rich.table import Table
import requests
from datetime import datetime

import fazenda

console = Console()

agendamentos = []


def ver_estoque_cliente():
    fazenda.listar_estoque()


def comprar_produto():
    console.print("--- COMPRAR PRODUTO ---")
    fazenda.listar_estoque()

    nome_prod = input("  Nome do produto que deseja comprar: ")

    achou = False
    i = 0
    while i < len(fazenda.estoque):
        nome_estoque = fazenda.estoque[i]["produto"]
        if nome_estoque.lower() == nome_prod.lower():
            achou = True

            qtd_compra = float(input("  Quantidade (kg): "))

            if qtd_compra <= 0:
                console.print("  Quantidade invalida.")
            elif qtd_compra > fazenda.estoque[i]["qtd"]:
                console.print("  Quantidade indisponivel. Temos: " + str(fazenda.estoque[i]["qtd"]) + " kg")
            else:
                total_compra = qtd_compra * fazenda.estoque[i]["preco"]
                console.print("  Produto: " + fazenda.estoque[i]["produto"])
                console.print("  Qtd    : " + str(qtd_compra) + " kg")
                console.print("  Total  : R$ " + str(round(total_compra, 2)))

                confirma = input("  Confirmar? (s/n): ")
                if confirma == "s":
                    fazenda.estoque[i]["qtd"] = fazenda.estoque[i]["qtd"] - qtd_compra
                    nova_venda = {"produto": fazenda.estoque[i]["produto"], "qtd": qtd_compra, "total": round(total_compra, 2)}
                    fazenda.vendas.append(nova_venda)
                    fazenda.registrar_historico("venda", fazenda.estoque[i]["produto"], qtd_compra)
                    console.print("  Compra realizada!")
                else:
                    console.print("  Cancelado.")
        i = i + 1

    if not achou:
        console.print("  Produto nao encontrado.")


def ver_animais_venda():
    tem_animal = False

    tabela = Table(title="Animais Disponiveis para Venda")
    tabela.add_column("Brinco")
    tabela.add_column("Tipo")
    tabela.add_column("Peso (kg)")

    i = 0
    while i < len(fazenda.animais):
        if fazenda.animais[i]["status"] == "Venda":
            tabela.add_row(fazenda.animais[i]["brinco"], fazenda.animais[i]["tipo"], str(fazenda.animais[i]["peso"]))
            tem_animal = True
        i = i + 1

    if tem_animal:
        console.print(tabela)
    else:
        console.print("  Nenhum animal disponivel para venda.")


def buscar_endereco_por_cep(cep):
    cep = cep.replace("-", "")
    cep = cep.strip()

    url = "https://viacep.com.br/ws/" + cep + "/json/"
    resposta = requests.get(url)
    dados = resposta.json()

    if "erro" in dados:
        return None
    else:
        return dados


def agendar_retirada(usuario_logado):
    console.print("--- AGENDAR RETIRADA ---")

    data_ag = input("  Data da retirada (DD/MM/AAAA): ")
    hora_ag = input("  Horario (HH:MM)              : ")

    console.print("  Tipo: 1-Queijos  2-Leite  3-Animais  4-Misto")
    op_tipo = input("  Escolha: ")

    if op_tipo == "1":
        tipo_ag = "Queijos"
    elif op_tipo == "2":
        tipo_ag = "Leite"
    elif op_tipo == "3":
        tipo_ag = "Animais"
    else:
        tipo_ag = "Misto"

    if data_ag == "" or hora_ag == "":
        console.print("  Data e horario sao obrigatorios.")
        return

    endereco = None
    usar_cep = input("  Deseja buscar o endereco pelo CEP? (s/n): ")

    if usar_cep == "s":
        cep = input("  Digite o CEP (somente numeros): ")
        endereco = buscar_endereco_por_cep(cep)

        if endereco != None:
            console.print("  Endereco encontrado: " + endereco["logradouro"] + ", " + endereco["bairro"] + " - " + endereco["localidade"] + "/" + endereco["uf"])
        else:
            console.print("  CEP nao encontrado. Endereco ficara em branco.")

    novo_agendamento = {"cliente": usuario_logado, "data": data_ag, "hora": hora_ag, "tipo": tipo_ag, "endereco": endereco}
    agendamentos.append(novo_agendamento)

    gerar_recibo(novo_agendamento)


def gerar_recibo(agendamento):
    console.print("====================================")
    console.print("   RECIBO / TICKET DE CARGA")
    console.print("   FAZENDA SERTAO")
    console.print("====================================")
    console.print("Cliente: " + agendamento["cliente"])
    console.print("Data de retirada: " + agendamento["data"] + " as " + agendamento["hora"])
    console.print("Tipo de carga: " + agendamento["tipo"])

    if agendamento["endereco"] != None:
        e = agendamento["endereco"]
        console.print("Endereco: " + e["logradouro"] + ", " + e["bairro"] + " - " + e["localidade"] + "/" + e["uf"])

    console.print("")
    console.print("Itens da carga:")

    if len(fazenda.vendas) == 0:
        console.print("  Nenhum item de compra registrado nesta sessao.")
    else:
        i = 0
        while i < len(fazenda.vendas):
            console.print("  " + fazenda.vendas[i]["produto"] + " - " + str(fazenda.vendas[i]["qtd"]) + " kg - R$ " + str(fazenda.vendas[i]["total"]))
            i = i + 1

    agora = datetime.now()
    console.print("")
    console.print("Emitido em: " + agora.strftime("%d/%m/%Y %H:%M"))
    console.print("====================================")


def listar_meus_agendamentos(usuario_logado):
    tem_agendamento = False

    tabela = Table(title="Meus Agendamentos")
    tabela.add_column("Data")
    tabela.add_column("Hora")
    tabela.add_column("Tipo")

    i = 0
    while i < len(agendamentos):
        if agendamentos[i]["cliente"] == usuario_logado:
            tabela.add_row(agendamentos[i]["data"], agendamentos[i]["hora"], agendamentos[i]["tipo"])
            tem_agendamento = True
        i = i + 1

    if tem_agendamento:
        console.print(tabela)
    else:
        console.print("  Nenhum agendamento encontrado.")


def calculadora_frete():
    console.print("--- CALCULADORA DE FRETE ---")

    distancia = float(input("  Distancia em km ate a fazenda: "))

    console.print("  Veiculo: 1-Pequeno R$2,50/km  2-Medio R$4,00/km  3-Grande R$6,50/km")
    op_vei = input("  Escolha: ")

    if op_vei == "1":
        preco_km = 2.50
    elif op_vei == "2":
        preco_km = 4.00
    else:
        preco_km = 6.50

    frete = distancia * preco_km

    console.print("  Distancia: " + str(distancia) + " km")
    console.print("  Frete    : R$ " + str(round(frete, 2)))

    if frete > 500:
        console.print("  Aviso: frete alto! Considere consolidar cargas.")