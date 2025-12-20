SELECT COUNT(*) as total_watches FROM watchdata_cleaned;

SELECT 
    brand,
    COUNT(*) as count,
    AVG(price_cleaned) as avg_price,
    MIN(year) as earliest_year,
    MAX(year) as latest_year
FROM watchdata_cleaned
GROUP BY brand
ORDER BY count DESC
LIMIT 10;