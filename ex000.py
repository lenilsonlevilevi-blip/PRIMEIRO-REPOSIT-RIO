# CONTROLE DE GASTOS BÁSICO
import sqlite3

# conectar ao banco
conexao = sqlite3.connect("gastos.db")

# criar cursor
cursor = conexao.cursor()

# criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS gastos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    valor REAL
)
""")

conexao.commit()

while True:
    print("--------CONTROLE DE GASTOS--------")
    print("1 - adicionar gasto:")
    print("2 - ver gastos:")
    print("3 - ver total de gastos:")
    print("4 - sair do programa:")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do gasto: ")
        valor = float(input("Digite o valor do gasto: "))

        cursor.execute(
            "INSERT INTO gastos (nome, valor) VALUES (?, ?)",
            (nome, valor)
        )

        conexao.commit()
        print("Gasto adicionado com sucesso!")

    elif opcao == "2":
        cursor.execute("SELECT nome, valor FROM gastos")
        gastos = cursor.fetchall()

        if len(gastos) == 0:
            print("Nenhum gasto encontrado")
        else:
            print("\nLista de gastos:")
            for gasto in gastos:
                print(gasto[0], "- R$", gasto[1])

    elif opcao == "3":
        cursor.execute("SELECT SUM(valor) FROM gastos")
        total = cursor.fetchone()[0]

        if total is None:
            total = 0

        print("Total de gastos: R$", total)

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida")



