usuarios = [
    ["admin",    "admin123",   "ADM"],
    ["cliente1", "cliente123", "CLIENTE"],
]

animais = [
    ["BOV-001", "Bovino de Leite", "Em lactacao", 420.0],
    ["CAP-001", "Caprino",         "Em lactacao",  45.0],
    ["SUI-001", "Suino/Leitao",    "Venda",        35.0],
]

estoque = [
    ["Queijo Coalho",   100.0, 32.00],
    ["Queijo Manteiga",  40.0, 55.00],
]

ordenhas = [
    ["12/05/2025", 180.0, 2.80],
    ["13/05/2025", 165.0, 2.80],
]

vendas = []
agendamentos = []

usuario_logado = ""
perfil_logado  = ""

rodando = True

while rodando:

    print("============================================")
    print("   FAZENDA SERTAO - Sistema de Gestao")
    print("============================================")

    if usuario_logado == "":
        print("  Voce nao esta logado.")
        print("  1 - Fazer login")
        print("  2 - Cadastrar usuario")
        print("  0 - Sair")
    elif perfil_logado == "ADM":
        print("  Logado como ADM:", usuario_logado)
        print("  1 - Gerenciar Rebanho")
        print("  2 - Producao e Estoque")
        print("  3 - Relatorio de vendas")
        print("  0 - Logout")
    else:
        print("  Logado como CLIENTE:", usuario_logado)
        print("  1 - Ver estoque e comprar")
        print("  2 - Agendar retirada")
        print("  3 - Calcular frete")
        print("  0 - Logout")

    print("--------------------------------------------")
    opcao = input("  Opcao: ")

    if usuario_logado == "":

        if opcao == "1":
            print("--------------------------------------------")
            print("  LOGIN")
            print("--------------------------------------------")
            login = input("  Usuario: ")
            senha = input("  Senha  : ")

            encontrado = False
            i = 0
            while i < len(usuarios):
                if usuarios[i][0] == login and usuarios[i][1] == senha:
                    encontrado     = True
                    usuario_logado = usuarios[i][0]
                    perfil_logado  = usuarios[i][2]
                i = i + 1

            if encontrado:
                print("  Bem-vindo,", usuario_logado, "! Perfil:", perfil_logado)
            else:
                print("  Usuario ou senha incorretos.")

        elif opcao == "2":
            print("--------------------------------------------")
            print("  CADASTRAR USUARIO")
            print("--------------------------------------------")
            novo_login = input("  Novo login : ")
            nova_senha = input("  Nova senha : ")
            print("  Perfil: 1-ADM  2-CLIENTE")
            op_perfil  = input("  Escolha   : ")

            if op_perfil == "1":
                novo_perfil = "ADM"
            else:
                novo_perfil = "CLIENTE"

            ja_existe = False
            i = 0
            while i < len(usuarios):
                if usuarios[i][0] == novo_login:
                    ja_existe = True
                i = i + 1

            if ja_existe:
                print("  Esse login ja existe.")
            elif novo_login == "" or nova_senha == "":
                print("  Login e senha nao podem ser vazios.")
            else:
                usuarios.append([novo_login, nova_senha, novo_perfil])
                print("  Usuario cadastrado com sucesso!")

        elif opcao == "0":
            print("  Encerrando sistema. Ate logo!")
            rodando = False

        else:
            print("  Opcao invalida.")

    elif perfil_logado == "ADM":

        if opcao == "1":

            continuar_rebanho = True
            while continuar_rebanho:

                print("--------------------------------------------")
                print("  GERENCIAR REBANHO")
                print("--------------------------------------------")
                print("  1 - Listar animais")
                print("  2 - Cadastrar animal")
                print("  3 - Buscar animal")
                print("  4 - Atualizar status")
                print("  5 - Remover animal")
                print("  0 - Voltar")
                op_rebanho = input("  Opcao: ")

                if op_rebanho == "1":
                    print("--------------------------------------------")
                    if len(animais) == 0:
                        print("  Nenhum animal cadastrado.")
                    else:
                        i = 0
                        while i < len(animais):
                            print("  [" + str(i) + "]",
                                  animais[i][0], "|",
                                  animais[i][1], "|",
                                  animais[i][2], "|",
                                  animais[i][3], "kg")
                            i = i + 1

                elif op_rebanho == "2":
                    print("--------------------------------------------")
                    brinco = input("  Brinco/ID: ")
                    print("  Tipo: 1-Bovino de Leite  2-Caprino  3-Ovino  4-Suino/Leitao")
                    op_tipo = input("  Escolha: ")
                    if op_tipo == "1":
                        tipo = "Bovino de Leite"
                    elif op_tipo == "2":
                        tipo = "Caprino"
                    elif op_tipo == "3":
                        tipo = "Ovino"
                    else:
                        tipo = "Suino/Leitao"

                    print("  Status: 1-Em lactacao  2-Para engorda  3-Venda  4-Reprodutor")
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
                        print("  Brinco obrigatorio.")
                    else:
                        animais.append([brinco, tipo, status, peso])
                        print("  Animal cadastrado!")

                elif op_rebanho == "3":
                    print("--------------------------------------------")
                    termo = input("  Buscar por brinco ou tipo: ").lower()
                    achou = False
                    i = 0
                    while i < len(animais):
                        brinco_lower = animais[i][0].lower()
                        tipo_lower   = animais[i][1].lower()
                        if termo in brinco_lower or termo in tipo_lower:
                            print("  [" + str(i) + "]",
                                  animais[i][0], "|",
                                  animais[i][1], "|",
                                  animais[i][2], "|",
                                  animais[i][3], "kg")
                            achou = True
                        i = i + 1
                    if not achou:
                        print("  Nenhum animal encontrado.")

                elif op_rebanho == "4":
                    print("--------------------------------------------")
                    i = 0
                    while i < len(animais):
                        print("  [" + str(i) + "]", animais[i][0], "|", animais[i][2])
                        i = i + 1
                    indice = int(input("  Numero do animal: "))
                    if indice >= 0 and indice < len(animais):
                        print("  Novo status: 1-Em lactacao  2-Para engorda  3-Venda  4-Reprodutor")
                        op_st = input("  Escolha: ")
                        if op_st == "1":
                            animais[indice][2] = "Em lactacao"
                        elif op_st == "2":
                            animais[indice][2] = "Para engorda"
                        elif op_st == "3":
                            animais[indice][2] = "Venda"
                        else:
                            animais[indice][2] = "Reprodutor"
                        print("  Status atualizado!")
                    else:
                        print("  Numero invalido.")

                elif op_rebanho == "5":
                    print("--------------------------------------------")
                    i = 0
                    while i < len(animais):
                        print("  [" + str(i) + "]", animais[i][0], "|", animais[i][1])
                        i = i + 1
                    indice = int(input("  Numero do animal a remover: "))
                    if indice >= 0 and indice < len(animais):
                        confirmacao = input("  Confirma remocao? (s/n): ")
                        if confirmacao == "s":
                            animais.pop(indice)
                            print("  Animal removido.")
                        else:
                            print("  Cancelado.")
                    else:
                        print("  Numero invalido.")

                elif op_rebanho == "0":
                    continuar_rebanho = False
                else:
                    print("  Opcao invalida.")

        elif opcao == "2":

            continuar_prod = True
            while continuar_prod:

                print("--------------------------------------------")
                print("  PRODUCAO E ESTOQUE")
                print("--------------------------------------------")
                print("  1 - Registrar ordenha do dia")
                print("  2 - Ver historico de ordenhas")
                print("  3 - Adicionar produto ao estoque")
                print("  4 - Ver estoque atual")
                print("  0 - Voltar")
                op_prod = input("  Opcao: ")

                if op_prod == "1":
                    print("--------------------------------------------")
                    data_ord    = input("  Data (DD/MM/AAAA): ")
                    litros      = float(input("  Litros ordenhados: "))
                    valor_litro = float(input("  Valor por litro R$: "))
                    if litros > 0 and valor_litro > 0:
                        ordenhas.append([data_ord, litros, valor_litro])
                        total = litros * valor_litro
                        print("  Ordenha registrada! Total: R$", round(total, 2))
                    else:
                        print("  Valores invalidos.")

                elif op_prod == "2":
                    print("--------------------------------------------")
                    if len(ordenhas) == 0:
                        print("  Nenhuma ordenha registrada.")
                    else:
                        total_litros = 0.0
                        i = 0
                        while i < len(ordenhas):
                            total_ord = ordenhas[i][1] * ordenhas[i][2]
                            print("  Data:", ordenhas[i][0],
                                  "| Litros:", ordenhas[i][1],
                                  "| Total: R$", round(total_ord, 2))
                            total_litros = total_litros + ordenhas[i][1]
                            i = i + 1
                        print("  Total geral:", total_litros, "litros")

                elif op_prod == "3":
                    print("--------------------------------------------")
                    nome_prod = input("  Nome do produto (ex: Queijo Coalho): ")
                    qtd       = float(input("  Quantidade (kg): "))
                    preco     = float(input("  Preco de venda R$/kg: "))

                    if qtd > 0 and preco > 0 and nome_prod != "":
                        achou_prod = False
                        i = 0
                        while i < len(estoque):
                            if estoque[i][0] == nome_prod:
                                estoque[i][1] = estoque[i][1] + qtd
                                estoque[i][2] = preco
                                achou_prod = True
                                print("  Estoque atualizado! Nova qtd:", estoque[i][1])
                            i = i + 1
                        if not achou_prod:
                            estoque.append([nome_prod, qtd, preco])
                            print("  Produto adicionado ao estoque!")
                    else:
                        print("  Dados invalidos.")

                elif op_prod == "4":
                    print("--------------------------------------------")
                    if len(estoque) == 0:
                        print("  Estoque vazio.")
                    else:
                        i = 0
                        while i < len(estoque):
                            valor_total = estoque[i][1] * estoque[i][2]
                            print("  [" + str(i) + "]",
                                  estoque[i][0], "|",
                                  estoque[i][1], "kg |",
                                  "R$", estoque[i][2], "/kg |",
                                  "Total: R$", round(valor_total, 2))
                            i = i + 1

                elif op_prod == "0":
                    continuar_prod = False
                else:
                    print("  Opcao invalida.")

        elif opcao == "3":
            print("--------------------------------------------")
            print("  RELATORIO DE VENDAS")
            print("--------------------------------------------")
            if len(vendas) == 0:
                print("  Nenhuma venda registrada ainda.")
            else:
                total_geral = 0.0
                i = 0
                while i < len(vendas):
                    print("  Produto:", vendas[i][0],
                          "| Qtd:", vendas[i][1],
                          "| Total: R$", vendas[i][2])
                    total_geral = total_geral + vendas[i][2]
                    i = i + 1
                print("  TOTAL ARRECADADO: R$", round(total_geral, 2))
                if total_geral >= 1000:
                    print("  Status: BOM desempenho!")
                else:
                    print("  Status: Continue vendendo!")

        elif opcao == "0":
            print("  Ate logo,", usuario_logado)
            usuario_logado = ""
            perfil_logado  = ""

        else:
            print("  Opcao invalida.")

    elif perfil_logado == "CLIENTE":

        if opcao == "1":

            continuar_loja = True
            while continuar_loja:

                print("--------------------------------------------")
                print("  LOJA")
                print("--------------------------------------------")
                print("  1 - Ver produtos disponiveis")
                print("  2 - Comprar produto")
                print("  3 - Ver animais para venda")
                print("  0 - Voltar")
                op_loja = input("  Opcao: ")

                if op_loja == "1":
                    print("--------------------------------------------")
                    if len(estoque) == 0:
                        print("  Nenhum produto disponivel.")
                    else:
                        i = 0
                        while i < len(estoque):
                            if estoque[i][1] > 0:
                                print("  [" + str(i) + "]",
                                      estoque[i][0], "|",
                                      estoque[i][1], "kg disponiveis |",
                                      "R$", estoque[i][2], "/kg")
                            i = i + 1

                elif op_loja == "2":
                    print("--------------------------------------------")
                    i = 0
                    while i < len(estoque):
                        if estoque[i][1] > 0:
                            print("  [" + str(i) + "]",
                                  estoque[i][0], "|",
                                  estoque[i][1], "kg |",
                                  "R$", estoque[i][2])
                        i = i + 1

                    indice = int(input("  Numero do produto: "))

                    if indice >= 0 and indice < len(estoque):
                        qtd_compra = float(input("  Quantidade (kg): "))

                        if qtd_compra <= 0:
                            print("  Quantidade invalida.")
                        elif qtd_compra > estoque[indice][1]:
                            print("  Quantidade indisponivel. Temos:", estoque[indice][1], "kg")
                        else:
                            total_compra = qtd_compra * estoque[indice][2]
                            print("  Produto :", estoque[indice][0])
                            print("  Qtd     :", qtd_compra, "kg")
                            print("  Total   : R$", round(total_compra, 2))
                            confirma = input("  Confirmar? (s/n): ")
                            if confirma == "s":
                                estoque[indice][1] = estoque[indice][1] - qtd_compra
                                vendas.append([estoque[indice][0],
                                               qtd_compra,
                                               round(total_compra, 2)])
                                print("  Compra realizada!")
                            else:
                                print("  Cancelado.")
                    else:
                        print("  Numero invalido.")

                elif op_loja == "3":
                    print("--------------------------------------------")
                    tem_animal = False
                    i = 0
                    while i < len(animais):
                        if animais[i][2] == "Venda":
                            print("  [" + str(i) + "]",
                                  animais[i][0], "|",
                                  animais[i][1], "|",
                                  animais[i][3], "kg")
                            tem_animal = True
                        i = i + 1
                    if not tem_animal:
                        print("  Nenhum animal disponivel para venda.")

                elif op_loja == "0":
                    continuar_loja = False
                else:
                    print("  Opcao invalida.")

        elif opcao == "2":
            print("--------------------------------------------")
            print("  AGENDAR RETIRADA")
            print("--------------------------------------------")
            data_ag = input("  Data da retirada (DD/MM/AAAA): ")
            hora_ag = input("  Horario (HH:MM)              : ")
            print("  Tipo: 1-Queijos  2-Leite  3-Animais  4-Misto")
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
                print("  Data e horario sao obrigatorios.")
            else:
                agendamentos.append([usuario_logado, data_ag, hora_ag, tipo_ag])
                print("  Agendamento confirmado!")
                print("  Data:", data_ag, "| Hora:", hora_ag, "| Tipo:", tipo_ag)

        elif opcao == "3":
            print("--------------------------------------------")
            print("  CALCULADORA DE FRETE")
            print("--------------------------------------------")
            distancia = float(input("  Distancia em km ate a fazenda: "))
            print("  Veiculo: 1-Pequeno R$2,50/km  2-Medio R$4,00/km  3-Grande R$6,50/km")
            op_vei = input("  Escolha: ")
            if op_vei == "1":
                preco_km = 2.50
            elif op_vei == "2":
                preco_km = 4.00
            else:
                preco_km = 6.50

            frete = distancia * preco_km
            print("  Distancia :", distancia, "km")
            print("  Frete     : R$", round(frete, 2))
            if frete > 500:
                print("  Aviso: frete alto! Considere consolidar cargas.")

        elif opcao == "0":
            print("  Ate logo,", usuario_logado)
            usuario_logado = ""
            perfil_logado  = ""

        else:
            print("  Opcao invalida.")

    input("\n  [ENTER para continuar]")