-- Creating real_estate table
CREATE TABLE IF NOT EXISTS real_estate (
    id SERIAL PRIMARY KEY,
    area VARCHAR(255),
    city VARCHAR(255),
    floor VARCHAR(50),
    location VARCHAR(255),
    price NUMERIC,
    rooms INTEGER,
    source VARCHAR(255),
    square_price NUMERIC,
    title TEXT
);




