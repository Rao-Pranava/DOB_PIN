import os
import re
from tqdm import tqdm
import time
from itertools import permutations
from itertools import combinations


def print_banner():
    # Clear Terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    width = 50

    print("=" * width)
    print("PIN Combination Generator".center(width))
    print("=" * width)
    print("Version : 1.0 - Generate PIN using DOB".center(width))
    print("Author: Pranava Rao & ChatGPT ;)".center(width))
    print("=" * width)
    print()

def get_inputs():
    
    inputs = []

    # Get number of inputs
    while True:
        try:
            count = int(input("Number of Inputs DOBs : "))

            if count <= 0:
                print("Please enter a number greater than zero.\n")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a whole number.\n")

    print()

    # Collect each input
    for i in range(1, count + 1):

        while True:

            value = input(f"Input DOB of {i} : ").strip()

            # Remove everything except digits
            cleaned = re.sub(r"\D", "", value)

            if len(cleaned) != 8:
                print("Invalid input! Please enter exactly 8 digits (DDMMYYYY).\n")
                continue

            inputs.append(cleaned)
            break

    return inputs


def build_pool(inputs):
    
    pool = set()

    for number in inputs:

        length = len(number)

        # Generate every substring from 2 digits up to full length
        for substring_length in range(2, length + 1):

            for start in range(length - substring_length + 1):

                substring = number[start:start + substring_length]
                pool.add(substring)

    pool = sorted(
        pool,
        key=lambda x: (len(x), x)
    )

    print("\n" + "=" * 50)
    print("Pool Generated")
    print("=" * 50)
    print(f"Unique Pool Entries : {len(pool)}")
    print("=" * 50)

    return pool

def generate_combinations(
    pool,
    output_length,
    permutation_mode="permutation",
    remove_leading_zeros=False
):
 
    results = set()
    duplicate_count = 0

    progress = tqdm(
        desc="Building combinations",
        dynamic_ncols=True,
        unit=" combo"
    )

    def process(candidate):

        nonlocal duplicate_count

        if remove_leading_zeros:
            candidate = candidate.lstrip("0")

            if candidate == "":
                return

        generated = set()

        if permutation_mode == "none":

            generated.add(candidate)

        elif permutation_mode == "rotation":

            for i in range(len(candidate)):
                generated.add(candidate[i:] + candidate[:i])

        elif permutation_mode == "permutation":

            for p in permutations(candidate):
                generated.add("".join(p))

        for value in generated:

            if remove_leading_zeros:
                value = value.lstrip("0")

                if value == "":
                    continue

            if value in results:
                duplicate_count += 1
            else:
                results.add(value)

        progress.update(1)

    def backtrack(current):

        if len(current) >= output_length:

            process(current[:output_length])
            return

        for item in pool:
            backtrack(current + item)

    for item in pool:
        backtrack(item)

    progress.close()

    return sorted(results), duplicate_count

def save_results(results, output_length):
    
    print("\n" + "-" * 50)
    print("Output File")
    print("-" * 50)

    default_filename = f"Combination_{output_length}_Digits.txt"

    filename = input(
        f"Default: {default_filename}\nFilename (Press Enter for default): "
    ).strip()

    if filename == "":
        filename = default_filename

    # Add .txt if omitted
    if not filename.lower().endswith(".txt"):
        filename += ".txt"

    total_saved = 0

    with open(filename, "w", encoding="utf-8") as file:

        for value in sorted(results):
            file.write(f"{value}\n")
            total_saved += 1

    return filename, total_saved

def print_summary(total_generated,
                  duplicates_removed,
                  filename,
                  output_length,
                  pool_size,
                  execution_time=None):
    
    width = 60

    print("\n" + "=" * width)
    print("GENERATION SUMMARY".center(width))
    print("=" * width)

    print(f"{'✓ Status':30}: Completed Successfully")
    print(f"{'Pool Size':30}: {pool_size}")
    print(f"{'Output Length':30}: {output_length} digits")
    print(f"{'Unique Combinations':30}: {total_generated:,}")
    print(f"{'Duplicates Removed':30}: {duplicates_removed:,}")
    print(f"{'Output File':30}: {filename}")

    if execution_time is not None:
        print(f"{'Execution Time':30}: {execution_time:.2f} seconds")

    print("=" * width)
def main():

    # Display Banner
    print_banner()

    # Collect User Inputs
    inputs = get_inputs()

    # Build Number Pool
    pool = build_pool(inputs)

    print("\n" + "-" * 50)

    # Get Output Length
    while True:
        try:
            output_length = input(
                "Output Length (2-16) [Default: 4]: "
            ).strip()

            if output_length == "":
                output_length = 4
            else:
                output_length = int(output_length)

            if 2 <= output_length <= 16:
                break

            print("Please enter a value between 2 and 16.")

        except ValueError:
            print("Please enter a valid number.")

    print()

    # Remove Leading Zeros
    remove_leading_zeros = (
        input("Remove leading zeros? (y/N): ")
        .strip()
        .lower() == "y"
    )

    print()

    # ----------------------------------------
    # Permutation Mode
    # ----------------------------------------

    print("=" * 50)
    print("Permutation Mode")
    print("=" * 50)
    print("1. Base Combinations Only")
    print("2. Cyclic Rotations")
    print("3. All Unique Permutations")
    print()

    while True:

        choice = input("Choice [Default: 3]: ").strip()

        if choice == "":
            permutation_mode = "permutation"
            break

        elif choice == "1":
            permutation_mode = "none"
            break

        elif choice == "2":
            permutation_mode = "rotation"
            break

        elif choice == "3":
            permutation_mode = "permutation"
            break

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

    print()

    # ----------------------------------------
    # Start Timer
    # ----------------------------------------

    start_time = time.perf_counter()

    # Generate Combinations

    results, duplicates_removed = generate_combinations(
        pool=pool,
        output_length=output_length,
        permutation_mode=permutation_mode,
        remove_leading_zeros=remove_leading_zeros
    )

    # Save Results

    filename, total_saved = save_results(
        results,
        output_length
    )

    # Stop Timer

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Print Summary

    print_summary(
        total_generated=total_saved,
        duplicates_removed=duplicates_removed,
        filename=filename,
        output_length=output_length,
        pool_size=len(pool),
        execution_time=execution_time
    )

if __name__ == "__main__":
    main()
