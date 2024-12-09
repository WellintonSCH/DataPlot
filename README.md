# Processamento de Dados com Interpolação, Derivada e Integral

Este projeto foi desenvolvido como um trabalho acadêmico no curso de **Ciências da Computação** da UTFPR Santa Helena, com o objetivo de processar dados de um arquivo CSV, realizando interpolação, cálculo de derivada e integral, e plotando os resultados.

## Funcionalidades

- **Carregamento de dados**: Recebe um arquivo CSV com duas colunas representando os dados de entrada.
- **Interpolação**: Gera uma função contínua que ajusta os pontos fornecidos.
- **Derivada**: Calcula a derivada da função interpolada.
- **Integral**: Calcula a integral da função interpolada no intervalo definido.
- **Visualização gráfica**: Plota os dados originais, a interpolação, a derivada e a integral em gráficos.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas principais**:
  - `numpy` para operações matemáticas.
  - `scipy` para interpolação e cálculo da integral.
  - `matplotlib` para geração de gráficos.

## Como Executar

1. *Clone o repositório*:
 ```
 git clone https://github.com/WellintonSCH/DataPlot.git
 ```
   
2. *Instale as dependências*:
```
  pip install -r requirements.txt
```
   
3. *Gere dados de teste: Execute o script que cria um arquivo CSV de exemplo*:
```
Copiar código
python generate_test_data.py
```

4. *Execute o script principal: Use o arquivo gerado ou forneça o seu arquivo CSV*:
```
  Copiar código
  python main.py
```

5. *Veja os gráficos: O programa exibirá gráficos com os resultados da interpolação, derivada e integral*.

# Contribuição #
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

# Licença #
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

Autor: Wellinton Schweitzer
Contato: schweitzerwellinton@gmail.com
