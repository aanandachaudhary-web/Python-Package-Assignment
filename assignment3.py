from colorama import Fore, init

init(autoreset=True)

name = input("Enter student's name: ")

try:
    marks = float(input("Enter student's marks (0-100): "))

    if not 0 <= marks <= 100:
        print(Fore.RED + "Please enter marks between 0 and 100.")

    else:
        print(Fore.CYAN + f"\nStudent name: {name}")
        print(f"Marks: {marks:g}")

        if marks >= 40:
            print(Fore.GREEN + "Result: PASS")
        else:
            print(Fore.RED + "Result: FAIL")

except ValueError:
    print(Fore.RED + "Invalid input. Please enter numeric marks.")