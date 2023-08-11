class Interface:
    @staticmethod
    def solicitar_motoboy():
        return int(input("Digite um número do Motoboy (1 a 5) ou 0 para sair: "))

    @staticmethod
    def mostrar_resultados(motoboy, ganho, pedidos, loja):
        print(f"Motoboy: {motoboy.nome}")
        print(f"Número de Pedidos: {pedidos}")
        print(f"Loja: {loja}")
        print(f"Ganho Total: R${ganho:.2f}")

    @staticmethod
    def mostrar_mensagem_invalida():
        print("Número inválido. Por favor, digite um número de 1 a 5 ou 0 para sair.")
