# 🏨 Hotel Management ML Project - MLOps Pipeline (AWS-Based)

This project is part of my hands-on practice inspired by the Udemy course  
**"Beginner to Advanced MLOps on GCP - CI/CD, Kubernetes, Jenkins"** by **Krish Naik**.

## 📌 Project Overview

The goal of this project is to build and deploy a machine learning model that predicts hotel booking demand or assists in hotel management decisions. The project demonstrates how to take an ML model from development to production using a full **MLOps pipeline**.

> **Note**: While the course uses **GCP**, all cloud infrastructure in this project has been implemented using **AWS** services.

## ⚙️ Key Components

- 🧠 **Model Development**: Training a machine learning model for hotel booking demand prediction using Python and scikit-learn.
- 🐳 **Dockerization**: Packaging the model and inference script into a Docker container.
- ☸️ **Kubernetes Deployment**: Deploying the Dockerized application to a Kubernetes cluster (EKS on AWS).
- 🔧 **CI/CD Integration**: Automating the build and deployment pipeline using **Jenkins**.
- 🌐 **API Service**: Exposing the model as a REST API using **Flask**.
- 📦 **Version Control & Pipeline Automation**: Managing code with **Git**, and automating steps from model training to deployment.
- ⚙️ **Configuration Management**: Storing AWS credentials and data ingestion settings (e.g., S3 bucket name, file name) in a `config.yaml` file, loaded using `pyyaml`. The `config.yaml` file is excluded from version control using `.gitignore` to prevent exposing sensitive information like AWS access keys.

## 🎯 Objectives

- Learn how to implement the **end-to-end MLOps lifecycle**  
- Understand infrastructure-as-code principles in a cloud-native environment  
- Practice real-world ML deployment using **AWS**, **Jenkins**, **Docker**, and **Kubernetes**

## 🚀 Technologies Used

- Python (scikit-learn, pandas, Flask, pyyaml)
- Docker
- Kubernetes (AWS EKS)
- Jenkins
- Git & GitHub
- AWS (IAM, S3)

## 🛠️ Setup Instructions

**1. Clone the Repository**


**2. Install Dependencies:**
```pip install -e .```

**3. Configure AWS Credentials:**

Create a config.yaml file in the project root based on the example below.
Ensure the file is added to `.gitignore` to prevent committing sensitive data.

Example config.yaml:
```
aws:
  access_key_id: YOUR_AWS_ACCESS_KEY_ID
  secret_access_key: YOUR_AWS_SECRET_ACCESS_KEY
  default_region: us-east-2

data_ingestion:
  bucket_name: your-s3-bucket
  bucket_file_name: data.csv
  train_ratio: 0.8
```

**4. Run the Data Ingestion Script:**
`python data_ingestion.py`

This downloads the dataset from S3 and splits it into training and test sets.

**5. Deploy the Application:**

Build the Docker image and deploy to AWS EKS using Jenkins as described in the pipeline configuration.



## 📚 Reference

- Course: [Beginner to Advanced MLOps on GCP - CI/CD, Kubernetes, Jenkins](https://www.udemy.com/course/beginner-to-advanced-mlops-on-gcp-cicd-kubernetes-jenkins/)  
  by **Krish Naik**

---

This project showcases a real-world scenario of taking a machine learning model into production using modern MLOps tools and practices, adapted for AWS.