from models.models import Motoboy, Loja

from controllers.alocacao import alocar_pedidos
from views.interface import Interface

from data.dados import motoboys, lojas

interface = Interface()

while True:
    motoboy_escolhido = interface.solicitar_motoboy()
    
    if motoboy_escolhido == 0:
        print("Saindo...")
        break
    elif motoboy_escolhido in range(1, 6):
        motoboy = motoboys[motoboy_escolhido - 1]
        ganho, pedidos, loja = alocar_pedidos(motoboy, lojas)
        
        interface.mostrar_resultados(motoboy, ganho, pedidos, loja)
    else:
        interface.mostrar_mensagem_invalida()
