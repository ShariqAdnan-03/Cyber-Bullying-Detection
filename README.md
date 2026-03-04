# 🛡️ Cyberbullying Detection System
> **Social Media Forensics: An Adaptive Approach Based on Neural Networks with Uncertainty**

An AI-powered real-time engine designed to identify and categorize toxic behavior on social media platforms. It leverages advanced Natural Language Processing (NLP) to perform both **Binary Classification** (Is it bullying?) and **Multi-Class Categorization** (What type of bullying is it?).

---

<img width="1023" height="486" alt="image" src="https://github.com/user-attachments/assets/7cf1e170-0942-4946-8d8e-b5761c4b051c" />
<img width="1884" height="785" alt="image" src="https://github.com/user-attachments/assets/7d1bfd4b-5d50-48e6-ab54-b1c9de20103c" />
<img width="1880" height="775" alt="image" src="https://github.com/user-attachments/assets/320d4193-5e45-489f-ac38-7815de1ad621" />



## 🚀 Key Features

- **Dual-Layer Prediction** — Provides a binary "Cyberbullying" vs "Non-Cyberbullying" verdict alongside a specific sub-category (e.g., Gender, Religion, Age).
- **Real-Time Dashboard** — A Flask-based web interface for instant message analysis.
- **Topic Modeling** — Uses Latent Dirichlet Allocation (LDA) to extract underlying themes from large-scale social media datasets.
- **Legacy Model Support** — Successfully integrates and runs pre-trained models from scikit-learn v1.0.2 within a modern Python 3.10 environment.

---

## 🛠️ Tech Stack

| Category | Tools & Libraries |
|---|---|
| Backend | Python 3.10, Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Machine Learning | Scikit-learn, TensorFlow, Joblib |
| NLP & Analysis | NLTK, Pandas, NumPy, Gensim |
| Database | SQLite (for user authentication) |

---

## 🧠 How It Works

### 1. Data Preprocessing
The system cleans raw social media text by:
- Removing special characters
- Converting text to lowercase
- Performing **Lemmatization** using NLTK's WordNet
- Filtering out common English stopwords to focus on high-impact keywords

### 2. Feature Extraction
Text data is transformed into numerical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**, allowing the ML models to understand the mathematical importance of specific toxic phrases.

### 3. Classification Engine
The core engine uses a **"Model Tournament"** approach, comparing multiple algorithms:

- **Decision Tree & Random Forest** — Robust structured data analysis
- **AdaBoost & Bagging Classifiers** — Reduce bias and improve prediction accuracy
- **Voting Classifier** — Ensemble method combining strengths of multiple models for the final verdict

---

## 📂 Project Structure

```
├── app.py                    # Main Flask application
├── topic_modelling.py        # LDA analysis script
├── cyberbullying_tweets.csv  # Training dataset
├── static/                   # CSS, JS, and UI images
├── templates/                # HTML pages (Index, Predict, Dashboard)
├── .gitignore                # Prevents uploading large models/venvs
└── *.pickle / *.sav          # Pre-trained ML models and vectorizers
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/ShariqAdnan-03/Cyber-Bullying-Detection.git
cd Cyber-Bullying-Detection
```

### 2. Set up the Python 3.10 Environment
```bash
python -m venv venv_old_project
.\venv_old_project\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install flask scikit-learn==1.2.2 pandas nltk gensim
```

### 4. Run the Application
```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000` by default.

---

## 📊 Results & Visualization

The project includes a **Topic Modeling** module that analyzes the `cyberbullying_tweets.csv` dataset. Sample output identifies clusters such as:

| Topic | Keywords | Description |
|---|---|---|
| Topic 0 | high, school, girl, bullied | School-related bullying |
| Topic 1 | religion, hate, muslim, attack | Religion-based harassment |
| Topic 2 | age, old, young, boomer | Age-based discrimination |

---

## 🙋 Author

**Shariq Adnan** — [GitHub](https://github.com/ShariqAdnan-03)
