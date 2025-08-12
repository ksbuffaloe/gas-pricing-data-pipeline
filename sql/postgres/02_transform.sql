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
  value,
  CURRENT_TIMESTAMP
FROM
  raw_prices
WHERE
  value IS NOT NULL;
