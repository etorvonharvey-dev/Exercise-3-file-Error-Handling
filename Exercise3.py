def save_user(username, age):
    try:
        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")
    except Exception as e:
        print("Error saving file:", e)


def display_users():
    try:
        with open("users.txt", "r") as file:
            print("\nSaved Users:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No users found yet.")


def main():
    try:
        username = input("Enter username: ").strip()
        if not username:
            raise ValueError("Username cannot be empty.")

        age = int(input("Enter age: "))
        if age <= 0:
            raise ValueError("Age must be positive.")

        save_user(username, age)

    except ValueError as ve:
        print("Input Error:", ve)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        display_users()
        print("\nSystem complete.")


if __name__ == "__main__":
    main()