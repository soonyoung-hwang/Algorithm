-- 코드를 입력하세요
select user_id, product_id
from
(SELECT user_id, product_id, count(*)
from ONLINE_SALE
group by user_id, product_id
having count(*) >= 2) K
order by user_id, product_id desc