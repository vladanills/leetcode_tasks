# Write your MySQL query statement below
SELECT distinct l1.num as ConsecutiveNums
FROM logs l1, logs l2, logs l3
WHERE l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num