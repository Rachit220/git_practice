def read_file_safe(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n File Content:\n")
            print(content)

    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")

    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")

    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        print("Read operation completed.\n")


def write_file_safe(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)
            print(f"Data written successfully to '{filename}'")

    except PermissionError:
        print(f"Error: Permission denied to write '{filename}'.")

    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        print("Write operation completed.\n")


def append_file_safe(filename, data):
    try:
        with open(filename, "a") as file:
            file.write(data)
            print(f"Data appended successfully to '{filename}'")

    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")

    except PermissionError:
        print(f"Error: Permission denied to modify '{filename}'.")

    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        print("Append operation completed.\n")
file_name = "example.txt"

write_file_safe(file_name, "Hello, this is safe file handling in Python and my self Rachit.\n")
append_file_safe(file_name, "Appending more content safely and privately.\n")
read_file_safe(file_name)
