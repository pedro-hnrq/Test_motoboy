from models.models import Motoboy, Loja

def calcular_comissao_adicional(taxa_comissao, pedido):
    return taxa_comissao * pedido if taxa_comissao else 0

def alocar_pedidos(motoboy, lojas):
    total_ganho = 0
    total_pedidos = 0
    loja = None
    
    for l in lojas:
        if motoboy.exclusividade is None or motoboy.exclusividade == l.nome:
            for pedido in l.pedidos:
                valor_pedido = pedido + calcular_comissao_adicional(l.taxa_comissao, pedido) + l.valor_fixo
                
                total_ganho += valor_pedido * motoboy.comissao
                total_pedidos += 1
                loja = l.nome
    
    return total_ganho, total_pedidos, loja
