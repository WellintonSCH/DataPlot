import csv

# Dados de tempo e km
dados = [
    [0, 0],
    [1, 2.5],
    [2, 4.8],
    [3, 6.2],
    [4, 7.0],
    [5, 7.5],
    [6, 7.8],
    [7, 7.9],
    [8, 7.9],
    [9, 7.7],
    [10, 7.5],
    [11, 7.2],
    [12, 6.8],
    [13, 6.5],
    [14, 6.0],
    [15, 5.5]
]

# Nome do arquivo
arquivo_csv = 'corrida.csv'

# Criação do arquivo CSV
with open(arquivo_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["tempo", "km"])  # Cabeçalhos
    writer.writerows(dados)  # Dados

print(f"Arquivo {arquivo_csv} criado com sucesso!")
