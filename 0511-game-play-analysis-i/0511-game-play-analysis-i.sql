# Write your MySQL query statement below
WITH SUB_TABLE AS (SELECT *, ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date) AS RN FROM Activity)
SELECT player_id, event_date AS first_login FROM SUB_TABLE WHERE RN = 1