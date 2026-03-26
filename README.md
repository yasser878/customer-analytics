# Adult Project

## 📌 Description
This project analyzes customer data using Python and Docker.

## 🚀 Features
- Data ingestion
- Data preprocessing
- Generate insights
- Data visualization
- Clustering

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Docker
- ---

## 📌 Detailed Explanation

The project follows a complete data processing pipeline from raw data to meaningful insights.

### 🔹 Data Ingestion
The dataset (adult.csv) is loaded using Python scripts. The data is read into a structured format (DataFrame) for easier manipulation.

### 🔹 Data Preprocessing
In this step, the raw data is cleaned and prepared:
- Handling missing values
- Encoding categorical variables into numerical values
- Removing unnecessary data
- Preparing the dataset for analysis

### 🔹 Analytics & Insights
The processed data is analyzed to extract useful insights:
- Identifying patterns and trends
- Generating statistical summaries
- Creating insight files for better understanding

### 🔹 Visualization
Visualization helps in understanding the data:
- Creating plots using Matplotlib
- Showing relationships between features
- Saving results as images

### 🔹 Clustering
Clustering is applied to group similar data:
- Using algorithms like K-Means
- Grouping similar records together
- Saving clustering results

### 🔹 Output Handling
All outputs are saved in the results folder, including processed data, insights, visualizations, and clustering results.

## ▶️ How to Run

### 1. Build Docker Image
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
