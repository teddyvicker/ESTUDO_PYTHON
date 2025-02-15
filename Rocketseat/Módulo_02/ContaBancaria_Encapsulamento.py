class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado: só pode ser acessado dentro da classe

    def depositar(self, valor):  # Método público para depositar dinheiro
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado. Novo saldo: R${self.__saldo}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):  # Método público para sacar dinheiro
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.__saldo}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def ver_saldo(self):  # Método público para ver o saldo
        print(f"Saldo atual: R${self.__saldo}")

minha_conta = ContaBancaria(1000)  # Cria uma conta com saldo inicial de R$1000

minha_conta.depositar(500)  # Vai mostrar: Depósito de R$500 realizado. Novo saldo: R$1500
minha_conta.sacar(200)  # Vai mostrar: Saque de R$200 realizado. Novo saldo: R$1300

minha_conta.ver_saldo()  # Vai mostrar: Saldo atual: R$1300

print(minha_conta.ver_saldo)  #