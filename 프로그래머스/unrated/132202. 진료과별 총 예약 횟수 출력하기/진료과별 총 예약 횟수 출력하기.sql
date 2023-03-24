# -- 코드를 입력하세요
SELECT MCDP_CD, COUNT(*)
FROM APPOINTMENT
WHERE YEAR(APNT_YMD) = 2022 and MONTH(APNT_YMD) = 5
GROUP BY MCDP_CD
ORDER BY COUNT(*), MCDP_CD

# SELECT * FROM APPOINTMENT