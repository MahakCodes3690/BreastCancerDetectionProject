# breast-cancer-detection-ml-flask
Machine Learning–based Breast Cancer Detection Web App built with Flask. Predicts whether a tumor is Benign (0) or Malignant (1) using an SVM model trained on the Breast Cancer Wisconsin dataset.
# 🚀 Features
- 🧠 **SVM (Support Vector Machine)**–based ML model for classification  
- 🧮 Preprocessing pipeline with **StandardScaler**  
- 🌐 Interactive **Flask Web App** for easy user input  
- 📊 Real-time predictions for 30 diagnostic features  
- 💾 Model saved with **Joblib** for reuse and integration  

---

## 🧠 Model Overview
- **Algorithm:** Support Vector Machine (Linear Kernel)  
- **Dataset:** [Breast Cancer Wisconsin (Diagnostic)](https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-dataset)  
- **Accuracy:** ~97% on test data  
- **Libraries Used:** Scikit-learn, NumPy, Pandas, Flask, Joblib  

---

## 🖥️ How It Works
1. User enters 30 feature values (or uploads data).  
2. Flask backend loads the trained model (`breast_cancer_pipeline.joblib`).  
3. Model predicts the class:
   - `0` → **Benign**
   - `1` → **Malignant**
4. Result displayed on the web page with prediction label and confidence score.

---

## 🧰 Tech Stack
| Layer | Technologies |
|-------|---------------|
| **Frontend** | HTML, CSS, Bootstrap |
| **Backend** | Flask (Python) |
| **ML Model** | Scikit-learn (SVM) |
| **Storage** | Joblib Model File |
| **Deployment** | Render / Streamlit / Localhost |

---
