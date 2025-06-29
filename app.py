import tkinter as tk
from tkinter import filedialog
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class ExcelOracleApp:
    def __init__(self, root):
        self.root = root
        self.df = None
        self.root.title("Excel Oracle")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="Load an Excel file to see the future.", pady=10)
        self.label.pack()

        self.load_button = tk.Button(root, text="Load Excel File", command=self.load_file)
        self.load_button.pack(pady=10)

        self.predict_button = tk.Button(root, text="Predict The Future", state=tk.DISABLED, command=self.predict)
        self.predict_button.pack(pady=10)

    def load_file(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx *.xls"), ("CSV files", "*.csv")]
        )
        if not filepath:
            return
        
        try:
            if filepath.endswith('.csv'):
                self.df = pd.read_csv(filepath)
            else:
                self.df = pd.read_excel(filepath)
            
            self.label.config(text=f"Loaded: {filepath.split('/')[-1]}")
            self.predict_button.config(state=tk.NORMAL)
        except Exception as e:
            self.label.config(text=f"Error: {e}")

    def predict(self):
        if self.df is None:
            self.label.config(text="No data loaded to predict.")
            return

        X = self.df[['Day']]
        y = self.df['Sales']

        model = LinearRegression()
        model.fit(X, y)

        last_day = self.df['Day'].max()
        future_days = pd.DataFrame({'Day': range(last_day + 1, last_day + 6)})
        
        future_sales = model.predict(future_days)

        for day, sale in zip(future_days['Day'], future_sales):
            print(f"Predicted sales for day {day}: {int(sale)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelOracleApp(root)
    root.mainloop()