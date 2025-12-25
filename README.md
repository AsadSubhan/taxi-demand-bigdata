# 🚕 Real-Time Taxi Demand Prediction Using Big Data Analytics

## 📌 Project Overview
Urban transportation systems face challenges such as uneven taxi availability, long passenger wait times, and inefficient resource utilization. This project implements a **Big Data analytics pipeline** to analyze large-scale NYC Taxi trip data and predict short-term taxi demand across different city zones using **distributed processing with Apache Spark**.

The project demonstrates real-world **big data engineering + machine learning** concepts including distributed ingestion, preprocessing, feature engineering, model training, and prediction.

---

## 🎯 Objectives
- Build a scalable big data pipeline for processing millions of taxi trip records  
- Predict short-term taxi demand per location and time window  
- Use distributed computing frameworks for data processing and ML  
- Store and query large datasets efficiently using Parquet and Hive  
- Visualize demand trends and evaluate prediction accuracy  

---

## 📂 Dataset
**Source:** NYC Taxi & Limousine Commission (TLC)  
🔗 https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

### Dataset Characteristics
- Millions of records per month  
- Multi-year historical data  
- Attributes include pickup/dropoff time, location IDs, fare, trip distance, etc.  
- Suitable for batch and streaming analytics  




---

## ⚙️ Tools & Technologies

| Category | Technology |
|-------|-----------|
| Distributed Processing | Apache Spark (PySpark) |
| Storage | Parquet, HDFS (conceptual) |
| Query Engine | Apache Hive |
| Machine Learning | Spark MLlib |
| Programming Language | Python |
| Visualization | Power BI / Tableau (optional) |

---

## 🔄 Pipeline Description

### 1️⃣ Data Ingestion
- Reads large CSV files using Spark
- Converts data into Parquet format for efficient storage and querying

### 2️⃣ Data Preprocessing
- Removes invalid records
- Extracts time-based features (hour, day of week)

### 3️⃣ Feature Engineering
- Aggregates taxi demand per location and time window
- Prepares data for machine learning

### 4️⃣ Model Training
- Uses **Random Forest Regressor (Spark MLlib)**
- Trains on distributed data
- Evaluates using RMSE

### 5️⃣ Prediction
- Predicts taxi demand for future time windows
- Supports location-based forecasting

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.x  
- Apache Spark (3.x)  
- Java 8+  

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Full Pipeline
```bash
bash scripts/run_pipeline.sh
```

### Run Individual Steps
```bash
spark-submit spark/ingestion/ingest_tlc_data.py
spark-submit spark/preprocessing/preprocess_trips.py
spark-submit spark/feature_engineering/build_features.py
spark-submit spark/modeling/train_demand_model.py
```


## ✅ Expected Outcomes
- Scalable big data processing pipeline
- Accurate short-term taxi demand predictions
- Efficient distributed storage and computation
- Industry-aligned big data project suitable for academic submission





### 👤 Author
 - Asad Subhan (DevOps/Cloud Engineer)