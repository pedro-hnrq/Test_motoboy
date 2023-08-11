from models.models import Motoboy, Loja

motoboys = [
    Motoboy("Moto 1", 2),
    Motoboy("Moto 2", 2),
    Motoboy("Moto 3", 2),
    Motoboy("Moto 4", 2, "Loja 1"),
    Motoboy("Moto 5", 3)
]

lojas = [
    Loja("Loja 1", [50, 50, 50], 0.05, 0),
    Loja("Loja 2", [50, 50, 50, 50], 0.05, 0),
    Loja("Loja 3", [50, 50, 100], 0.15, 0)
]
