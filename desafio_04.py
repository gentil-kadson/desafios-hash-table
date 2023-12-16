usuarios = {}


def cadastrar_usuario(id: int, username: str, password: str) -> None:
    usuarios[id] = {
        "username": username,
        "password": password
    }


def buscar_usuario(id: int) -> str:
    if id in usuarios:
        return f"id: {id} \nusername: {
            usuarios[id]["username"]} \npassword: {usuarios[id]["password"]}\n"
    else:
        return f"Este usuário não está cadastrado.\n"


# exemplo de uso
cadastrar_usuario(1, "Yoshigake Kira", "Baize dosuto")
cadastrar_usuario(10, "Diavolo", "Kingu Kurimuson")

# exemplo de busca
print(buscar_usuario(10))
print(buscar_usuario(1))
print(buscar_usuario(100))
