# Portfólio de Projetos

## Sobre Mim
Olá, senhoras e senhores! 
Sou o Douglas, um desenvolvedor dedicado a criar soluções inovadoras. Este repositório apresenta dois dos meus projetos recentes, cujo objetivo é criar arquivos dentro do padrão aceito pela B3, tanto em .csv quanto em .txt. Abaixo, descrevo as tecnologias utilizadas e como cada um deles pode ser executado. Sinta-se à vontade para explorar o código e me contatar para qualquer dúvida ou colaboração.

## Projetos

### 1. Projeto: Conversão e Limpeza de Datas em Arquivo .CSV

#### Descrição
Este projeto visa converter datas de um arquivo CSV do formato `dd/mm/yyyy` para o formato `yyyy-mm-dd`, mudar a codificação de UTF-16 para UTF-8, mudar o delimitador de "," para ";" e salvar o arquivo processado em um novo CSV. O código lê o arquivo CSV de entrada, converte as datas e salva o resultado em um arquivo CSV de saída com um delimitador e codificação específicos.

#### Tecnologias Utilizadas
- Python
- Pandas

#### Funcionalidades
- Conversão de datas de `dd/mm/yyyy` para `yyyy-mm-dd`
- Leitura de arquivos CSV com codificação UTF-16
- Salvamento de arquivos CSV com codificação UTF-8 e delimitador `;`

#### Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/douglassilvaf/conversor-Planilhas.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd conversor-Planilhas
   ```

3. Instale as dependências:
   ```bash
   pip install pandas
   ```

4. Execute o script Python:
   ```bash
   python converter_data.py
   ```

#### Código
```python
import pandas as pd

def convert_date(data):
    try:
        formatted_date = pd.to_datetime(data, format='%d/%m/%Y').strftime('%Y-%m-%d')
        return formatted_date
    except ValueError:
        return data  # Return the original date if it cannot be converted

input_csv = "Exemplo.csv"

try:
    df = pd.read_csv(input_csv, sep="\t", encoding="utf-16")  # Specify UTF-16 encoding
    if df.empty:
        print("The DataFrame is empty after reading the file.")
    else:
        print("File read successfully:")
        print(df.head())

        date_column_list = [col for col in df.columns if "Data" in col]
        for col in date_column_list:
            df[col] = df[col].apply(convert_date)

        output_csv = "teste_cleaned.csv"
        try:
            df.to_csv(output_csv, sep=";", encoding="utf-8", index=False)
            print(f"{output_csv} was successfully saved with ';' as delimiter.")
        except Exception as e:
            print(f"Error saving the file: {e}")

except Exception as e:
    print(f"Error reading the file: {e}")
```

### 2. Projeto: Conversão e Salvamento de Dados de Arquivo .CSV para .TXT

#### Descrição
Este projeto visa ler um arquivo CSV com codificação UTF-16, converter as datas no formato `dd/mm/yyyy` para `yyyy-mm-dd`, e salvar o resultado em um arquivo .txt com delimitador `|` e codificação UTF-8. O código manipula as colunas de datas especificadas no arquivo de entrada e trata erros de conversão caso as datas não estejam no formato esperado.

#### Tecnologias Utilizadas
- Python
- Pandas

#### Funcionalidades
- Leitura de arquivo CSV com codificação UTF-16
- Conversão de datas de `dd/mm/yyyy` para `yyyy-mm-dd`
- Salvamento de dados em um arquivo .txt com delimitador `|` e codificação UTF-8

#### Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/douglassilvaf/conversor-Planilhas.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd conversor-Planilhas
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install pandas
   ```

4. Execute o script Python:
   ```bash
   python codigoTxt.py
   ```

#### Código
```python
import pandas as pd

def convert_date(data):
    try:
        formatted_date = pd.to_datetime(data, format='%d/%m/%Y').strftime('%Y-%m-%d')
        return formatted_date
    except ValueError:
        return data  # Retorna a data original se não puder ser convertida

input_csv = "TESTE.csv"

try:
    df = pd.read_csv(input_csv, sep="\t", encoding="utf-16")  # Especifica a codificação UTF-16
    if df.empty:
        print("O DataFrame está vazio após a leitura do arquivo.")
    else:
        print("Arquivo lido com sucesso:")
        print(df.head())

        date_column_list = [col for col in df.columns if "Data" in col]
        for col in date_column_list:
            df[col] = df[col].apply(convert_date)

        output_txt = "teste_cleaned.txt"
        try:
            df.to_csv(output_txt, sep="|", encoding="utf-8", index=False)
            print(f"{output_txt} foi salvo com sucesso com o delimitador '|'.")
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")

except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
```

Certifique-se de ajustar conforme necessário para refletir precisamente as especificações e funcionalidades do seu projeto.
