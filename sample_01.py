def print_pattern(n):
    for i in range(n):
        print(f"Outer loop: {i}")
        for j in range(n):
            print(f"Inner loop: {j}")

def main():
    print("Starting the program...")
    n = 3
    print_pattern(n)
    print("Program completed.")

if __name__ == "__main__":
    main()
