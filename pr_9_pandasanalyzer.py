import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class SalesDataAnalyzer:
    def __init__(self):
        self.data = None
        print("--- Sales Analyzer Initialized ---")

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print(f"Error loading file: {e}")

    def explore_data(self):
        if self.data is not None:
            print("\n--- Explore Data ---")
            print("1. First 5 rows\n2. Last 5 rows\n3. Column names\n4. Data types\n5. Basic info")
            choice = input("Enter your choice: ")
            
            if choice == '1': 
                print(self.data.head())
            elif choice == '2': 
                print(self.data.tail())
            elif choice == '3': 
                print(self.data.columns)
            elif choice == '4': 
                print(self.data.dtypes)
            elif choice == '5': 
                print(self.data.info())
            else:
                print("Invalid choice.")
        else:
            print("Please load a dataset first.")

    def clean_data(self):
        if self.data is not None:
            print("\n--- Handle Missing Data ---")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean (numeric only)")
            print("3. Drop rows with missing values")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                missing_rows = self.data[self.data.isnull().any(axis=1)]
                if missing_rows.empty:
                    print("No missing values found.")
                else:
                    print(missing_rows)
            elif choice == '2':
                self.data = self.data.fillna(self.data.mean(numeric_only=True))
                print("Missing values filled with mean.")
            elif choice == '3':
                self.data = self.data.dropna()
                print("Rows with missing values dropped.")
            else:
                print("Invalid choice.")
        else:
            print("No data to clean.")

    def mathematical_operations(self):
        if self.data is not None:
            if 'Sales' in self.data.columns:
                sales_array = np.array(self.data['Sales'])
                print(f"Original Sales Array (first 5 values): {sales_array[:5]}")
                
                # Example: calculate 10% tax
                tax_array = sales_array * 0.10
                print(f"Tax Calculation (10% of Sales, first 5 values): {tax_array[:5]}")
            else:
                print("No 'Sales' column found in dataset.")
        else:
            print("Load data first.")

    def search_sort_filter(self):
        if self.data is not None:
            if 'Sales' in self.data.columns:
                sorted_data = self.data.sort_values(by='Sales', ascending=False)
                print("Top 5 rows after sorting by Sales (Descending):")
                print(sorted_data.head())
            else:
                print("No 'Sales' column to sort.")
        else:
            print("Load data first.")

    def aggregate_functions(self):
        if self.data is not None:
            print("\n--- Descriptive Statistics ---")
            print(self.data.describe())
        else:
            print("No data available.")

    def visualize_data(self):
        if self.data is not None:
            print("\n--- Data Visualization ---")
            print("1. Bar Plot\n2. Line Plot\n3. Scatter Plot\n4. Pie Chart\n5. Histogram")
            choice = input("Enter your choice: ")
            
            plt.figure(figsize=(10, 6))
            
            try:
                if choice == '1':
                    if 'Region' in self.data.columns and 'Sales' in self.data.columns:
                        sns.barplot(x='Region', y='Sales', data=self.data)
                        plt.title("Sales by Region")
                    else:
                        print("Required columns not found for Bar Plot.")
                elif choice == '2':
                    if 'Year' in self.data.columns and 'Sales' in self.data.columns:
                        sns.lineplot(x='Year', y='Sales', data=self.data, marker='o')
                        plt.title("Sales Trend over Years")
                    else:
                        print("Required columns not found for Line Plot.")
                elif choice == '3':
                    x_col = input("Enter x-axis column: ")
                    y_col = input("Enter y-axis column: ")
                    if x_col in self.data.columns and y_col in self.data.columns:
                        sns.scatterplot(x=x_col, y=y_col, data=self.data)
                        plt.title(f"{x_col} vs {y_col}")
                    else:
                        print("Invalid columns for Scatter Plot.")
                elif choice == '4':
                    col = input("Enter column for Pie Chart (e.g., Region): ")
                    if col in self.data.columns:
                        self.data[col].value_counts().plot.pie(autopct='%1.1f%%')
                        plt.title(f"Pie Chart of {col}")
                    else:
                        print("Column not found.")
                elif choice == '5':
                    col = input("Enter numeric column for Histogram: ")
                    if col in self.data.columns:
                        self.data[col].plot.hist(bins=10)
                        plt.title(f"Histogram of {col}")
                    else:
                        print("Column not found.")
                else:
                    print("Invalid choice.")
                    return

                plt.tight_layout()
                plt.show()
                print("Plot displayed successfully!")
            except Exception as e:
                print(f"Error displaying plot: {e}")
        else:
            print("Load data first.")

    def save_visualization(self):
        filename = input("Enter file name to save (e.g., plot.png): ")
        try:
            plt.savefig(filename)
            print(f"Visualization saved as {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

    def __del__(self):
        print("Cleaning up resources... Goodbye!")

def main():
    analyzer = SalesDataAnalyzer()
    
    while True:
        print("\n========== Data Analysis & Visualization Program ==========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations (Numpy/Math)")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("==========================================================")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            path = input("Enter the path of the dataset (CSV file): ")
            analyzer.load_data(path)
        elif choice == '2':
            analyzer.explore_data()
        elif choice == '3':
            analyzer.mathematical_operations()
        elif choice == '4':
            analyzer.clean_data()
        elif choice == '5':
            analyzer.aggregate_functions()
        elif choice == '6':
            analyzer.visualize_data()
        elif choice == '7':
            analyzer.save_visualization()
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
