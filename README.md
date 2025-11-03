# 🚀 Airflow Lab 1 — Cloud Composer Tutorial

## 📘 Overview
This lab introduces you to **Apache Airflow** and **Google Cloud Composer** through a simple Directed Acyclic Graph (DAG).  
You’ll learn how to:
- Create a DAG definition file.  
- Add tasks using different operators (`BashOperator`, `PythonOperator`).  
- Define task dependencies.  
- Trigger and monitor DAG runs in Cloud Composer or Airflow UI.

---

## 🗂️ File Structure
```
airflow_lab1/
 ├── airflow_lab1.py     # DAG definition file
 └── README_Airflow_Lab1.md            # Documentation
```

---

## 🧠 DAG Description
The DAG named **`cloud_composer_tutorial_v2`** contains two tasks:

1. **Task 1 – show_system_info (BashOperator)**  
   Prints the current system date/time and working directory.
   ```bash
   echo "Current Date and Time:" && date && echo "Current Directory:" && pwd
   ```

2. **Task 2 – calculate_days_until_new_year (PythonOperator)**  
   Uses Python to calculate how many days and hours remain until **January 1, 2026**.

**Task Flow:**  
```
show_system_info → calculate_days_until_new_year
```

---

## ⚙️ Setup Instructions

### Step 1: Upload the DAG
- Open **Google Cloud Console** → **Composer** → **Environments**.
- Navigate to the **DAGs folder** in the environment’s GCS bucket.
- Upload `airflow_lab1.py` there.

### Step 2: Verify in Airflow UI
- Go to the **Airflow Web UI** (link available from your Composer environment).
- Search for the DAG ID: `cloud_composer_tutorial_v2`.
- Toggle the DAG to **“On”** to make it active.

### Step 3: Trigger the DAG
- In Airflow UI, click **Trigger DAG**.
- Monitor execution under **Graph View** or **Task Logs**.

---

## 📊 Expected Output

**Task 1 (`show_system_info`)**  
- Logs show the current system time and working directory path.  
Example:
```
Current Date and Time:
Mon Nov 3 15:25:10 UTC 2025
Current Directory:
/home/airflow/gcs/dags
```

**Task 2 (`calculate_days_until_new_year`)**  
- Logs show a message similar to:
```
There are 59 days and 8 hours left until New Year 2026!
```

---

## 🧩 Key Concepts Learned
- How to define DAGs in Airflow.
- Using different operators (`BashOperator` and `PythonOperator`).
- Setting `default_args` and `start_date`.
- Managing dependencies with `>>` (task chaining).
- Deploying and running a DAG in **Google Cloud Composer**.

---

## 📅 Optional Enhancements
You can expand this lab by adding:
- A **FileSensor** to detect file availability before processing.  
- A **BranchPythonOperator** to conditionally execute tasks.  
- An **EmailOperator** to send notifications on success or failure.
