import os
import pandas as pd

def transform_data():
    try:
        # Load data from the data/raw folder
        df = pd.read_csv('data/raw/apartmentsdata.csv')

        # 1. Fill missing values in the 'floor' column (keeping the original type)
        df.fillna({'floor': 'Nema Podataka'}, inplace=True)

        # 2. Fill missing values in other columns
        df.fillna({
            'area': df['area'].mean(),
            'price': df['price'].mean(),
            'rooms': df['rooms'].mean(),
            'square_price': df['square_price'].mean(),
            'location': 'Nema Podataka',
            'source': 'Nema Podataka',
            'title': 'Nema Podataka'
        }, inplace=True)

        # 3. Remove unnecessary rows
        df.dropna(subset=['city'], inplace=True)  # Remove rows where 'city' is missing

        # 4. Create the output directory if it doesn't exist
        os.makedirs('data/processed', exist_ok=True)

        # 5. Save the transformed data to a new CSV file
        output_path = 'data/processed/real_estate_transformed.csv'
        df.to_csv(output_path, index=False)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call the function
transform_data()


