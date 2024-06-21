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
input_csv = "REGISTRO_ALERTASPLD.csv"
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


