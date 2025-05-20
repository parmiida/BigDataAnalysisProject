# BigDataAnalysisProject
# Anomaly Detection in Streaming Time-Series Data

This project is the final assignment for the Big Data Analytics course. It implements a simple pipeline to detect anomalies in streaming time-series data using Apache Kafka and Apache Spark.

## 🔧 Technologies Used
- Apache Kafka
- Apache Spark (Structured Streaming)
- Python
- Pandas

## 📌 Project Overview
The goal is to simulate a real-time data stream and process it to identify anomalies based on sudden value deviations. A dataset of time-series events is streamed to Kafka in batches. Spark reads the stream, processes the records, and flags outliers using a threshold-based method.

## 📈 Pipeline Steps

### 1. Data Streaming with Kafka
- A CSV file (`timeseries.csv`) is read using Python and Pandas.
- The data is sent in batches of 100 records to a Kafka topic (`T4`).
- Each record contains `id`, `date`, `value`, and `label` fields.

### 2. Real-Time Data Ingestion with Spark
- Spark reads the Kafka topic as a stream.
- The value column (JSON string) is parsed into structured fields using a defined schema.
- The data is split and deserialized to retrieve individual records.

### 3. Anomaly Detection
- A `lag` function is used to compare each value with the previous one.
- The absolute difference is calculated.
- If the difference exceeds a defined threshold (e.g., 400), the record is flagged as an anomaly.
- The results are displayed in the console.

## 🧪 Example Output
The output includes the following fields:
- `id`
- `value`
- `label`
- `prev_value`
- `value_diff`
- `detection` (1 for anomaly, 0 otherwise)

## ⚠️ Limitations
- The current detection method is basic and purely threshold-based.
- The accuracy of this approach is limited and may result in false positives or negatives.

## 🚀 Future Improvements
- Use statistical or machine learning-based anomaly detection techniques.
- Store the results in a persistent sink (e.g., database or file system).
