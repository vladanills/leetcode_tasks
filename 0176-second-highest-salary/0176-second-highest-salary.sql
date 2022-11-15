# Write your MySQL query statement below
SELECT (SELECT distinct salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1) AS SecondHighestSalary