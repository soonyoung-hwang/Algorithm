-- 코드를 입력하세요


SELECT A.animal_id, A.name
from ANIMAL_INS A, ANIMAL_OUTS B
where A.animal_id = B.animal_id
order by (B.datetime - A.datetime) DESC
limit 2
