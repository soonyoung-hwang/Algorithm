-- 코드를 입력하세요
SELECT HOUR(DATETIME) as HOUR, COUNT(*)
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 and HOUR(DATETIME) <= 19
GROUP BY HOUR
ORDER BY HOUR ASC