CREATE TABLE IF NOT EXISTS raw_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    period DATE,
    duoarea TEXT,
    area_name TEXT,
    product TEXT,
    product_name TEXT,
    process TEXT,
    process_name TEXT,
    series TEXT,
    series_description TEXT,
    value REAL,
    units TEXT,
    inserted_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS clean_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    period DATE,
    product TEXT,
    product_name TEXT,
    series_description TEXT,
    value REAL,
    ingestion_timestamp TEXT DEFAULT (datetime('now'))
);
