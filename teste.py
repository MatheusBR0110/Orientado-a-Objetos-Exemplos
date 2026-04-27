numero_da_conta = 5420
titular = "Matheus"
saldo = 50
limite = 300

conta = {"numero":5420, "titular":"Matheus",
         "saldo":50, "limite":300
}

print(conta["titular"])
print(conta["limite"])

def criar_conta(numero_da_conta,titular,saldo,limite):
    conta = {"numero":numero_da_conta, "titular":titular,
         "saldo":saldo, "limite":limite
}
    return conta

conta = criar_conta(459, "Gustavo", 500.0, 2500.0)
print(conta["limite"])

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f"Seu saldo atual é {conta["saldo"]}")

sacar(conta, 50)
extrato(conta)
depositar(conta, 200)
extrato(conta)
