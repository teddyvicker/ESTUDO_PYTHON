def add_contact(contacts):
    """Adiciona um novo contato à lista de contatos."""
    contact = {}
    contact["nome"] = input("Digite o nome do contato: ")
    contact["telefone"] = input("Digite o telefone do contato: ")
    contact["email"] = input("Digite o email do contato: ")
    contact["favorito"] = False
    contacts.append(contact)

def print_contacts(contacts):
    """Imprime a lista de contatos."""
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['nome']} - {contact['telefone']} - {contact['email']} - Favorito: {contact['favorito']}")

def edit_contact(contacts, index):
    """Edita um contato da lista de contatos."""
    contact = contacts[index]
    contact["nome"] = input("Digite o novo nome do contato: ")
    contact["telefone"] = input("Digite o novo telefone do contato: ")
    contact["email"] = input("Digite o novo email do contato: ")

def toggle_favorite(contacts, index):
    """Marca/desmarca um contato como favorito."""
    contact = contacts[index]
    contact["favorito"] = not contact["favorito"]

def print_favorites(contacts):
    """Imprime a lista de contatos favoritos."""
    for i, contact in enumerate(contacts, 1):
        if contact["favorito"]:
            print(f"{i}. {contact['nome']} - {contact['telefone']} - {contact['email']} - Favorito: {contact['favorito']}")

def remove_contact(contacts, index):
    """Remove um contato da lista de contatos."""
    del contacts[index]

def main():
    """Função principal do programa."""
    contacts = []
    while True:
        print("Escolha uma opção:")
        print("1. Adicionar contato")
        print("2. Visualizar contatos")
        print("3. Editar contato")
        print("4. Marcar/desmarcar contato como favorito")
        print("5. Visualizar contatos favoritos")
        print("6. Apagar contato")
        print("7. Sair")
        option = int(input("Digite a opção: "))
        if option == 1:
            add_contact(contacts)
            print("Contato Add com Sucesso!!")
        elif option == 2:
            print_contacts(contacts)
        elif option == 3:
            index = int(input("Digite o índice do contato a ser editado: ")) - 1
            edit_contact(contacts, index)
        elif option == 4:
            index = int(input("Digite o índice do contato a ser marcado/desmarcado como favorito: ")) - 1
            toggle_favorite(contacts, index)
        elif option == 5:
            print_favorites(contacts)
        elif option == 6:
            index = int(input("Digite o índice do contato a ser apagado: ")) - 1
            remove_contact(contacts, index)
        elif option == 7:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()