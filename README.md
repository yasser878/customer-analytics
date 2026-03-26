# Adult Project

## 📌 Description
This project performs a complete data analytics pipeline on the Adult dataset using Python and Docker.  
It starts from raw data ingestion, processes and cleans the data, extracts insights, visualizes results, and applies clustering techniques to group similar records.

---

## 🚀 Features
- Data ingestion from CSV file
- Data preprocessing and cleaning
- Insight generation and statistical analysis
- Data visualization using plots
- Clustering using machine learning algorithms
- Dockerized environment for reproducibility

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Docker

---

## 📌 Detailed Explanation

The project follows a structured pipeline where data flows through multiple stages to ensure accurate processing and meaningful results.

---

### 🔹 Data Ingestion
In this stage, the dataset (adult.csv) is loaded into the system using Python scripts.

- The dataset is read using Pandas into a DataFrame  
- Data is structured into rows and columns  
- Initial inspection of data is performed (shape, columns, data types)  
- Raw data is saved as `data_raw.csv`  

This step ensures that the dataset is correctly loaded and ready for processing.

---

### 🔹 Data Preprocessing
This is one of the most important stages in the pipeline, where raw data is cleaned and prepared.

- Handling missing or null values  
- Removing duplicate or inconsistent records  
- Encoding categorical variables into numerical values  
- Cleaning noisy or irrelevant data  
- Preparing features for analysis and machine learning  

The goal is to transform raw data into a clean, consistent, and usable format.

---

### 🔹 Analytics & Insights
In this stage, the processed data is analyzed to extract useful information.

- Generating statistical summaries (mean, median, distributions)  
- Identifying patterns and relationships between variables  
- Extracting meaningful insights from the dataset  
- Saving results into insight files (e.g., `insight1.txt`, `insight2.txt`)  

This step helps in understanding the dataset and discovering hidden patterns.

---

### 🔹 Visualization
Visualization is used to make the analysis easier to understand.

- Creating plots using Matplotlib  
- Visualizing distributions and feature relationships  
- Representing insights graphically  
- Saving plots (e.g., `summary_plot.png`)  

This helps in interpreting results visually.

---

### 🔹 Clustering
Clustering is applied to group similar data points together.

- Using machine learning algorithms such as K-Means  
- Grouping records based on similarity between features  
- Assigning each record to a cluster  
- Saving clustering results (`clusters.txt`)  

This helps in identifying different segments within the dataset.

---

### 🔹 Output Handling
All results generated during the pipeline are saved and organized.

- Processed datasets (CSV files)  
- Insight text files  
- Visualization images  
- Clustering results  

All outputs are stored inside the `results` folder for easy access.

---

## ▶️ How to Run

### 1. Build Docker Image
bash
docker build -t analytics_image .

### 2. Run Container
docker run -it --name analytics_container analytics_image

### 3. Inside Container
python ingest.py adult.csv

### 4. Outputs
Check results folder for:
- data_raw.csv
- data_preprocessed.csv
- insights
- clusters
- summary plot

## 👨‍💻 Authors
- Yasser Helal
- Habiba Mahdi
- Habiba Ramadan
- Marive Atef

### Build Image
![Build](images/build.png.jpeg)

### Run Container
![Run](images/run.png.jpeg)

### Push Image
![Push](images/push.png.jpeg)
