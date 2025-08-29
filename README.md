# Real Estate Data Analysis

This project implements a comprehensive ETL (Extract, Transform, Load) pipeline to analyze real estate data. It automates the entire process, from fetching raw data to generating valuable analytical insights. The pipeline fetches a dataset from Kaggle, cleans and processes it with Python and SQL, and stores the final data in a PostgreSQL database.

The core value of this project lies in its ability to transform raw data into actionable insights through predefined analytical SQL views. These views provide quick access to key information, such as:

The 10 most affordable 4-bedroom properties in your favorite cities.

The 10 most expensive properties on the market.

The 10 most affordable properties overall.

📁 Project Structure
The project is organized into a logical directory structure to streamline the ETL process.

data/: Stores the dataset files, with subdirectories for raw/ (the original data from Kaggle) and processed/ (the cleaned data ready for loading).

scripts/: Contains the Python scripts that drive the ETL pipeline.

extract.py: Utilizes the Kaggle API to download the raw dataset.

transform.py: Cleans the data by handling missing or empty values.

load.py: Inserts the processed data into the PostgreSQL database.

run_etl.py: A single-entry point script that executes the entire ETL process in sequence.

sql/: Houses the SQL scripts for database management and analysis.

create_table.sql: Defines the database schema for the real_estate table.

analysis_queries.sql: Contains the queries used to create the analytical views for insight generation.

.env: The file where you'll store your sensitive environment variables (e.g., database credentials).

requirements.txt: Lists all Python libraries required for the project.

README.md: This documentation file.

🛠️ Installation & Setup
To get this project up and running, follow these steps.

1. Clone the Repository
First, clone the project from GitHub to your local machine:

Bash

git clone https://github.com/brankowss/Real-Estate-ETL
cd Real-Estate-ETL
2. Set Up a Virtual Environment
It's best practice to use a virtual environment to manage dependencies.

Bash

python3 -m venv venv
Activate the environment:

On macOS/Linux: source venv/bin/activate

On Windows: venv\Scripts\activate

3. Install Python Dependencies
Install all the necessary libraries using the requirements.txt file:

Bash

pip install -r requirements.txt
🚀 Running the Program
Once all the setup steps are complete, you can run the full ETL pipeline with a single command:

Bash

python3 run_etl.py
⚙️ Configuration
Before running the program, you must configure a few essential components: your Kaggle API token and your PostgreSQL database.

1. Configure the Kaggle API
You need a Kaggle account and an API token to download the dataset.

Sign up for a free account at Kaggle.

Go to your account settings (Account > API).

Click Create New API Token to download a kaggle.json file.

Move this file to the correct location on your system:

macOS/Linux:

Bash

mkdir -p ~/.kaggle
mv /path/to/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json # Set permissions
Windows:

Bash

mkdir $HOME\.kaggle
Move-Item -Path .\Downloads\kaggle.json -Destination $HOME\.kaggle\
2. Set Up PostgreSQL
If you don't have PostgreSQL installed, you can download it from the official website: Download PostgreSQL.

Log in to PostgreSQL:

Bash

psql -U your_postgres_username
Create the Database:

SQL

CREATE DATABASE your_postgres_database_name;
3. Create the .env File
Finally, create a .env file in the root of your project directory and add your PostgreSQL credentials. This keeps your sensitive information secure.

# PostgreSQL Configuration
POSTGRES_DB=your_postgres_database_name
POSTGRES_USER=your_postgres_username
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_HOST=localhost # Or your host address
POSTGRES_PORT=5432      # Or your custom port
