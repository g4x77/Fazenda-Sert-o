from rich.console import Console
from rich.table import Table
from datetime import datetime

console = Console()

animais = [
    {"brinco": "BOV-001", "tipo": "Bovino de Leite", "status": "Em lactacao", "peso": 420.0},
    {"brinco": "CAP-001", "tipo": "Caprino", "status": "Em lactacao", "peso": 45.0},
    {"brinco": "SUI-001", "tipo": "Suino/Leitao", "status": "Venda", "peso": 35.0},
]

estoque = [
    {"produto": "Queijo Coalho", "qtd": 100.0, "preco": 32.00},
    {"produto": "Queijo Manteiga", "qtd": 40.0, "preco": 55.00},
]

ordenhas = [
    {"data": "12/05/2025", "litros": 180.0, "valor_litro": 2.80},
    {"data": "13/05/2025", "litros": 165.0, "valor_litro": 2.80},
]

vendas = []

historico = []


def registrar_historico(acao, item, qtd):
    agora = datetime.now()
    data_hora = agora.strftime("%d/%m/%Y %H:%M")
    novo_registro = {"data": data_hora, "acao": acao, "item": item, "qtd": qtd}
    historico.append(novo_registro)


def listar_animais():
    if len(animais) == 0:
        console.print("  Nenhum animal cadastrado.")
        return

    tabela = Table(title="Rebanho")
    tabela.add_column("#")
    tabela.add_column("Brinco")
    tabela.add_column("Tipo")
    tabela.add_column("Status")
    tabela.add_column("Peso (kg)")

    i = 0
    while i < len(animais):
        tabela.add_row(str(i), animais[i]["brinco"], animais[i]["tipo"], animais[i]["status"], str(animais[i]["peso"]))
        i = i + 1

    console.print(tabela)


def cadastrar_animal():
    console.print("--- CADASTRAR ANIMAL ---")
    brinco = input("  Brinco/ID: ")

    console.print("  Tipo: 1-Bovino de Leite  2-Caprino  3-Ovino  4-Suino/Leitao")
    op_tipo = input("  Escolha: ")

    if op_tipo == "1":
        tipo = "Bovino de Leite"
    elif op_tipo == "2":
        tipo = "Caprino"
    elif op_tipo == "3":
        tipo = "Ovino"
    else:
        tipo = "Suino/Leitao"

    console.print("  Status: 1-Em lactacao  2-Para engorda  3-Venda  4-Reprodutor")
    op_status = input("  Escolha: ")

    if op_status == "1":
        status = "Em lactacao"
    elif op_status == "2":
        status = "Para engorda"
    elif op_status == "3":
        status = "Venda"
    else:
        status = "Reprodutor"

    peso = float(input("  Peso (kg): "))

    if brinco == "":
        console.print("  Brinco obrigatorio.")
    else:
        novo_animal = {"brinco": brinco, "tipo": tipo, "status": status, "peso": peso}
        animais.append(novo_animal)
        console.print("  Animal cadastrado!")


def buscar_animal():
    console.print("--- BUSCAR ANIMAL ---")
    termo = input("  Buscar por brinco ou tipo: ")
    termo = termo.lower()

    achou = False

    tabela = Table(title="Resultado da busca")
    tabela.add_column("Brinco")
    tabela.add_column("Tipo")
    tabela.add_column("Status")
    tabela.add_column("Peso (kg)")

    i = 0
    while i < len(animais):
        brinco_lower = animais[i]["brinco"].lower()
        tipo_lower = animais[i]["tipo"].lower()
        if termo in brinco_lower or termo in tipo_lower:
            tabela.add_row(animais[i]["brinco"], animais[i]["tipo"], animais[i]["status"], str(animais[i]["peso"]))
            achou = True
        i = i + 1

    if achou:
        console.print(tabela)
    else:
        console.print("  Nenhum animal encontrado.")


def atualizar_status_animal():
    console.print("--- ATUALIZAR STATUS ---")
    listar_animais()

    indice = int(input("  Numero do animal: "))

    if indice >= 0 and indice < len(animais):
        console.print("  Novo status: 1-Em lactacao  2-Para engorda  3-Venda  4-Reprodutor")
        op_st = input("  Escolha: ")

        if op_st == "1":
            animais[indice]["status"] = "Em lactacao"
        elif op_st == "2":
            animais[indice]["status"] = "Para engorda"
        elif op_st == "3":
            animais[indice]["status"] = "Venda"
        else:
            animais[indice]["status"] = "Reprodutor"

        console.print("  Status atualizado!")
    else:
        console.print("  Numero invalido.")


def remover_animal():
    console.print("--- REMOVER ANIMAL ---")
    listar_animais()

    indice = int(input("  Numero do animal a remover: "))

    if indice >= 0 and indice < len(animais):
        confirmacao = input("  Confirma remocao? (s/n): ")
        if confirmacao == "s":
            animal_removido = animais.pop(indice)
            console.print("  Animal " + animal_removido["brinco"] + " removido.")
        else:
            console.print("  Cancelado.")
    else:
        console.print("  Numero invalido.")


