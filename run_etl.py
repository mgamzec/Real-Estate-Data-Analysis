import os
import subprocess

def run_etl():
    try:
        print("Starting ETL process...")

        # Step 1: Run extraction
        print("Running extraction...")
        subprocess.run(["python", "scripts/extract.py"], check=True)

        # Step 2: Run transformation
        print("Running transformation...")
        subprocess.run(["python", "scripts/transform.py"], check=True)

        # Step 3: Run loading
        print("Running loading...")
        subprocess.run(["python", "scripts/load.py"], check=True)

        print("ETL process completed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred during the ETL process: {e}")
        exit(1)

if __name__ == "__main__":
    run_etl()

