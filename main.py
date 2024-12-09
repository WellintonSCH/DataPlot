import csv
import numpy as np
import plt

def has_header(first_row): 
    if all(c.isdigit() for c in first_row):
        return False
    else: 
        return True

def read_csv(file_name):
    try:
        with open(file_name, 'r', newline='') as file: 
            reader = csv.reader(file)
            data = list(reader)
            first_row = data[0]
            if has_header(first_row):
                header = data[0]
                values = np.array(data[1:], dtype=float).T
            else:
                header = None
                lines = np.array(data, dtype=float).T
        return header, values
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None, None

def main():
    while True:
        file_name = input("Digite o nome do arquivo CSV ou 'sair' para encerrar: ").strip()
        if file_name.lower() == 'sair':
            print("Encerrando o programa.")
            break
        
        headers, values = read_csv(file_name)
        if headers is None and values is None:
            print("Por favor, tente novamente.")
            continue

        x, y = values[0], values[1]

        while True:
            print("\nSelecione uma operação:")
            print("1 - Mostrar gráfico dos dados")
            print("2 - Interpolação e gráfico")
            print("3 - Derivada da interpolação")
            print("4 - Integral da interpolação")
            print("5 - Sair")
            choice = input("Opção: ")

            if choice == "1":
                title = input("Título do gráfico: ")
                x_label = input("Título do eixo x: ")
                y_label = input("Título do eixo y: ")
                try:
                    plt.plot_data(x, y, title, x_label, y_label)
                except Exception as e:
                    print(f"Erro ao calcular: {e}")

            elif choice == "2":
                title = input("Título do gráfico: ")
                x_label = input("Título do eixo x: ")
                y_label = input("Título do eixo y: ")
                try:
                    poly = plt.plot_interpolation(x, y, title, x_label, y_label)
                except Exception as e:
                    print(f"Erro ao calcular: {e}")

            elif choice == "3":
                title = input("Título do gráfico: ")
                x_label = input("Título do eixo x: ")
                y_label = input("Título do eixo y: ")
                try:
                    plt.plot_derivative(poly, x, title, x_label, y_label)
                except Exception as e:
                    print(f"Erro ao calcular: {e}")

            elif choice == "4":
                try:
                    a = float(input("Valor inicial: "))
                    b = float(input("Valor final: "))
                
                    result = plt.calculate_integral(poly, a, b)
                    print(f"A integral de {a} a {b} é: {result}")
                except Exception as e:
                    print(f"Erro ao calcular: {e}")

            elif choice == "5":
                print("Encerrando...")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    main()
