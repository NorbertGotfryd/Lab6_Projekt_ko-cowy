import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            print("Loaded JSON data successfully.")
            return data
        except json.JSONDecodeError as e:
            print(f'Error loading JSON: {e}')
            return None

if __name__ == '__main__':
    args = parse_arguments()
    data = load_json(args.input_file)
    if data:
        print(data)
