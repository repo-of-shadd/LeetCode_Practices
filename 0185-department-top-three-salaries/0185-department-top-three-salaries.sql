# Write your MySQL query statement below
Select  a.Department,a.Employee, a.Salary
From (SELECT E.id, 
                    E.name AS Employee, 
                    E.salary AS Salary, 
                    E.departmentId, 
                    DP.name AS Department,
                    DENSE_RANK() OVER(PARTITION BY DP.name ORDER BY E.salary DESC) AS DR 
             FROM Employee AS E 
             JOIN Department AS DP ON E.departmentId = DP.id) a
             
WHERE   a.DR <= 3;