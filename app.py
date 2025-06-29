import tkinter as tk
from tkinter import filedialog

class ExcelOracleApp:
    def __init__(self, root):
        self.root = root
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

    def predict(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelOracleApp(root)
    root.mainloop()