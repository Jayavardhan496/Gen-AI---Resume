# 📄 AI Resume & Cover Letter Writer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gen-ai---resume.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Create job‑ready resumes *and* cover letters in seconds.  
Powered by *Groq’s Llama‑3* models and built with *Streamlit, this app crafts ATS‑friendly documents you can download as **PDF* or *Word* files.

---

## 🚀 Try It Live

👉 **[gen‑ai---resume.streamlit.app](https://gen-ai---resume.streamlit.app/)**

---

## ✨ Key Features

| # | Feature               | What it does                                                                 |
|---|------------------------|------------------------------------------------------------------------------|
| 1 | *AI Resume Builder*  | Generates a clean, sectioned resume from your details                        |
| 2 | *Cover‑Letter Writer*| Writes a tailored cover letter using the job description you paste          |
| 3 | *Groq Llama‑3*       | Fast, cost‑efficient LLM responses via llama3‑8b‑8192                       |
| 4 | *Download Options*   | One‑click export to *PDF* (HTML-to-PDF) or *.docx* using python‑docx   |
| 5 | *Responsive UI*      | Runs entirely in Streamlit; no design skills required                        |

---

## 🛠 Tech Stack

- *Frontend / UI:* Streamlit 1.28+  
- *LLM:* Groq API → Llama‑3‑8B‑8192  
- *Python Packages:* python-docx, Pillow, base64, io, dotenv, groq  
- *Language:* Python 3.9+

---

## 🔧 Local Setup

1. *Clone* the repository

bash
git clone https://github.com/Jayavardhan496/Gen-AI---Resume.git
cd Gen-AI---Resume


2. *Install* dependencies

bash
pip install -r requirements.txt


3. *Set up your Groq API key*

Create a .env file in the root folder and add:

env
GROQ_API_KEY=your_groq_key_here


4. *Run the Streamlit app*

bash
streamlit run app.py


Open in your browser at: http://localhost:8501

---

## 📂 Project Structure


├── app.py                 # Streamlit UI and main logic
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── (helper modules)       # Resume & cover letter generation


---

## 🛣 Roadmap

- [ ] Multiple résumé design templates  
- [ ] LinkedIn profile integration for auto-fill  
- [ ] One-click email application submission  
- [ ] Custom fonts and themes

Feel free to open issues or contribute via pull requests!

---

## ⭐ Star This Repo

If this project helped you, please consider giving it a ⭐ on GitHub — it really encourages us!
