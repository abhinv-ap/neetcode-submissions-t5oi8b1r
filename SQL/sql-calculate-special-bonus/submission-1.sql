-- Write your query below
select employee_id,
CASE
    when employee_id % 2 = 1 and name not like 'M%' THEN salary
    Else 0
END as bonus

from employees
order by employee_id
