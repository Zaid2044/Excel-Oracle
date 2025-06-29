import tkinter as tk
from tkinter import filedialog
import pandas as pd
import lightgbm as lgb
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

        self.predict_button =.Button(root, text="Predict The Future", state=tk.DISABLED, command=self.predict)
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

        self.df['day_of_week'] = (self.df['Day'] - 1) % 7
        self.df['week_of_year'] = (self.df['Day'] - 1) // 7

        self.df['day_of_week'] = self.df['day_of_week'].astype('category')
        self.df['week_of_year'] = self.df['week_of_year'].astype('category')

        X = self.df[['Day', 'day_of_week', 'week_of_year']]
        y = self.df['Sales']

        model = lgb.LGBMRegressor(random_state=42)
        model.fit(X, y)

        last_day = self.df['Day'].max()
        
        future_days_range = range(last_day + 1, last_day + 6)
        future_df = pd.DataFrame({'Day': future_days_range})
        future_df['day_of_week'] = (future_df['Day'] - 1) % 7
        future_df['week_of_year'] = (future_df['Day'] - 1) // 7

        future_df['day_of_week'] = future_df['day_of_week'].astype('category')
        future_df['week_of_year'] = future_df['week_of_year'].astype('category')
        
        future_sales = model.predict(future_df)

        plot_window = tk.Toplevel(self.root)
        plot_window.title("The Future is Now")

        fig = Figure(figsize=(6, 4), dpi=100)
        plot = fig.add_subplot(111)

        plot.plot(self.df['Day'], self.df['Sales'], 'b-', label='Historical Data')
        plot.plot(future_df['Day'], future_sales, 'r--', label='Predicted Future')

        plot.set_title("Sales Prediction")
        plot.set_xlabel("Day")
        plot.set_ylabel("Sales")
        plot.legend()
        plot.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelOracleApp(root)
    root.mainloop()