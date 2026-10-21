def saque(valor, saldo, limite_credito):
    status = False

    if valor <= saldo:
        saldo = saldo - valor
        status = True
    elif valor <= limite_credito:
        limite_credito = limite_credito - valor
        status = True

    return status, saldo, limite_credito


casos_de_teste = [
    {
        "nome": "Caso 1 - Saque dentro do saldo",
        "valor": 300,
        "saldo": 1000,
        "limite_credito": 500,
        "esperado": (True, 700, 500)
    },
    {
        "nome": "Caso 2 - Saque utilizando o limite de credito",
        "valor": 1200,
        "saldo": 1000,
        "limite_credito": 1500,
        "esperado": (True, 1000, 300)
    },
    {
        "nome": "Caso 3 - Saque acima do saldo e do limite",
        "valor": 1600,
        "saldo": 1000,
        "limite_credito": 500,
        "esperado": (False, 1000, 500)
    }
]

for caso in casos_de_teste:
    resultado = saque(
        caso["valor"],
        caso["saldo"],
        caso["limite_credito"]
    )

    print(caso["nome"])
    print("Valor do saque:", caso["valor"])
    print("Saldo inicial:", caso["saldo"])
    print("Limite de credito inicial:", caso["limite_credito"])
    print("Resultado esperado:", caso["esperado"])
    print("Resultado obtido:", resultado)
    print("Teste aprovado:", resultado == caso["esperado"])
    print("-" * 45)
