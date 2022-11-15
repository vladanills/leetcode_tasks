# Write your MySQL query statement below
SELECT DISTINCT num as ConsecutiveNums 
FROM 
(   SELECT num, 
    LEAD(num) OVER(ORDER BY id) as 'lead',
    LAG(num) OVER(ORDER BY id) as 'lag'
    FROM Logs) v
WHERE v.num = v.lag and v.num = v.lead
