import matplotlib.pyplot as plt
import numpy as np
import sqlite3
from database import register_user, login_user, save_history, view_history

# ...existing code...

if __name__ == "__main__":
    print("Welcome to the MCP Tool with User Login!")
    print("1 = Register")
    print("2 = Login")
    print("Type 'exit' to quit.")

    current_user_id = None

    while True:
        if not current_user_id:
            option = input("\nEnter your choice (1 = Register, 2 = Login): ")
            if option.lower() == 'exit':
                print("Exiting the MCP Tool. Goodbye!")
                break

            if option == '1':
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                register_user(username, password)

            elif option == '2':
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                current_user_id = login_user(username, password)

            else:
                print("Invalid option. Please choose 1 or 2.")
        else:
            print("\nWelcome back! What would you like to do?")
            print("1 = View history")
            print("2 = Perform an action")
            print("3 = Logout")

            option = input("Enter your choice: ")
            if option == '1':
                history = view_history(current_user_id)
                if history:
                    print("Your history:")
                    for action, timestamp in history:
                        print(f"- {action} at {timestamp}")
                else:
                    print("No history found.")

            elif option == '2':
                print("Available options:")
                print("1 = Create a plot")
                print("2 = Find intersection of two lines")
                print("3 = Find zeros of a polynomial")
                print("4 = Find common values between two sets of data")
                print("Type 'exit' at any time to quit.")

                while True:
                    try:
                        option = input("\nEnter the operation you want to perform (1, 2, 3, 4): ")
                        if option.lower() == 'exit':
                            print("Exiting the MCP Tool. Goodbye!")
                            break

                        if option == '1':
                            print("Creating a plot.")
                            user_input = input("Enter data values separated by spaces: ")
                            data = list(map(float, user_input.split()))

                            plot_type = input("Enter plot type (1 = Line, 2 = Pie, 3 = Bar, 4 = Scatter, 5 = Histogram): ")
                            if not plot_type.isdigit() or int(plot_type) not in [1, 2, 3, 4, 5]:
                                print("Invalid plot type. Please choose a number from 1 to 5.")
                                continue

                            labels_input = input("Enter variable names separated by spaces (e.g., x1 x2 y1): ")
                            labels = labels_input.split()

                            if len(labels) < 1:
                                print("Please provide at least one label.")
                                continue

                            if len(labels) < 3:
                                print("Warning: At least three labels are recommended for proper axis labeling.")

                            generate_plot(data, int(plot_type), labels)

                        elif option == '2':
                            print("Finding intersections of multiple lines.")
                            num_lines = int(input("Enter the number of lines: "))
                            lines = []
                            for i in range(num_lines):
                                print(f"Line {i + 1}:")
                                m = float(input("  Enter slope (m): "))
                                b = float(input("  Enter y-intercept (b): "))
                                lines.append((m, b))

                            intersections = find_intersections(lines)
                            if intersections:
                                print("The intersections are:")
                                for point in intersections:
                                    print(f"  ({point[0]}, {point[1]})")
                            else:
                                print("No intersections found (all lines are parallel).")

                        elif option == '3':
                            print("Finding zeros of a polynomial.")
                            coefficients = list(map(float, input("Enter polynomial coefficients separated by spaces (highest degree first): ").split()))
                            zeros = find_zeros(coefficients)
                            print(f"The zeros of the polynomial are: {zeros}")

                        elif option == '4':
                            print("Finding common values between two sets of data.")
                            array1 = list(map(float, input("Enter the first set of values separated by spaces: ").split()))
                            array2 = list(map(float, input("Enter the second set of values separated by spaces: ").split()))
                            common_values = find_common_values(array1, array2)
                            print(f"The common values are: {common_values}")

                        else:
                            print("Invalid option. Please choose 1, 2, 3, or 4.")

                    except ValueError as e:
                        print(f"Error: {e}. Please ensure your input is valid and try again.")

                action = input("Describe the action you performed: ")
                save_history(current_user_id, action)
                print("Action saved to history.")

            elif option == '3':
                print("Logging out...")
                current_user_id = None

            else:
                print("Invalid option. Please choose 1, 2, or 3.")