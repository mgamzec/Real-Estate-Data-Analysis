# Real Estate Data Analysis

<img width="1650" height="1083" alt="image" src="https://github.com/user-attachments/assets/c9a3c7ba-5733-4e26-8106-51b062e4527f" />


This project implements a comprehensive ETL (Extract, Transform, Load) pipeline to analyze real estate data. It automates the entire process, from fetching raw data to generating valuable analytical insights. The pipeline fetches a dataset from Kaggle, cleans and processes it with Python and SQL, and stores the final data in a PostgreSQL database.

It fetches data from **Kaggle**, processes it using Python and SQL, and stores it in a **PostgreSQL** database. Analytical **SQL views** are created to extract insights such as 10 cheapest 4-bedroom properties for my two favorite cities, 10 most expensive properties, 10 most cheapest properties and more.

## **Project Structure**

- **`data/`**: Contains raw (`raw/`) and processed (`processed/`) data.
- **`scripts/`**:
  - `extract.py`: Fetches the dataset from Kaggle using the Kaggle API.
  - `transform.py`: Cleans data who have empty values.
  - `load.py`: Loads the processed data into the PostgreSQL database.
- **`sql/`**:
  - `create_table.sql`: Defines the database schema for the `real_estate` table.
  - `analysis_queries.sql`: Contains SQL queries to create analytical views.
- **`run_etl.py`**: Runs the entire ETL process in one step.
- **`.env`**: Environment variables for PostgreSQL which is needed to be created.
- **`requirements.txt`**: Python dependencies for the project.
- **`README.md`**: Project documentation.

## Installation

1. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate     # On Windows
    ```
2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Start program**:
    ```bash
    python3 run_etl.py
    ``` 

### Setting Up PostgreSQL

Install PostgreSQL: Download PostgreSQL(https://www.postgresql.org/download/).

Log in to PostgreSQL:
```bash
psql -U your_postgres_username
``` 
Create the database:
```bash
CREATE DATABASE your_postgres_database_name;
```

### 3. Creating the `.env` File

In the root of the project, create a file named `.env` and add the following environment variables:

```dotenv
# PostgreSQL Configuration
POSTGRES_DB=your_postgres_database_name
POSTGRES_USER=your_postgres_username
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_HOST=localhost  # or your host
POSTGRES_PORT=5432       # or your custom port
```  



