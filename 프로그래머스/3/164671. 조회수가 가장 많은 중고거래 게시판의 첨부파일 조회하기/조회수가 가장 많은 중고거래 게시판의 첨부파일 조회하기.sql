-- 코드를 입력하세요

# select format('/home/grep/src/',board_id, file_id, file_ext) as file_path
select concat('/home/grep/src/', A.board_id, '/', file_id, file_name, file_ext) as file_path
from (select board_id
      from USED_GOODS_BOARD
      order by views desc
      limit 1) A, used_goods_file B
where A.board_id = B.board_id
order by file_id desc


