-- Практический блок: вторая часть
-- Работа с базой данных

-- 1 задание
SELECT c.login,
	COUNT(*)
FROM "Couriers" AS c
INNER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;


-- 2 задание
SELECT track,
       CASE
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN "inDelivery" = true THEN 1
           ELSE 0
       END
FROM "Orders";