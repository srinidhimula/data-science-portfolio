-- Overall Market Summary
-- Purpose: High-level KPIs for executive dashboard

SELECT 
    COUNT(*) as total_inventory,
    COUNT(DISTINCT brand) as unique_brands,
    ROUND(AVG(price_cleaned), 2) as avg_price,
    ROUND(MIN(price_cleaned), 2) as min_price,
    ROUND(MAX(price_cleaned), 2) as max_price
FROM watchdata_cleaned;

-- Top 10 Most Expensive Watches
-- Purpose: Identify premium inventory
SELECT 
    brand,
    model,
    ref_cleaned,
    price_cleaned,
    year,
    CASE 
        WHEN has_box_papers=1 THEN 'Full Set'
        WHEN has_box_papers=0 THEN 'Watch Only'
    END as documentation
FROM watchdata_cleaned
ORDER BY price_cleaned DESC
LIMIT 10;

-- Average Price by Brand
-- Purpose: Brand positioning analysis
SELECT 
    brand,
    COUNT(*) as watch_count,
    ROUND(AVG(price_cleaned), 2) as avg_price,
    ROUND(MIN(price_cleaned), 2) as min_price,
    ROUND(MAX(price_cleaned), 2) as max_price,
    ROUND(STDDEV(price_cleaned), 2) as price_std_dev
FROM watchdata_cleaned
GROUP BY brand
HAVING COUNT(*) >= 5  -- Only brands with 5+ watches
ORDER BY avg_price DESC;

-- Price Premium for Documentation (Box & Papers)
-- Purpose: Quantify value of complete documentation
SELECT 
    brand,
    ROUND(AVG(CASE WHEN has_box AND has_papers THEN price END), 2) as avg_price_full_set,
    ROUND(AVG(CASE WHEN NOT (has_box AND has_papers) THEN price END), 2) as avg_price_incomplete,
    ROUND(
        AVG(CASE WHEN has_box AND has_papers THEN price END) - 
        AVG(CASE WHEN NOT (has_box AND has_papers) THEN price END), 
        2
    ) as documentation_premium,
    COUNT(*) as total_watches
FROM watches
WHERE brand IN ('Rolex', 'Patek Philippe', 'Omega', 'Audemars Piguet')
GROUP BY brand
ORDER BY documentation_premium DESC;


-- Brand Segment Analysis
-- Purpose: Compare performance across your engineered segments
SELECT 
    brand_segment,
    COUNT(*) as watch_count,
    ROUND(AVG(price), 2) as avg_price,
    ROUND(MIN(price), 2) as segment_min,
    ROUND(MAX(price), 2) as segment_max,
    COUNT(DISTINCT brand) as brands_in_segment
FROM watches
WHERE brand_segment IS NOT NULL
GROUP BY brand_segment
ORDER BY avg_price DESC;