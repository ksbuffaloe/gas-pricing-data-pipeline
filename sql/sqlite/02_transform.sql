-- Clear out the old data in clean_prices table
-- and insert cleaned data from raw_prices table
DELETE FROM clean_prices;

INSERT INTO clean_prices (
  period,
  product,
  product_name,
  series_description,
  value,
  ingestion_timestamp
)
SELECT
  period,
  LOWER(TRIM(product)),
  LOWER(TRIM(product_name)),
  LOWER(TRIM(series_description)),
  value REAL,
  datetime('now')
FROM
  raw_prices
WHERE
  value IS NOT NULL;
