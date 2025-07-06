<h1 align="center">📊 Excel Oracle</h1>
<p align="center">
  An AI-powered assistant that lets you chat with your Excel spreadsheets using natural language. Upload any .xlsx file and get intelligent answers, visualizations, and insights — instantly.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenAI_API-03A9F4?style=flat&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Excel-217346?style=flat&logo=microsoft-excel&logoColor=white"/>
</p>

---

## 🧠 Overview

**Excel Oracle** makes spreadsheet analysis as easy as asking a question. No formulas, no filters — just upload your Excel file and ask. It understands context, processes data with Pandas, and responds using GPT-3.5 or GPT-4 via the OpenAI API.

This project includes:

* 📥 File uploader for `.xlsx`
* 💬 Natural language interface
* 📊 Smart chart generation
* 🧠 GPT-powered query resolution
* 📈 Visual + tabular output

---

## ✨ Features

* 🤖 Chat with your Excel like it's ChatGPT
* 🧠 GPT-4 / GPT-3.5 integration via OpenAI API
* 📊 Dynamic charts using Matplotlib and Plotly
* 📄 Multiple question sessions per file
* 💡 Understands structure, context, and column relationships

---

## 🔍 Tech Stack

* **Language:** Python 3.9+
* **Framework:** Streamlit
* **LLM API:** OpenAI GPT (3.5/4)
* **Data Engine:** Pandas
* **Charts:** Matplotlib, Plotly
* **Excel Parsing:** OpenPyXL

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

* Python 3.9+
* OpenAI API Key

### 📦 Installation

```bash
git clone https://github.com/Zaid2044/Excel-Oracle.git
cd Excel-Oracle
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 🔐 Configure API Key

Create a `.env` file in the root:

```env
OPENAI_API_KEY="your_actual_key_here"
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Visit: [http://localhost:8501](http://localhost:8501)
Upload your Excel file → Ask your questions → Get clean answers and charts

---

## 📁 Project Structure

```
Excel-Oracle/
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧩 Future Upgrades

* 🗂️ Multi-sheet support
* 🧮 Google Sheets + CSV integration
* 🎙️ Voice query input
* 🔄 Retain question history across sessions

---

## 🧑‍💻 Author
**MOHAMMED ZAID AHMED**

---
