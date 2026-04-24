try:
    name = input("Enter student name: ")
    score = float(input("Enter score (0-100): "))

    if score < 0 or score > 100:
        print("Error: Score must be between 0 and 100 only.")
    else:
        if score >= 75:
            remarks = "Pass"
        else:
            remarks = "Fail"

        print("\nStudent:", name)
        print("Score:", score)
        print("Remarks:", remarks)

except ValueError:
    print("Error: Please enter a valid number for the score.")

finally:
    print("\nEnd of Program.")