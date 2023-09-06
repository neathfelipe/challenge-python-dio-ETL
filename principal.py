import openpyxl
import requests
import os

def adicionar_moeda():
    name = input("Digite seu nome: ")
    real = input("Qual valor você quer saber a conversão para Real Brasileiro: ")
    input_moeda = """\n
    DIGITE A MOEDA QUE VOCÊ DESEJA CONVERTER
    [USD]\tDólar Americano/Real Brasileiro
    [CAD]\tDólar Canadense/Real Brasileiro
    [GBP]\tLibra Esterlina/Real Brasileiro
    [ARS]\tPeso Argentino/Real Brasileiro
    [EUR]\tEuro/Real Brasileiro
    [JPY]\tIene Japonês/Real Brasileiro
    => """
    moeda = input(input_moeda)

    url = 'https://economia.awesomeapi.com.br/json/all'
    response = requests.get(url)
    data = response.json()

    valor_atual_moeda = float(data[moeda]['ask'])
    valor_convertido = round(float(real) / valor_atual_moeda, 2)

    print(f'Olá {name}, a sua quantia de R${real} convertida para {moeda} é de {valor_convertido}')
    info_salva = (name, real, moeda, valor_atual_moeda, valor_convertido,)
    return info_salva

info = adicionar_moeda()

if os.path.isfile(f'{info[0]}.xlsx'): 
  info_list = list(info)
  workbook = openpyxl.load_workbook(f'{info[0]}.xlsx')
  worksheet = workbook.active
  worksheet.append(info_list)
  workbook.save(f'{info[0]}.xlsx')
  print(f'Os dados foram adicionados em {info[0]}.xlsx')
else:
  workbook = openpyxl.Workbook()
  worksheet = workbook.active
  worksheet['A1'] = 'Nome'
  worksheet['B1'] = 'Reais'
  worksheet['C1'] = 'Moeda'
  worksheet['D1'] = 'Cotação'
  worksheet['E1'] = 'Valor Convertido'

  worksheet.append(info)
  workbook.save(f'{info[0]}.xlsx')
  print(f'Os dados foram salvos em {info[0]}.xlsx')
