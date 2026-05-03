-- Write your query below
select p.name,p.travelled_distance 
from(select u.name ,coalesce(sum(distance),0) as travelled_distance from 
users as u left join rides as r on u.id=r.user_id
group by u.id) as p
order by p.travelled_distance DESC , p.name
