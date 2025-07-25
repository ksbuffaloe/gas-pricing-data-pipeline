-- clear previous data in clean_prices table
DELETE FROM clean_prices;

-- transform data from raw_prices to clean_prices
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
  value::NUMERIC,
  NOW()  -- adds the current timestamp for this cleaning run
FROM
  raw_prices
WHERE
  value IS NOT NULL;
