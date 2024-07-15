Claro, aqui está o README.md atualizado com a descrição de ambos os códigos:

```markdown
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

### 2. Projeto: Leitura e Manipulação de Arquivo .TXT

#### Descrição
Este projeto visa ler um arquivo .txt, tratar possíveis erros de parsing e criar um DataFrame com os dados lidos. O código lida com a leitura de arquivos .txt com codificação UTF-16 e converte-os em um DataFrame, tratando possíveis erros de parsing durante o processo.

#### Tecnologias Utilizadas
- Python
- Pandas

#### Funcionalidades
- Leitura de arquivos .txt com codificação UTF-16
- Tratamento de erros de parsing durante a leitura
- Criação de um DataFrame a partir dos dados lidos

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
   python ler_txt.py
   ```

#### Código
```python
import pandas as pd

# Function to handle parsing errors (replace with your specific logic)
def handle_parsing_error(line):
    try:
        # Replace this with your parsing logic to separate values based on delimiter
        # (';' in this case) and create a dictionary or list as needed
        data_dict = {
            "column1": 'Data Acionamento',  # Replace with actual column names and parsed values
            "column2": 'Data Registro',
            # ... add more key-value pairs for other columns
        }
        return data_dict
    except Exception as e:
        print(f"Error parsing line: {line}")
        # Handle the error (e.g., log, skip row, etc.)
        return None  # Or return a default value (e.g., empty dictionary)

# Read the CSV file
input_csv = "Exemplo.csv"
try:
    # Open the file in read mode with UTF-16 encoding
    with open(input_csv, 'r', encoding="utf-16") as f:
        lines = f.readlines()

        # Skip the header row (optional)
        data = [handle_parsing_error(line) for line in lines[1:]]

    # Create a DataFrame from the parsed data
    if data:  # Check if any data was successfully parsed
        df = pd.DataFrame(data)
    else:
        print("No valid data found in the CSV file.")

    if df.empty:
        print("The DataFrame is empty after parsing.")
    else:
        print("File parsed successfully (with potential errors handled).")
        print(df.head())

except Exception as e:
    print(f"Error reading the file: {e}")
```
