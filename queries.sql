-- Задание 1
-- Выведи список логинов курьеров с количеством их заказов в статусе «В доставке»
SELECT c.login, COUNT(o.id) AS orders_in_delivery
FROM "Couriers" c
LEFT JOIN "Orders" o ON c.id = o."courierId" AND o."inDelivery" = true
GROUP BY c.login;

-- Задание 2
-- Выведи все трекеры заказов и их статусы
SELECT track,
    CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM "Orders";
