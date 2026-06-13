from rich.console import Console

console = Console()

usuarios = [
    {"login": "admin", "senha": "admin123", "perfil": "ADM"},
    {"login": "cliente1", "senha": "cliente123", "perfil": "CLIENTE"},
]


def fazer_login():
    console.print("--- LOGIN ---")
    login = input("  Usuario: ")
    senha = input("  Senha  : ")

    encontrado = False
    usuario_encontrado = None

    i = 0
    while i < len(usuarios):
        if usuarios[i]["login"] == login and usuarios[i]["senha"] == senha:
            encontrado = True
            usuario_encontrado = usuarios[i]
        i = i + 1

    if encontrado:
        console.print("  Bem-vindo, " + usuario_encontrado["login"] + "! Perfil: " + usuario_encontrado["perfil"])
        return usuario_encontrado
    else:
        console.print("  Usuario ou senha incorretos.")
        return None


def cadastrar_usuario():
    console.print("--- CADASTRAR USUARIO ---")
    novo_login = input("  Novo login : ")
    nova_senha = input("  Nova senha : ")
    console.print("  Perfil: 1-ADM  2-CLIENTE")
    op_perfil = input("  Escolha   : ")

    if op_perfil == "1":
        novo_perfil = "ADM"
    else:
        novo_perfil = "CLIENTE"

    ja_existe = False
    i = 0
    while i < len(usuarios):
        if usuarios[i]["login"] == novo_login:
            ja_existe = True
        i = i + 1

    if ja_existe:
        console.print("  Esse login ja existe.")
    elif novo_login == "" or nova_senha == "":
        console.print("  Login e senha nao podem ser vazios.")
    else:
        novo_usuario = {"login": novo_login, "senha": nova_senha, "perfil": novo_perfil}
        usuarios.append(novo_usuario)
        console.print("  Usuario cadastrado com sucesso!")