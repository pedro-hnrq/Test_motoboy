class Motoboy:
    def __init__(self, nome, comissao, exclusividade=None):
        self.nome = nome
        self.comissao = comissao
        self.exclusividade = exclusividade


class Loja:
    def __init__(self, nome, pedidos, taxa_comissao, valor_fixo):
        self.nome = nome
        self.pedidos = pedidos
        self.taxa_comissao = taxa_comissao
        self.valor_fixo = valor_fixo
