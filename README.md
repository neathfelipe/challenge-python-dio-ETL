# Conversor de Moedas para Excel

Este é um programa Python simples que permite aos usuários converter um valor em Real Brasileiro (BRL) para uma moeda estrangeira e salvar os resultados em um arquivo Excel (.xlsx). O programa utiliza a API "AwesomeAPI" para obter as taxas de câmbio atualizadas.

## Pré-requisitos

Antes de executar este programa, você deve garantir que o Python esteja instalado em seu sistema. Além disso, você precisa instalar as seguintes bibliotecas usando o pip:

```
pip install openpyxl requests
```

## Como Usar

1. Execute o programa digitando `python seu_programa.py` no terminal.

2. Você será solicitado a inserir seu nome, um valor em Reais (BRL) e a moeda de destino para a conversão.

3. O programa usará a API "AwesomeAPI" para obter a taxa de câmbio atualizada para a moeda de destino e calculará o valor convertido.

4. Os resultados, incluindo seu nome, o valor em Reais, a moeda de destino, a taxa de câmbio e o valor convertido, serão registrados em um arquivo Excel com o nome do usuário (por exemplo, `usuario.xlsx`). Se o arquivo já existir, os dados serão adicionados como uma nova linha na planilha existente. Caso contrário, um novo arquivo Excel será criado.

5. O programa exibirá uma mensagem indicando onde os dados foram salvos.

## Exemplo de Uso

```
Digite seu nome: Felipe
Qual valor você quer saber a conversão para Real Brasileiro: 100
DIGITE A MOEDA QUE VOCÊ DESEJA CONVERTER
[USD]    Dólar Americano/Real Brasileiro
[CAD]    Dólar Canadense/Real Brasileiro
[GBP]    Libra Esterlina/Real Brasileiro
[ARS]    Peso Argentino/Real Brasileiro
[EUR]    Euro/Real Brasileiro
[JPY]    Iene Japonês/Real Brasileiro
=> USD
Olá Felipe, a sua quantia de R$100.0 convertida para USD é de 18.64

Os dados foram adicionados em Felipe.xlsx.
```

## Autor

Felipe Rodrigues 
