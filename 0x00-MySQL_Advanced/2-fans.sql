-- SQL script to rank country origins of bands by the number of (non-unique) fans

-- Assuming metal_bands table has columns:
-- band_name (name of the band)
-- origin (country of the band)
-- fans (number of fans)

-- Rank country origins of bands by the number of (non-unique) fans
SELECT 
    origin, 
    SUM(fans) AS nb_fans
FROM 
    metal_bands
GROUP BY 
    origin
ORDER BY 
    nb_fans DESC;
