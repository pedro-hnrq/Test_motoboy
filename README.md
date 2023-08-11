# <p align="center">Teste Motoboy e Lojas</p>

### 🎯 Objetivo

<p align="justify">Este repositório contém um código que resolve o seguinte problema: alocar pedidos a motoboys com base em suas comissões e exclusividade de lojas. O objetivo é garantir que os motoboys recebam pedidos de acordo com suas condições e prioridades, evitando que fiquem sem pedidos para coletar.</p>

#### Problema

<p align="justify">Existem 5 motoboys, cada um com diferentes comissões por pedido coletado, e alguns motoboys têm exclusividade com certas lojas para coletas. Além disso, motoboys sem exclusividade podem coletar de todas as lojas. É importante garantir que os motoboys com exclusividade tenham prioridade na alocação de pedidos.</p>

### ✨ Dados do Teste

<p align="justify">Motoboys

   - Moto 1: Comissão - R$2 por entrega | Atende todas as lojas
   - Moto 2: Comissão - R$2 por entrega | Atende todas as lojas
   - Moto 3: Comissão - R$2 por entrega | Atende todas as lojas
   - Moto 4: Comissão - R$2 por entrega | Exclusividade com loja 1
   - Moto 5: Comissão - R$3 por entrega | Atende todas as lojas

Lojas

- Loja 1: 3 pedidos (R$50, R$50, R$50) | Paga 5% do valor do pedido + valor fixo
- Loja 2: 4 pedidos (R$50, R$50, R$50, R$50) | Paga 5% do valor do pedido + valor fixo
- Loja 3: 3 pedidos (R$50, R$50, R$100) | Paga 15% do valor do pedido + valor fixo</p>

#### Código Explicativo

```
Test_motoboy/
│
├── main.py
│
├── models/
│   └── models.py
│
├── data/
│   └── dados.py  
│
├── controllers/
│   └── alocacao_controller.py
│
└── views/
    └── interface.py
```

### 🚀 Execução do Código

#### 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Python (versão 3.10.X)


#### 🛠️ Instalação

Faça o clone do projeto:

Link ssh
```
git clone git@github.com:pedro-hnrq/Test_motoboy.git
```

Após clonar o repositório acesse o diretório
```
cd Test_motoboy
``` 

executa no terminal:

No Unix ou no MacOS, execute:

```bash
python3 main.py
```

No Windows, execute:

```bash
python main.py
```

## Licença
[MIT License](LICENSE)
