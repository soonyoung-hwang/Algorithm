-- 코드를 입력하세요
SELECT *
FROM FOOD_PRODUCT F
WHERE F.PRICE = (select max(price) from food_product)
