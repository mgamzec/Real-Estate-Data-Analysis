# Serbian Real Estate ETL Project

This project demonstrates an ETL pipeline for analyzing Serbian real estate data. It fetches data from **Kaggle**, processes it using Python and SQL, and stores it in a **PostgreSQL** database. Analytical **SQL views** are created to extract insights such as 10 cheapest 4-bedroom properties for my two favorite cities, 10 most expensive properties, 10 most cheapest properties and more.

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

1. **Clone the repository**:
   ```bash
   git clone https://github.com/brankowss/Real-Estate-ETL
   cd Real-Estate-ETL
   ```
2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate     # On Windows
    ```
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Start program**:
    ```bash
    python3 run_etl.py
    ``` 

## Setup

Before running the project, you need to sign up and configure your KaggleAPI token.

### 1. Setting Up the Kaggle API Token

Sign up for a free Kaggle account: Kaggle(https://www.kaggle.com/).
Go to Account Settings and select Create New API Token to download kaggle.json.
Move the kaggle.json file to the correct location:

```bash
# On Linux/Mac
mkdir -p ~/.kaggle 
mv /path/to/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# On Windows
mkdir $HOME\.kaggle
Move-Item -Path .\Downloads\kaggle.json -Destination $HOME\.kaggle\
``` 
### 2. Setting Up PostgreSQL

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



