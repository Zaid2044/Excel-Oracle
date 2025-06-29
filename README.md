# Excel Oracle 🔮✨

You stare at the spreadsheet. The spreadsheet stares back. You make a pivot table. It's cringe. You use VLOOKUP. It's boomer-tier. You need to know the future, but your Excel skills are stuck in the past.

**The Excel Oracle** is the answer. It's a simple GUI powered by a god-tier LightGBM model that doesn't just look at your data—it understands its rhythm. Load a file, click a button, and witness the prophecy.

## ✨ Features - The Vision ✨

*   **📜 The Sacred Scroll:** Load time-series data from any `.csv` or `.xlsx` file with a simple, clean UI.
*   **🧠 The Brain Transplant:** Automatically performs feature engineering on your data, teaching the AI the concepts of "day of the week" and "week of the year" to understand complex, seasonal patterns.
*   **🤖 The Prophet:** Trains a powerful `LightGBM` regression model on your historical data in seconds.
*   **📈 The Vision:** Generates a clean, professional plot from `matplotlib` showing your past data in a solid line and the AI's predicted future in a dashed line. It's not a guess; it's a data-driven prophecy.

## 🛠️ The Arsenal - Tech Stack 🛠️

*   **Language:** Python 🐍
*   **Data Handling:** Pandas
*   **Machine Learning:** Scikit-learn & LightGBM
*   **Plotting:** Matplotlib
*   **GUI:** Tkinter

## 📜 The Ritual - Installation & Setup 📜

Awaken the Oracle on your machine.

**1. Clone the Temple**
```bash
git clone https://github.com/Zaid2044/Excel-Oracle.git
cd Excel-Oracle
```

**2. Create the Virtual Sanctuary**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**3. Install the Arcane Libraries**
```bash
pip install -r requirements.txt
```

## ⚔️ How to Consult the Oracle ⚔️

Run the main script from your terminal:
```bash
python app.py
```

*   **1. A window will appear. Click "Load Excel File".**
*   **2. Select a .csv or .xlsx file containing your time-series data.**
*   **3. The "Predict The Future" button will become clickable. Click it.**
*   **4.A new window will pop up, revealing the prophecy in a beautiful graph.** 

## The Scrolls (Data Format)

For the Oracle to read your data correctly, it expects at least two columns:

*   **Day:** A numerical sequence representing the time step (1, 2, 3, ...).
*   **Sales:** The value you want to predict.

Check out sales_data.csv for a simple linear example