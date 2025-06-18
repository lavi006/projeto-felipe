# arquivo: contatos.py (VERSÃO MELHORADA)

def exibir_menu():
    print("\n" + "=" * 40)
    print("📒  CADASTRO DE CONTATOS".center(40))
    print("=" * 40)
    print("1️⃣  Adicionar contato")
    print("2️⃣  Listar contatos")
    print("3️⃣  Sair")
    print("=" * 40)
    return input("👉 Escolha uma opção: ")


def adicionar_contato(lista_contatos):
    print("\n" + "-" * 40)
    print("➕  NOVO CONTATO".center(40))
    print("-" * 40)

    nome = input("👤 Nome: ").strip().title()
    telefone = input("📞 Telefone: ").strip()
    email = input("📧 Email: ").strip().lower()

    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }

    lista_contatos.append(contato)
    print(f"\n✅ Contato '{nome}' adicionado com sucesso!")


def listar_contatos(lista_contatos):
    print("\n" + "-" * 50)
    print("📜 LISTA DE CONTATOS".center(50))
    print("-" * 50)

    if not lista_contatos:
        print("📭 Nenhum contato cadastrado ainda.\n")
        return

    for i, contato in enumerate(lista_contatos, 1):
        print(f"{i}. 👤 {contato['nome']}")
        print(f"   📞 Telefone: {contato['telefone']}")
        print(f"   📧 Email: {contato['email']}")
        print("-" * 50)


def main():
    contatos = []

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            adicionar_contato(contatos)
        elif opcao == "2":
            listar_contatos(contatos)
        elif opcao == "3":
            print("\n👋 Obrigado por usar o Cadastro de Contatos! Até logo!\n")
            print("=" * 40)
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()