import pandas as pd

def convert_date(data):
    try:
        formatted_date = pd.to_datetime(data, format='%d/%m/%Y').strftime('%Y-%m-%d')
        return formatted_date
    except ValueError:
        return data  # Retorna a data original se não puder ser convertida

input_csv = "REGISTRO_ALERTASPLD.csv"

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

        output_txt = "teste_cleanedfinal.txt"
        try:
            df.to_csv(output_txt, sep="|", encoding="utf-8", index=False)
            print(f"{output_txt} foi salvo com sucesso com o delimitador '|'.")
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")

except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
