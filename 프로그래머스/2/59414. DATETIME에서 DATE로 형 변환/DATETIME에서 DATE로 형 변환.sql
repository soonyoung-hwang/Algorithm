-- 코드를 입력하세요
SELECT animal_id, name, date_format(DATETIME, '20%y-%m-%d') as '날짜'
from ANIMAL_INS
order by animal_id