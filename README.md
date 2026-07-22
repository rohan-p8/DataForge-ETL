# 📊 DataForge ETL Pipeline

A modular **ETL (Extract, Transform, Load)** pipeline built with **Python**, **Pandas**, and **MySQL** that extracts sales data, validates and transforms it, and loads the cleaned data into a normalized relational database.

This project demonstrates production-oriented software engineering practices including modular architecture, transaction management, environment-based configuration, logging, and efficient batch database loading.

---

## 🚀 Features

- Extract sales data from CSV files
- Validate input data before processing
- Transform and clean raw data
- Remove duplicate records
- Standardize column names
- Remove unnecessary spaces
- Convert text values to Title Case
- Save processed data as CSV
- Load data into a normalized MySQL database
- Batch insert using `executemany()`
- Idempotent ETL using `INSERT IGNORE`
- Transaction management using `commit()` and `rollback()`
- Environment variable configuration using `.env`
- Logging for ETL execution
- Modular and maintainable project structure

---

# 🏗️ ETL Workflow

```
Raw CSV
   │
   ▼
Extract
   │
   ▼
Validate
   │
   ▼
Transform
   │
   ▼
Processed CSV
   │
   ▼
Load into MySQL
   │
   ▼
Customers
Products
Transactions
```

---

# 📂 Project Structure

```
DataForge-ETL/
│
├── config/
│   ├── __init__.py
│   ├── database.py
│   └── settings.py
│
├── data/
│   ├── archive/
│   ├── processed/
│   │   └── sales_july_processed.csv
│   ├── raw/
│   │   ├── sales_july.csv
│   │   └── sales_july.json
│
├── database/
│
├── docs/
│   └── learning_notes.md
│
├── etl/
│   ├── extractor.py
│   ├── validator.py
│   ├── transformer.py
│   └── loader.py
│
├── logs/
│   └── etl.log
│
├── sql/
│   └── schema.sql
│
├── tests/
│
├── utils/
│   ├── __init__.py
│   └── logger.py
│
├── .env
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

# 🛠️ Technologies Used

- Python 3
- Pandas
- MySQL
- mysql-connector-python
- python-dotenv
- Logging Module
- Git
- GitHub

---

# 🗄️ Database Schema

The ETL loads data into a normalized relational database.

## Customers

| Column | Type |
|---------|------|
| customer_id | INT (Primary Key) |
| customer_name | VARCHAR(100) |

---

## Products

| Column | Type |
|---------|------|
| product_id | INT (Primary Key, AUTO_INCREMENT) |
| product_name | VARCHAR(100) UNIQUE |

---

## Transactions

| Column | Type |
|---------|------|
| transaction_id | INT (Primary Key) |
| customer_id | INT (Foreign Key) |
| product_id | INT (Foreign Key) |
| quantity | INT |
| unit_price | DECIMAL(10,2) |
| transaction_date | DATE |

---

# 🔄 ETL Process

## 1. Extract

- Read sales data from CSV
- Load data into a Pandas DataFrame

---

## 2. Validate

- Validate required columns
- Check missing values
- Validate positive numeric values

---

## 3. Transform

- Standardize column names
- Remove extra spaces
- Convert text to Title Case
- Remove duplicate rows

---

## 4. Load

Load cleaned data into:

- Customers
- Products
- Transactions

using efficient batch inserts.

---

# ⚡ Performance Optimizations

- Batch insertion using `executemany()`
- Single database connection
- Centralized transaction management
- `INSERT IGNORE` for duplicate handling
- Environment variable configuration
- Modular ETL architecture

---

# 🔒 Environment Variables

Database credentials are stored in a `.env` file.

Example:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=dataforge_etl
DB_PORT=3306
```

The `.env` file is excluded from Git using `.gitignore`.

---

# 📂 SQL Schema

Database creation script is available in:

```
sql/schema.sql
```

Run this script before executing the ETL pipeline.

---

# ▶️ Installation

## Clone Repository

```bash
git clone https://github.com/rohan-p8/DataForge-ETL.git
```

---

## Move into Project

```bash
cd DataForge-ETL
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Copy

```
.env.example
```

to

```
.env
```

Update your MySQL credentials.

---

## Create Database

Run

```
sql/schema.sql
```

inside MySQL.

---

## Run the ETL Pipeline

```bash
python main.py
```

---

# 📄 Sample Input

```csv
customer_id,transaction_id,customer_name,product_name,quantity,unit_price,transaction_date

1,1001,Rohan,Laptop,2,65000,2026-07-01
2,1002,Amit,Mouse,1,700,2026-07-01
```

---

# 📊 Output

### Processed CSV

- Duplicate-free data
- Standardized columns
- Clean dataset

### MySQL Database

- Customers Table
- Products Table
- Transactions Table

---

# 💻 Software Engineering Practices

- Modular Project Architecture
- Single Responsibility Principle (SRP)
- Environment Variable Configuration
- Exception Handling
- Logging
- Batch Processing
- Transaction Management
- Idempotent ETL
- Version Control using Git

---

# 🚀 Future Improvements

- Support Excel files
- Support REST APIs
- Docker containerization
- Apache Airflow scheduling
- Cloud database integration
- Automated Data Quality Report

---

# 👨‍💻 Author

**Rohan Patil**

GitHub: https://github.com/rohan-p8

Linkedin: https://www.linkedin.com/in/rohan-patil-network

---

## ⭐ If you found this project useful, consider giving it a star!