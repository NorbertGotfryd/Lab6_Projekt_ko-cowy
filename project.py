def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        print(f'Saved data to {file_path}')

if __name__ == '__main__':
    args = parse_arguments()
    data = load_json(args.input_file)
    if data:
        save_json(data, args.output_file)
