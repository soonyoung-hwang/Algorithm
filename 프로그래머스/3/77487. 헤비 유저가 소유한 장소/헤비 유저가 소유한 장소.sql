-- 코드를 입력하세요
SELECT B.id, b.name, b.host_id
from 
    (select host_id
    from places
    group by host_id
    having count(*) >= 2) K, places B
where K.host_id = B.host_id
order by b.id