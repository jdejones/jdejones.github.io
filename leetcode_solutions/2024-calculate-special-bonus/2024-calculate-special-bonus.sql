# Write your MySQL query statement below
SELECT
  employee_id,
  (employee_id % 2 <> 0
   AND name NOT LIKE 'M%'
  ) * salary
  bonus
FROM Employees
ORDER BY employee_id;
