-- 코드를 입력하세요
SELECT B.BOOK_ID, A.AUTHOR_NAME, date_format(B.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
FROM AUTHOR A JOIN BOOK B on A.AUTHOR_ID = B.AUTHOR_ID
WHERE B.CATEGORY = '경제'
ORDER BY PUBLISHED_DATE