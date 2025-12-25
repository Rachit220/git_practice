# File names
input_file = "input.txt"
output_file = "res.txt"

try:
    with open(input_file, "r") as file:
        text = file.read()

        # Count lines
        lines = text.split("\n")
        line_count = len(lines)

        # Count words
        words = text.split()
        word_count = len(words)

        # Count characters
        char_count = len(text)

    # Display results
    print("Lines:", line_count)
    print("Words:", word_count)
    print("Characters:", char_count)

    # Save results to another file
    with open(output_file, "w") as file:
        file.write("Text File Analysis Result\n")
        file.write("-------------------------\n")
        file.write(f"Lines: {line_count}\n")
        file.write(f"Words: {word_count}\n")
        file.write(f"Characters: {char_count}\n")

    print("\nResults saved to", output_file)

except FileNotFoundError:
    print("Input file not found. Please check the file name.")
