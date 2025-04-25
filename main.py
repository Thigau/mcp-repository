import matplotlib.pyplot as plt
import numpy as np

def generate_plot(data, plot_type, labels):
    if plot_type == 1:  # Line plot
        plt.plot(data, label=labels[0])
    elif plot_type == 2:  # Pie chart
        if len(data) != len(set(data)):
            raise ValueError("Pie chart requires unique labels for each data point.")
        plt.pie(data, labels=labels, autopct='%1.1f%%')
    elif plot_type == 3:  # Bar chart
        plt.bar(range(len(data)), data, label=labels[0])
    elif plot_type == 4:  # Scatter plot
        plt.scatter(range(len(data)), data, label=labels[0])
    elif plot_type == 5:  # Histogram
        plt.hist(data, bins=10, edgecolor='black', label=labels[0])
    else:
        raise ValueError("Unsupported plot type")

    plt.title(f"Plot Type {plot_type}")
    plt.xlabel(labels[1] if len(labels) > 1 else labels[0])
    plt.ylabel(labels[2] if len(labels) > 2 else labels[0])
    plt.legend()
    plt.grid(True)
    plt.show()

def find_intersection(line1, line2):
    # Solve for intersection of two lines given by y = m1*x + b1 and y = m2*x + b2
    m1, b1 = line1
    m2, b2 = line2

    if m1 == m2:
        raise ValueError("The lines are parallel and do not intersect.")

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y

def find_intersections(lines):
    # Find intersections between multiple lines
    intersections = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            m1, b1 = lines[i]
            m2, b2 = lines[j]

            if m1 == m2:
                continue  # Skip parallel lines

            x = (b2 - b1) / (m1 - m2)
            y = m1 * x + b1
            intersections.append((x, y))

    return intersections

def find_zeros(coefficients):
    # Find zeros of a polynomial given its coefficients
    return np.roots(coefficients)

def find_common_values(array1, array2):
    # Find common values between two arrays
    return np.intersect1d(array1, array2)

if __name__ == "__main__":
    print("Welcome to the MCP Tool!")
    print("This tool allows you to create plots and perform advanced calculations.")
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