import numpy as np

class DataAnalytics:
    def __init__(self):
        self.array = None

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                elements = input("Enter elements for the 1D array separated by space: ").split()
                self.array = np.array([float(x) if '.' in x else int(x) for x in elements])
            elif choice == 2:
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                total_elements = rows * cols
                elements = input(f"Enter {total_elements} elements for the array separated by space: ").split()
                if len(elements) != total_elements:
                    print(f"Error: Expected {total_elements} elements, but got {len(elements)}.")
                    return
                arr = np.array([float(x) if '.' in x else int(x) for x in elements])
                self.array = arr.reshape((rows, cols))
            elif choice == 3:
                d = int(input("Enter depth (blocks): "))
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                total_elements = d * rows * cols
                elements = input(f"Enter {total_elements} elements for the array separated by space: ").split()
                if len(elements) != total_elements:
                    print(f"Error: Expected {total_elements} elements, but got {len(elements)}.")
                    return
                arr = np.array([float(x) if '.' in x else int(x) for x in elements])
                self.array = arr.reshape((d, rows, cols))
            else:
                print("Invalid choice selected.")
                return

            print("\nArray created successfully:")
            print(self.array)
            
        except ValueError:
            print("Invalid input! Please enter valid numeric values.")

    def mathematical_operations(self):
        if self.array is None:
            print("\nNo array found! Please create an array first (Option 1).")
            return

        print("\nMathematical Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product / Matrix Multiplication (2D arrays)")

        try:
            choice = int(input("Enter your choice: "))
            
            if choice in [1, 2, 3, 4]:
                flat_size = self.array.size
                elements = input(f"Enter same-size array elements ({flat_size} elements separated by space): ").split()
                if len(elements) != flat_size:
                    print(f"Error: Expected {flat_size} elements.")
                    return
                
                other_arr = np.array([float(x) if '.' in x else int(x) for x in elements]).reshape(self.array.shape)
                
                print("\nOriginal Array:")
                print(self.array)
                print("\nSecond Array:")
                print(other_arr)

                if choice == 1:
                    result = np.add(self.array, other_arr)
                    print("\nResult of Addition:")
                elif choice == 2:
                    result = np.subtract(self.array, other_arr)
                    print("\nResult of Subtraction:")
                elif choice == 3:
                    result = np.multiply(self.array, other_arr)
                    print("\nResult of Multiplication:")
                elif choice == 4:
                    result = np.divide(self.array, other_arr)
                    print("\nResult of Division:")
                
                print(result)

            elif choice == 5:
                if self.array.ndim != 2:
                    print("Matrix multiplication requires a 2D array.")
                    return
                cols = self.array.shape[1]
                elements = input(f"Enter second 2D array elements compatible for multiplication ({cols} columns per row): ").split()
                other_arr = np.array([float(x) if '.' in x else int(x) for x in elements]).reshape((cols, -1))
                
                result = np.dot(self.array, other_arr)
                print("\nDot Product / Matrix Multiplication Result:")
                print(result)
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def combine_or_split_arrays(self):
        if self.array is None:
            print("\nNo array found! Please create an array first.")
            return

        print("\nCombine or Split Arrays:")
        print("1. Combine Arrays (Concatenate)")
        print("2. Split Array")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                flat_size = self.array.size
                elements = input(f"Enter elements of another array to combine ({flat_size} elements separated by space): ").split()
                other_arr = np.array([float(x) if '.' in x else int(x) for x in elements]).reshape(self.array.shape)
                
                axis = int(input("Enter axis to concatenate along (0 for rows, 1 for columns if 2D): "))
                combined = np.concatenate((self.array, other_arr), axis=axis)
                print("\nCombined Array:")
                print(combined)
            elif choice == 2:
                sections = int(input("Enter number of sections to split into: "))
                axis = int(input("Enter axis to split along: "))
                split_result = np.array_split(self.array, sections, axis=axis)
                print("\nSplit Arrays:")
                for i, part in enumerate(split_result):
                    print(f"Section {i+1}:\n{part}")
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def search_sort_filter(self):
        if self.array is None:
            print("\nNo array found! Please create an array first.")
            return

        print("\nSearch, Sort, and Filter:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values (e.g., elements > value)")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                val = float(input("Enter value to search: "))
                indices = np.where(self.array == val)
                print(f"\nOriginal Array:\n{self.array}")
                print(f"Found at indices: {indices}")
            elif choice == 2:
                sorted_arr = np.sort(self.array, axis=-1)
                print(f"\nOriginal Array:\n{self.array}")
                print(f"\nSorted Array:\n{sorted_arr}")
                print("(Sorting applied row-wise/along last axis.)")
            elif choice == 3:
                threshold = float(input("Enter threshold value for filtering (e.g., elements > x): "))
                filtered = self.array[self.array > threshold]
                print(f"\nFiltered Elements (where value > {threshold}):")
                print(filtered)
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def compute_aggregates_and_statistics(self):
        if self.array is None:
            print("\nNo array found! Please create an array first.")
            return

        print("\nAggregates and Statistics:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum and Maximum")

        try:
            choice = int(input("Enter your choice: "))
            print(f"\nOriginal Array:\n{self.array}")
            
            if choice == 1:
                print(f"Sum of Array: {np.sum(self.array)}")
            elif choice == 2:
                print(f"Mean of Array: {np.mean(self.array)}")
            elif choice == 3:
                print(f"Median of Array: {np.median(self.array)}")
            elif choice == 4:
                print(f"Standard Deviation: {np.std(self.array)}")
            elif choice == 5:
                print(f"Variance: {np.var(self.array)}")
            elif choice == 6:
                print(f"Minimum Value: {np.min(self.array)}")
                print(f"Maximum Value: {np.max(self.array)}")
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @classmethod
    def about_project(cls):
        print("\n[Class Method] NumPy Analyzer: Built to perform data operations, math computations, and statistics using OOP.")

    @staticmethod
    def app_info():
        print("[Static Method] Version 1.0 | Developed for Skill Education Data Analytics Project.")


def main():
    analyzer = DataAnalytics()
    DataAnalytics.about_project()
    DataAnalytics.app_info()

    while True:
        print("\n==========================================")
        print("Welcome to the NumPy Analyzer!")
        print("==========================================")
        print("Choose an option:")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                analyzer.create_array()
            elif choice == 2:
                analyzer.mathematical_operations()
            elif choice == 3:
                analyzer.combine_or_split_arrays()
            elif choice == 4:
                analyzer.search_sort_filter()
            elif choice == 5:
                analyzer.compute_aggregates_and_statistics()
            elif choice == 6:
                print("\nThank you for using the NumPy Analyzer! Goodbye!")
                break
            else:
                print("Invalid option. Please choose between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a valid integer choice.")

if __name__ == "__main__":
    main()