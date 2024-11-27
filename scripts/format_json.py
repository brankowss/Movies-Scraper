import json

def format_ids(input_file="data/data.json", output_file="data/id.json"):
    try:
        with open(input_file, "r") as file:
            data = json.load(file)
        
        formatted_ids = [entry["id"] for entry in data if "id" in entry]
        
        with open(output_file, "w") as file:
            json.dump(formatted_ids, file, indent=4)
        
        print(f"Formatted IDs saved to {output_file}")
    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except KeyError as e:
        print(f"Error: Missing key {e} in one of the entries.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the input file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

format_ids()