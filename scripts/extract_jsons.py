import json

def extract_dicts_by_prompt(json_file, prompt_file, output_file):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)  # Assumes the JSON file contains a list of dictionaries

    # Load the prompts from the text file
    with open(prompt_file, 'r') as f:
        prompts = [line.strip() for line in f]  # Remove any leading/trailing whitespace

    # Extract dictionaries with matching prompt_en
    extracted_dicts = [d for d in data if d.get('prompt_en') in prompts]

    # Save the extracted dictionaries to a new JSON file as a list of dicts
    with open(output_file, 'w') as f:
        json.dump(extracted_dicts, f, indent=4)  # Save with pretty-printing

    print(f"Extracted {len(extracted_dicts)} dictionaries to {output_file}")

# Example usage
json_file = '/home/yfeng/ygcheng/src/VBench/vbench/VBench_full_info.json'  # Path to the JSON file
prompt_file = '/home/yfeng/ygcheng/src/VBench/prompts/vbench_50/extracted_prompts_50.txt'  # Path to the text file with prompts
output_file = '/home/yfeng/ygcheng/src/VBench/prompts/vbench_50/extracted_prompts_50.json'  # Path to the output JSON file

extract_dicts_by_prompt(json_file, prompt_file, output_file)