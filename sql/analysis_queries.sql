-- View for 10 cheapest cities per square meter
CREATE VIEW cheapest_cities_sqm AS
SELECT 
    city,
    COUNT(*) AS num_samples,
    ROUND(AVG(price / area), 2) AS avg_price_per_sqm
FROM 
    real_estate
WHERE 
    area > 0 
GROUP BY 
    city
HAVING 
    COUNT(*) >= 10 
ORDER BY 
    avg_price_per_sqm ASC
LIMIT 10;

-- View for 10 most expensive cities per square meter
CREATE VIEW most_expensive_cities_sqm AS
SELECT 
    city,
    COUNT(*) AS num_samples,
    ROUND(AVG(price / area), 2) AS avg_price_per_sqm
FROM 
    real_estate
WHERE 
    area > 0 
GROUP BY 
    city
HAVING 
    COUNT(*) >= 10 
ORDER BY 
    avg_price_per_sqm DESC
LIMIT 10;

--View for average prices by real estate source
CREATE VIEW avg_price_by_source AS
SELECT 
    source,
    COUNT(*) AS num_samples,
    ROUND(AVG(price), 2) AS avg_price
FROM 
    real_estate
WHERE 
    source IS NOT NULL
GROUP BY 
    source
HAVING 
    COUNT(*) >= 10
ORDER BY 
    avg_price DESC;

-- View for average prices per square meter per area 
CREATE VIEW avg_price_per_sqm_by_area AS
SELECT 
    area,
    COUNT(*) AS num_samples,
    ROUND(AVG(price / area), 2) AS avg_price_per_sqm
FROM 
    real_estate
WHERE 
    area > 0
GROUP BY 
    area
HAVING 
    COUNT(*) >= 10
ORDER BY 
    avg_price_per_sqm DESC;

-- Views for the 10 most expensive properties
CREATE VIEW top_10_most_expensive_properties AS
SELECT 
    city,
    area,
    price,
    rooms,
    floor,
    location,
    source,
    title
FROM 
    real_estate
ORDER BY 
    price DESC
LIMIT 10;

-- Views for the 10 most cheapest properties
CREATE VIEW top_10_most_cheapest_properties AS
SELECT 
    city,
    area,
    price,
    rooms,
    floor,
    location,
    source,
    title
FROM 
    real_estate
ORDER BY 
    price ASC
LIMIT 10;

-- Views for the 10 most largest properties
CREATE VIEW top_10_largest_properties AS
SELECT 
    city,
    area,
    price,
    rooms,
    floor,
    location,
    source,
    title
FROM 
    real_estate
ORDER BY 
    area DESC
LIMIT 10;

-- Views for the 10 most smallest properties
CREATE VIEW top_10_smallest_properties AS
SELECT 
    city,
    area,
    price,
    rooms,
    floor,
    location,
    source,
    title
FROM 
    real_estate
ORDER BY 
    area ASC
LIMIT 10;

-- Views for the 10 cheapest 4 bedroom properties for my 2 favorite cities which I am interested in 
CREATE VIEW cheapest_4_room_properties_2_favorite_cities AS
SELECT
    city,
    area,
    price,
    rooms,
    location,
    source,
    square_price,
    title
FROM
    real_estate
WHERE
    rooms = 4
    AND city IN ('Beograd', 'Pančevo')
ORDER BY
    price ASC
LIMIT 10;


