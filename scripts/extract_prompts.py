def extract_lines(input_file, output_file, step=19):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for i, line in enumerate(infile, start=1):
            if i % step == 0:  # Check if the line number is a multiple of 19
                outfile.write(line)

# Example usage
input_file = '/home/yfeng/ygcheng/src/VBench/prompts/all_dimension.txt'  # Path to the input file
output_file = '/home/yfeng/ygcheng/src/VBench/prompts/vbench_50/extracted_prompts_50.txt'  # Path to the output file

extract_lines(input_file, output_file)
print(f"Extracted lines saved to {output_file}")