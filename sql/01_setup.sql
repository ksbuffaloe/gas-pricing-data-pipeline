CREATE TABLE IF NOT EXISTS raw_prices (
    id SERIAL PRIMARY KEY,
    period DATE,
    duoarea TEXT,
    area_name TEXT,
    product TEXT,
    product_name TEXT,
    process TEXT,
    process_name TEXT,
    series TEXT,
    series_description TEXT,
    value NUMERIC,
    units TEXT,
    inserted_at TIMESTAMP DEFAULT NOW()
);


CREATE TABLE IF NOT EXISTS clean_prices (
    id SERIAL PRIMARY KEY,
    period DATE,
    product TEXT,
    product_name TEXT,
    series_description TEXT,
    value NUMERIC,
    ingestion_timestamp TIMESTAMP DEFAULT NOW()
);

