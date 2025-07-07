# 📄 AI Resume & Cover Letter Writer

[![Live App](https://img.shields.io/badge/Live%20App-Click%20Here-brightgreen?style=flat&logo=streamlit)](https://gen-ai---resume.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Create job‑ready resumes *and* cover letters in seconds.  
Powered by **Groq’s Llama‑3** models and built with **Streamlit**, this app crafts ATS‑friendly documents you can download as **PDF** or **Word** files.

---

## 🚀 Try It Live

👉 **[gen‑ai---resume.streamlit.app](https://gen-ai---resume.streamlit.app/)**

---

## ✨ Key Features

| #️⃣ | Feature                | What it does                                                                   |
|-----|------------------------|--------------------------------------------------------------------------------|
| 1️⃣ | **AI Resume Builder** 📝   | Generates a clean, sectioned resume from your details                         |
| 2️⃣ | **Cover‑Letter Writer** 💌 | Writes a tailored cover letter using the job description you paste            |
| 3️⃣ | **Groq Llama‑3** ⚡       | Fast, cost‑efficient LLM responses via `llama3‑8b‑8192`                        |
| 4️⃣ | **Download Options** 📄   | Export to **PDF** (HTML-to-PDF) or **.docx** using `python‑docx`               |
| 5️⃣ | **Responsive UI** 📱      | No design skills required – works fully inside **Streamlit**                  |

---

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-ff4b4b?logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM-informational?logo=lightning&logoColor=white)

- **Frontend / UI:** Streamlit 1.28+  
- **LLM:** Groq API → Llama‑3‑8B‑8192  
- **Packages:** `python-docx`, `Pillow`, `base64`, `io`, `dotenv`, `groq`  
- **Language:** Python 3.9+

---

## 🔧 Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jayavardhan496/Gen-AI---Resume.git
   cd Gen-AI---Resume
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Groq API key**

   Create a `.env` file in the root folder and add:

   ```env
   GROQ_API_KEY=your_groq_key_here
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

   Open in your browser at: [http://localhost:8501](http://localhost:8501)

---

## 📂 Project Structure

<pre>
📁 Gen-AI---Resume
🌀️ app.py               # Main Streamlit app logic
🌀️ requirements.txt     # Python dependencies
🌀️ README.md            # Project documentation
🌀️ utils/               # Resume & cover letter generation logic
🌀️ assets/              # Logos, icons, sample templates
</pre>

---

## 🛣 Roadmap

- [ ] 🎨 Add multiple résumé design templates  
- [ ] 🔗 Integrate LinkedIn auto-fill  
- [ ] 📧 One-click email application submission  
- [ ] 🕋 Custom fonts and themes  

---

## 🙌 Contribute

Found a bug or want to suggest a feature?  
Feel free to **open an issue** or **submit a pull request**. Contributions are welcome!

---

## ⭐ Star This Repo

If this project helped you, please consider giving it a ⭐ on GitHub — it really encourages us!

---

## 📬 Contact

Connect with me on [LinkedIn](https://linkedin.com/in/YOUR_USERNAME)  
or check out the live app 👉 [gen-ai---resume.streamlit.app](https://gen-ai---resume.streamlit.app/)
