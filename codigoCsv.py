import pandas as pd

def convert_date(data):
    try:
        formatted_date = pd.to_datetime(data, format='%d/%m/%Y').strftime('%Y-%m-%d')
        return formatted_date
    except ValueError:
        return data  # Return the original date if it cannot be converted

input_csv = "REGISTRO_ALERTASPLD.csv"

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
