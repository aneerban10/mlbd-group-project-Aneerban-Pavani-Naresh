# 📚 Book Recommendation System

## 📌 Project Overview
The Book Recommendation System is designed to enhance user experience by providing personalized book suggestions based on reading history and preferences. Leveraging Google Cloud technologies and machine learning algorithms, the system combines collaborative filtering to recommend books efficiently and accurately. It includes a user-friendly frontend interface and a robust backend for scalable data processing and real-time inference.

---

## 🚀 Key Features

- 📖 Personalized recommendations using collaborative and content-based filtering  
- ☁️ Scalable data handling with Google Cloud Storage & BigQuery  
- 🔍 Machine learning model deployment via Scikit-Learn & Google AI Platform  
- 🌐 Flask-based web interface for seamless user interaction  
- ⚡ Real-time prediction and recommendation delivery  
- 📊 Data ingestion and processing pipelines built for performance and reliability  

---

## 🧠 Problem Statement

The system addresses challenges such as:
- **Data Management**: Efficiently processing large-scale datasets (books, users, ratings) using GCS.  
- **Analytics**: Deriving insights from user behavior and rating patterns  
- **Prediction**: Using ML models to forecast user preferences  
- **Accessibility**: Providing a clean and intuitive UI for all users  
- **Scalability**: Ensuring system performance under growing user base and data volume  

---

## 🛠️ Technology Stack

- **Programming Language**: Python  
- **UI Framework**: Flask  
- **Data Processing**: Pandas, NumPy, Google Cloud Storage  
- **Machine Learning**: Scikit-Learn, SVD  
- **Cloud Platform**: Google Cloud Platform (GCP)  
- **Notebook**: Jupyter Notebook  

---

## 📁 Dataset Information

- **Source**: Kaggle – Collaborative Filtering Book Recommendation Dataset  
- **Books**: 271,360 rows × 8 columns  
- **Users**: 278,858 rows × 3 columns  
- **Ratings**: 1,149,780 rows × 3 columns  

---

## 🔄 Methodology

### Collaborative Filtering
1. Create a User-Item matrix  
2. Compute user similarity (e.g., cosine similarity)  
3. Identify top-K similar users  
4. Predict ratings
