# # -- 코드를 입력하세요

select k.car_id as CAR_ID, round(k.duration, 1) as AVERAGE_DURATION
from (
select car_Id, sum(DATEDIFF(end_date, start_date)+1)/count(*) as duration
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id) K
where k.duration >= 7
group by car_id
order by average_duration desc, car_id desc


