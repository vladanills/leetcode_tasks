# Write your MySQL query statement below
SELECT email 
FROM (
    SELECT email, count(email) as num
    FROM Person
    GROUP BY email) p
WHERE p.num > 1