def registrar_ordenha():
    console.print("--- REGISTRAR ORDENHA ---")
    data_ord = input("  Data (DD/MM/AAAA): ")
    litros = float(input("  Litros ordenhados: "))
    valor_litro = float(input("  Valor por litro R$: "))

    if litros > 0 and valor_litro > 0:
        nova_ordenha = {"data": data_ord, "litros": litros, "valor_litro": valor_litro}
        ordenhas.append(nova_ordenha)
        total = litros * valor_litro
        registrar_historico("producao", "Leite", litros)
        console.print("  Ordenha registrada! Total: R$ " + str(round(total, 2)))
    else:
        console.print("  Valores invalidos.")


def listar_ordenhas():
    if len(ordenhas) == 0:
        console.print("  Nenhuma ordenha registrada.")
        return

    tabela = Table(title="Historico de Ordenhas")
    tabela.add_column("Data")
    tabela.add_column("Litros")
    tabela.add_column("Valor/L")
    tabela.add_column("Total")

    total_litros = 0.0
    i = 0
    while i < len(ordenhas):
        total_ord = ordenhas[i]["litros"] * ordenhas[i]["valor_litro"]
        tabela.add_row(ordenhas[i]["data"], str(ordenhas[i]["litros"]), "R$ " + str(ordenhas[i]["valor_litro"]), "R$ " + str(round(total_ord, 2)))
        total_litros = total_litros + ordenhas[i]["litros"]
        i = i + 1

    console.print(tabela)
    console.print("  Total geral: " + str(total_litros) + " litros")


def adicionar_produto_estoque():
    console.print("--- ADICIONAR PRODUTO AO ESTOQUE ---")
    nome_prod = input("  Nome do produto (ex: Queijo Coalho): ")
    qtd = float(input("  Quantidade (kg): "))
    preco = float(input("  Preco de venda R$/kg: "))

    if qtd > 0 and preco > 0 and nome_prod != "":
        achou_prod = False
        i = 0
        while i < len(estoque):
            if estoque[i]["produto"] == nome_prod:
                estoque[i]["qtd"] = estoque[i]["qtd"] + qtd
                estoque[i]["preco"] = preco
                achou_prod = True
                registrar_historico("producao", nome_prod, qtd)
                console.print("  Estoque atualizado! Nova qtd: " + str(estoque[i]["qtd"]))
            i = i + 1

        if not achou_prod:
            novo_produto = {"produto": nome_prod, "qtd": qtd, "preco": preco}
            estoque.append(novo_produto)
            registrar_historico("producao", nome_prod, qtd)
            console.print("  Produto adicionado ao estoque!")
    else:
        console.print("  Dados invalidos.")


def listar_estoque():
    if len(estoque) == 0:
        console.print("  Estoque vazio.")
        return

    tabela = Table(title="Estoque Atual")
    tabela.add_column("Produto")
    tabela.add_column("Qtd (kg)")
    tabela.add_column("Preco/kg")
    tabela.add_column("Total")

    i = 0
    while i < len(estoque):
        total_item = estoque[i]["qtd"] * estoque[i]["preco"]
        tabela.add_row(estoque[i]["produto"], str(estoque[i]["qtd"]), "R$ " + str(estoque[i]["preco"]), "R$ " + str(round(total_item, 2)))
        i = i + 1

    console.print(tabela)


def relatorio_geral():
    console.print("=== RELATORIO GERAL DA FAZENDA ===")

    contagem_tipos = {}
    i = 0
    while i < len(animais):
        tipo = animais[i]["tipo"]
        if tipo in contagem_tipos:
            contagem_tipos[tipo] = contagem_tipos[tipo] + 1
        else:
            contagem_tipos[tipo] = 1
        i = i + 1

    tabela_animais = Table(title="Rebanho por Tipo")
    tabela_animais.add_column("Tipo")
    tabela_animais.add_column("Quantidade")

    for tipo in contagem_tipos:
        tabela_animais.add_row(tipo, str(contagem_tipos[tipo]))

    console.print(tabela_animais)

    total_litros = 0.0
    i = 0
    while i < len(ordenhas):
        total_litros = total_litros + ordenhas[i]["litros"]
        i = i + 1

    console.print("Total de litros de leite registrados: " + str(total_litros) + " L")

    listar_estoque()

    if len(vendas) == 0:
        console.print("  Nenhuma venda registrada ainda.")
    else:
        total_vendas = 0.0
        i = 0
        while i < len(vendas):
            total_vendas = total_vendas + vendas[i]["total"]
            i = i + 1

        console.print("Total arrecadado em vendas: R$ " + str(round(total_vendas, 2)))

        if total_vendas >= 1000:
            console.print("  Status: BOM desempenho!")
        else:
            console.print("  Status: Continue vendendo!")


def listar_historico():
    if len(historico) == 0:
        console.print("  Nenhuma movimentacao registrada.")
        return

    tabela = Table(title="Historico de Movimentacao")
    tabela.add_column("Data")
    tabela.add_column("Acao")
    tabela.add_column("Item")
    tabela.add_column("Qtd")

    i = 0
    while i < len(historico):
        tabela.add_row(historico[i]["data"], historico[i]["acao"], historico[i]["item"], str(historico[i]["qtd"]))
        i = i + 1

    console.print(tabela)