# arquivo: contatos.py (VERSÃO 2)

def exibir_menu():
    print("\n=== CADASTRO DE CONTATOS ===")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Sair")
    return input("Escolha uma opção: ")


def adicionar_contato(lista_contatos):
    print("\n--- NOVO CONTATO ---")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }

    lista_contatos.append(contato)
    print(f"\n✅ Contato '{nome}' adicionado com sucesso!")


def listar_contatos(lista_contatos):
    if not lista_contatos:
        print("\n📭 Nenhum contato cadastrado ainda.")
        return

    print(f"\n--- LISTA DE CONTATOS ({len(lista_contatos)} contato(s)) ---")
    for i, contato in enumerate(lista_contatos, 1):
        print(f"\n{i}. {contato['nome']}")
        print(f"   📞 {contato['telefone']}")
        print(f"   📧 {contato['email']}")


def main():
    contatos = []

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            adicionar_contato(contatos)
        elif opcao == "2":
            listar_contatos(contatos)
        elif opcao == "3":
            print("\n👋 Obrigado por usar o Cadastro de Contatos!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()