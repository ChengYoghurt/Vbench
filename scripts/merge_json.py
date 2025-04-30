import json

def merge_json_files(file1, file2, output_file):
    # Read the first JSON file
    with open(file1, 'r') as f1:
        data1 = json.load(f1)  # Load JSON data from file1

    # Read the second JSON file
    with open(file2, 'r') as f2:
        data2 = json.load(f2)  # Load JSON data from file2

    # Assuming both JSON files have the same structure (e.g., lists or dictionaries)
    # Merge the data
    if isinstance(data1, list) and isinstance(data2, list):
        merged_data = data1 + data2  # Concatenate lists
    elif isinstance(data1, dict) and isinstance(data2, dict):
        merged_data = {**data1, **data2}  # Merge dictionaries
    else:
        raise ValueError("JSON files must be either both lists or both dictionaries.")

    # Write the merged data to a new JSON file
    with open(output_file, 'w') as outfile:
        json.dump(merged_data, outfile, indent=4)  # Write with pretty formatting

    print(f"Merged data saved to {output_file}")

# Example usage
file1 = '/home/yfeng/ygcheng/src/VBench/evaluation_results/results_2025-02-25-22:07:21_full_info.json'  # Path to the first JSON file
file2 = '/home/yfeng/ygcheng/src/VBench/evaluation_results/results_2025-02-26-14:43:47_full_info.json'  # Path to the second JSON file
output_file = '/home/yfeng/ygcheng/src/VBench/evaluation_results/merged_full_info.json'  # Path to the output merged JSON file

merge_json_files(file1, file2, output_file)