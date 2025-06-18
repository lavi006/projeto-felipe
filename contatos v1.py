# arquivo: contatos.py (VERSÃO 1)

def main():
    print("=== CADASTRO DE CONTATOS ===")
    print("Digite os dados do contato:")

    # Solicitar dados
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    # Exibir dados cadastrados
    print("\n--- CONTATO CADASTRADO ---")
    print(f"Nome: {nome}")
    print(f"Telefone: {telefone}")
    print(f"Email: {email}")
    print("\nContato salvo com sucesso!")


if __name__ == "__main__":
    main()