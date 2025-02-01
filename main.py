from logic import MatheMatics

def main():
    math_obj = MatheMatics()

    choice = input("Enter the operation you want to perform (1,2,3,4):\n"
                   "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

    try:
        if choice == '1':
            print(f"The sum of the two numbers is: {math_obj.add()}")
        elif choice == '2':
            print(f"The difference of the two numbers is: {math_obj.sub()}")
        elif choice == '3':
            print(f"The product of the two numbers is: {math_obj.mul()}")
        elif choice == '4':
            print(f"The quotient of the two numbers is: {math_obj.div()}")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    main()
