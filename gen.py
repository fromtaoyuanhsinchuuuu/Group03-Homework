import os
import random

# Function to calculate hash based on the description
def calculate_hash(data, nonce):
    H = 0
    for idx, d in enumerate(data + [nonce], start=1):
        if idx % 25 == 0:
            H = ((H ^ d) << 1) % (2 ** 30)
        else:
            H = (H ^ d) % (2 ** 30)
    return H

# Generate block content
def generate_block(prev_hash, data_count, nonce_range):
    data = [random.randint(1, 2 ** 30) for _ in range(data_count)]
    nonce = random.randint(*nonce_range)
    block_hash = calculate_hash(data, nonce)
    return {
        "prev_hash": prev_hash,
        "data": data,
        "nonce": nonce,
        "hash": block_hash
    }

# Main generator function
def generate_test_case(input_file):
    # Read the number of blocks and block file names from the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    num_blocks = int(lines[0].strip())
    block_files = [line.strip() for line in lines[1:]]
    
    # Ensure the input file's block count matches the specified number
    if len(block_files) != num_blocks:
        raise ValueError(f"Input file {input_file} specifies {num_blocks} blocks, but lists {len(block_files)} filenames.")
    
    # Determine the number of data entries per block based on the input file name
    if int(input_file.split('.')[0]) <= 6:  # For 2.in to 6.in
        data_count_range = (1, 24)
    else:  # For 7.in to 11.in
        data_count_range = (25, 1000)
    
    # Generate blocks
    prev_hash = 0
    for i, block_file in enumerate(block_files):
        # Determine the number of data entries in the block
        data_count = random.randint(*data_count_range)
        
        # Last block always has nonce = 0
        nonce_range = (1, 2 ** 30) if i < len(block_files) - 1 else (0, 0)
        
        # Generate block content
        block = generate_block(prev_hash, data_count, nonce_range)
        
        # Write block to file
        with open(block_file, 'w') as f:
            f.write(f"P: {prev_hash}\n")
            for idx, d in enumerate(block["data"], start=1):
                f.write(f"{idx}: {d}\n")
            f.write(f"N: {block['nonce']}\n")
        
        # Update prev_hash for the next block
        prev_hash = block["hash"]

# Generate test cases for 2.in to 11.in
for i in range(2, 12):
    input_file = f"{i}.in"
    print(f"Generating blocks for {input_file}...")
    generate_test_case(input_file)
