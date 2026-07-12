# Automated SQL Data Extraction Workflow

## Overview

This project automates the process of extracting data from a SQL Server database using Python. Instead of manually connecting to the database, running SQL queries, exporting results, and creating reports, the script performs the entire workflow automatically.

The project demonstrates a beginner-friendly ETL (Extract, Transform, Load) automation pipeline and showcases the integration of Python, SQL Server, Pandas, logging, email notifications, and Windows Task Scheduler.

---

## Problem Statement

Organizations frequently need to extract data from databases for reporting and analysis. Performing this task manually every day is repetitive, time-consuming, and prone to human error.

This project automates the extraction process by:

* Connecting to a SQL Server database
* Executing SQL queries
* Loading the results into a Pandas DataFrame
* Exporting the data to a CSV file
* Recording execution details in a log file
* Sending email notifications about the execution status
* Supporting scheduled execution using Windows Task Scheduler

---

## Features

* SQL Server database connectivity using `pyodbc`
* Automatic SQL query execution
* Data extraction into Pandas DataFrames
* CSV export
* Logging for monitoring and debugging
* Error handling using `try-except`
* Email notifications for success or failure
* Ready for scheduled execution with Windows Task Scheduler

---

## Technologies Used

* Python
* SQL Server Express (`.\SQLEXPRESS`)
* Pandas
* pyodbc
* Logging
* SMTP (Email)
* Windows Task Scheduler

---

## Project Workflow

```text
SQL Server Database
        │
        ▼
Python Script
        │
        ▼
Execute SQL Query
        │
        ▼
Pandas DataFrame
        │
        ▼
Export to CSV
        │
        ▼
Write Log File
        │
        ▼
Send Email Notification
        │
        ▼
Scheduled Execution (Optional)
```

---

## Project Structure

```text
AUTOMATION/
│
├── automate_extraction.py
├── config_example.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

> **Note:** `config.py` is intentionally excluded from the repository because it contains local database and email credentials.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project folder:

```bash
cd AUTOMATION
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Create a `config.py` file using `config_example.py` as a template and update it with your SQL Server and email configuration.

Run the script:

```bash
python automate_extraction.py
```

---

## Expected Output

After successful execution, the project will:

* Connect to the SQL Server database
* Execute the SQL query
* Extract data into a Pandas DataFrame
* Generate a CSV file containing the extracted data
* Create or update the log file
* Send an email notification (if configured)

---

## Screenshots

Include screenshots such as:

* SQL Server database table
* Successful script execution
* Generated CSV file
* Log file
* Windows Task Scheduler
* Email notification (optional)

---

## Future Improvements

* Export reports to Excel
* Add automatic data transformation
* Load processed data back into SQL Server
* Support multiple database systems
* Integrate with Power BI dashboards
* Schedule execution using Apache Airflow

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Connecting Python to SQL Server
* Executing SQL queries from Python
* Working with Pandas DataFrames
* Exporting data to CSV
* Implementing logging and error handling
* Sending automated email notifications
* Scheduling scripts using Windows Task Scheduler
* Building a simple ETL automation workflow

---

## Author

**Yuva Kotipalli**
