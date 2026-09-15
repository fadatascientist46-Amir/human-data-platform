# Human Data Engineering Platform

## 1. What is the Problem?

A company has a lot of data about what users do on its applications.

For example, users can:

- Login
- Search
- Click
- View a page
- Buy something
- Give feedback
- Logout

Every action creates data.

The problem is that this data comes from many different places.

For example:

Web Application
Mobile Application
Database
API
Files

The company needs one system to collect, process, clean, store,
and analyze all this data.

---

# 2. Why Do We Need This Project?

Without a proper Data Engineering platform, the company can have:

- Data in different places
- Duplicate data
- Missing data
- Incorrect data
- Slow reports
- Difficulty processing large amounts of data
- No real-time information
- Difficult data analysis

Our project solves these problems.

---

# 3. What Will Our Project Do?

Our project will:

1. Collect user activity data.
2. Receive some data in real time.
3. Receive some data in batch.
4. Process large amounts of data.
5. Clean bad data.
6. Remove duplicate data.
7. Store raw data.
8. Store cleaned data.
9. Create useful business data.
10. Make the data available for analysis.

---

# 4. Simple Example

Suppose a user opens a shopping application.

The user does this:

Login
↓
Search for phone
↓
View phone
↓
Click Buy
↓
Purchase

Each action creates an event.

Example:

{
  "user_id": "U1001",
  "event_type": "search",
  "page": "products"
}

Another event:

{
  "user_id": "U1001",
  "event_type": "purchase",
  "page": "checkout"
}

Our platform collects these events.

---

# 5. How Will We Collect Real-Time Data?

We will use Kafka.

Simple flow:

User Activity
      ↓
     Kafka
      ↓
     Spark

Kafka is used to receive and temporarily hold
large numbers of real-time events.

---

# 6. How Will We Process the Data?

We will use PySpark.

Simple flow:

Kafka
  ↓
PySpark
  ↓
Clean Data
  ↓
Transform Data
  ↓
Store Data

PySpark allows us to process large amounts of data
using distributed computing.

---

# 7. Where Will We Store the Data?

We will use Databricks and Delta Lake.

We will create three layers.

Bronze
  ↓
Silver
  ↓
Gold

## Bronze

Bronze contains the original/raw data.

Example:

User event exactly as it arrived.

## Silver

Silver contains cleaned data.

For example:

- Remove duplicates
- Fix data types
- Handle missing values
- Validate events

## Gold

Gold contains useful business data.

For example:

- Daily active users
- Number of purchases
- Events by country
- Events by device
- Events by event type

---

# 8. Why Do We Need Batch Processing?

Not all data arrives in real time.

For example, a company may have an old file containing
one year of historical user activity.

We need to process this old data too.

We will use:

Airflow
   ↓
PySpark
   ↓
Databricks

Airflow will schedule and control our batch pipelines.

---

# 9. What About PostgreSQL and MongoDB?

We will use two types of databases.

PostgreSQL
→ SQL / relational database

MongoDB
→ NoSQL / document database

This helps us learn how to bring data from different
database systems into our Data Engineering platform.

---

# 10. What is Data Quality?

Data quality means making sure our data is correct and usable.

For example, this is bad data:

{
  "user_id": null,
  "event_type": "unknown"
}

We need to detect it.

We will check:

- Missing values
- Duplicate events
- Invalid event types
- Wrong data types
- Invalid timestamps

---

# 11. What is Data Governance?

Some human data can be sensitive.

For example:

- Email
- Phone number
- User information

We need to protect this data.

We will learn:

- Data masking
- Access control
- PII identification
- Audit logging

---

# 12. What is Monitoring?

We need to know whether our pipeline is working.

For example:

Kafka
  ↓
Spark
  ↓
Databricks

What if Spark stops?

We need to know.

We will monitor:

- Pipeline status
- Number of records
- Failed records
- Processing time
- Kafka lag
- Data quality errors

---

# 13. What is Scalability?

Suppose today we have:

1,000 events per second.

Tomorrow we have:

10,000 events per second.

Later:

100,000 events per second.

Our system should continue working.

Kafka and Spark help us process larger amounts of data.

---

# 14. Main Technology Stack

Python
→ Programming

Kafka
→ Real-time data ingestion

PySpark
→ Big data processing

Databricks
→ Data platform

Delta Lake
→ Data storage

Airflow
→ Pipeline scheduling

PostgreSQL
→ SQL database

MongoDB
→ NoSQL database

Docker
→ Containerization

Kubernetes
→ Container management

Prometheus + Grafana
→ Monitoring

Git + GitHub
→ Version control

---

# 15. Final Project Flow

Real-Time:

User Activity
      ↓
    Kafka
      ↓
PySpark Streaming
      ↓
   Bronze
      ↓
   Silver
      ↓
    Gold
      ↓
 Databricks
      ↓
 Analytics


Batch:

Historical Data
      ↓
   Airflow
      ↓
PySpark Batch
      ↓
Bronze → Silver → Gold
      ↓
 Databricks

---

# 16. Main Goal

The main goal of this project is:

Build a complete Data Engineering platform that can
collect, process, clean, store, monitor, and provide
large amounts of human-generated data for analysis.

---

# 17. Skills We Will Learn

By completing this project, we will practice:

- Python
- SQL
- Kafka
- PySpark
- Spark Streaming
- Batch Processing
- Databricks
- Delta Lake
- Airflow
- PostgreSQL
- MongoDB
- Data Quality
- Data Governance
- Data Security
- Monitoring
- Docker
- Kubernetes
- Git
- CI/CD