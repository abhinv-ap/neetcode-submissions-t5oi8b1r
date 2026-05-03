-- Write your query below
select name from 
customers as c1
left join
orders as c2
on c1.id = c2.customer_id
where c2.customer_id is Null

