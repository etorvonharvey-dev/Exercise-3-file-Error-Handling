def main():
    try:
        username = input("Enter Username: ")
        age = int(input("Enter Age: "))
        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")
        
        print("\nData saved successfully!")

    except ValueError:
        print("\nError: Please enter a valid numerical value for Age.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

    else:
        print("\n--- Saved Users ---")
        try:
            with open("users.txt", "r") as file:
                content = file.read()
                print(content if content else "No data found in file.")
        except FileNotFoundError:
            print("No file found yet. Save a user first.")

    finally:
        print("\nSystem complete.")

if __name__ == "__main__":
    main()