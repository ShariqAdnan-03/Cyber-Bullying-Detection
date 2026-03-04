# 🛡️ Forensic Analysis of Social Media: Detecting Cyberbullying-Related Hate Speech

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" />
  <img src="https://img.shields.io/badge/Framework-Flask-green.svg" />
  <img src="https://img.shields.io/badge/ML-Ensemble%20Learning-orange.svg" />
  <img src="https://img.shields.io/badge/Patent-Applied%20202541122189-purple.svg" />
</p>

An adaptive ensemble learning system for detecting cyberbullying-related hate speech on social media. Combines SVM, Random Forest, Logistic Regression, and MLP classifiers with a **Voting Classifier ensemble** (Boosted DT + Bagging RF) to achieve up to **100% accuracy** on benchmark datasets.

> 🔏 **Patent Application No:** `202541122189` — [Check Status](https://iprsearch.ipindia.gov.in/PublicSearch/PublicationSearch/ApplicationStatus)  
> 📚 **Course Code:** CBS1904

---

## 🧠 How It Works

```
Raw Social Media Text
        ↓
Preprocessing (clean, encode, SMOTE oversample, TF-IDF vectorize)
        ↓
ML Models: SVM · Random Forest · Logistic Regression · MLP-OVO · MLP-OVR
        ↓
Voting Classifier (Boosted DT + Bagging RF)  ← best performer
        ↓
Topic Modeling (keyword/theme extraction)
        ↓
Prediction: Cyberbullying Detected / Not Detected
```

---

## 📈 Results

The **Voting Classifier** outperformed all individual models across both datasets:

| Dataset | Task | Voting Classifier Accuracy |
|---------|------|---------------------------|
| Dataset 1 | Binary | **99.4%** |
| Dataset 1 | Multi-class | **98.5%** |
| Dataset 2 | Binary | **100%** |
| Dataset 2 | Multi-class | **99.7%** |

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.8+ |
| ML | scikit-learn, imbalanced-learn (SMOTE) |
| NLP | NLTK, TF-IDF |
| Visualization | Matplotlib, Seaborn, WordCloud |
| Web App | Flask, HTML/CSS/JS, Bootstrap 4 |
| Database | SQLite3 |
| Environment | Anaconda, Jupyter Notebook |

---

## ⚙️ Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-username/cyberbullying-detection.git
cd cyberbullying-detection

# 2. Create environment
conda create -n cyberbully python=3.8
conda activate cyberbully

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
cd app && python app.py
# Open http://127.0.0.1:5000
```

---

## 🚀 Usage

1. Register / Login via the web interface
2. Enter a social media post or tweet
3. Get an instant prediction — **cyberbullying** or **not**

---

## 📁 Project Structure

```
cyberbullying-detection/
├── datasets/          # Dataset 1 & 2 (CSV)
├── notebooks/         # Preprocessing, training, topic modeling
├── models/            # Saved .pkl model files
├── app/               # Flask app (templates, static, app.py)
├── utils/             # preprocess.py, vectorizer.py, predict.py
└── requirements.txt
```

---

## 🔮 Future Scope

- Multilingual support (Arabic, Hindi) via multilingual BERT
- GPU-accelerated transformers (BERT, RoBERTa)
- LLM integration for nuanced context understanding
- Real-time browser extension / API deployment

---

## 👥 Team

| Name |
|------|
| Annamreddy Dinesh |
| Perugu Ajay Kumar |
| Vakkala Shariq Adnan |

---

## 📚 References

1. Yarbrough et al. — *Cyberbullying and the Faculty Victim Experience* [DOI](https://doi.org/10.1007/s42380-023-00173-x)
2. Alzaqebah et al. — *Cyberbullying Detection for Arabic Datasets* [DOI](https://doi.org/10.1016/j.jksuci.2023.101652)
3. Muneer et al. — *Stacking Ensemble + Enhanced BERT* [DOI](https://doi.org/10.3390/info14080467)
4. Sultan et al. — *Shallow-to-Deep Learning for Hate Speech* [DOI](https://doi.org/10.32604/cmc.2023.032993)
5. Fulantelli et al. — *Cyberbullying & Cyberhate: Systematic Review* [DOI](https://doi.org/10.3389/fpsyg.2022.909909)
