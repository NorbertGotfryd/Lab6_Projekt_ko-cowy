import argparse
import json

def parse_arguments():
    parser = argparse.ArgumentParser(description='Data conversion program.')
    parser.add_argument('input_file', type=str, help='Path to the input file.')
    parser.add_argument('output_file', type=str, help='Path to the output file.')
    return parser.parse_args()

def load_json(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            print("Loaded JSON data successfully.")
            return data
        except json.JSONDecodeError as e:
            print(f'Error loading JSON: {e}')
            return None

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        print(f'Saved data to {file_path}')

if __name__ == '__main__':
    args = parse_arguments()
    data = load_json(args.input_file)
    if data:
        save_json(data, args.output_file)
