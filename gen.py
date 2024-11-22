import random

def generate_hash(data, nonce):
    """Custom hash function based on the problem description."""
    hash_value = 0
    for i, d in enumerate(data + [nonce], start=1):
        if i % 25 == 0:
            hash_value = ((hash_value ^ d) << 1) % (2 ** 30)
        else:
            hash_value = (hash_value ^ d) % (2 ** 30)
    return hash_value

def generate_block(file_name, prev_hash, data_count, is_last_block=False, introduce_error=False):
    """Generate a single block file."""
    data = [random.randint(0, 2 ** 30 - 1) for _ in range(data_count)]
    nonce = 0 if is_last_block else random.randint(0, 2 ** 30 - 1)
    hash_value = generate_hash(data, nonce)

    # Introduce an error if required
    if introduce_error:
        if not is_last_block and random.choice([True, False]):
            hash_value = (hash_value + 1) % (2 ** 30)  # Change hash value
        else:
            data[random.randint(0, data_count - 1)] += 1  # Change a data value

    with open(file_name, "w") as f:
        f.write(f"P: {prev_hash}\n")
        for idx, d in enumerate(data, start=1):
            f.write(f"{idx}: {d}\n")
        f.write(f"N: {nonce}\n")
    return hash_value

def generate_testcases(start, end):
    """Generate test cases and write them into .in files."""
    for test_id in range(start, end + 1):
        block_count = random.randint(2, 20) if test_id < 7 else random.randint(2, 20)
        introduce_error_in = random.choice([None, random.randint(1, block_count - 1)])
        with open(f"{test_id}.in", "w") as test_file:
            test_file.write(f"{block_count}\n")
            prev_hash = 0
            for block_num in range(1, block_count + 1):
                file_name = f"block_{test_id}_{block_num}.txt"
                is_last_block = (block_num == block_count)
                introduce_error = (introduce_error_in == block_num)
                prev_hash = generate_block(file_name, prev_hash, random.randint(1, 24 if test_id < 7 else 50), is_last_block, introduce_error)
                test_file.write(file_name + "\n")

# Generate test cases 2.in to 11.in
generate_testcases(2, 11)

