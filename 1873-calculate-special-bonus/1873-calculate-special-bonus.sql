# Write your MySQL query statement below
SELECT employee_id, IF (MOD(employee_id,2)!=0 AND name NOT LIKE 'm%', salary, salary*0) AS bonus FROM Employees ORDER BY employee_id;