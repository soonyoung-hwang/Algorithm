-- 코드를 입력하세요
# SELECT date_format(OUT_DATE, '%y-%m-%d')
# from food_order
SELECT ORDER_ID, PRODUCT_ID, date_format(OUT_DATE,'%Y-%m-%d'), CASE WHEN OUT_DATE IS NULL THEN '출고미정'
WHEN date_format(OUT_DATE, '%y-%m-%d') > '22-05-01' THEN '출고대기'
ELSE '출고완료' END AS '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID