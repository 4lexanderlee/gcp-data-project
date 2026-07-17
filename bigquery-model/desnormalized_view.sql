CREATE OR REPLACE WIEW ecomerce_dataset.desnomalized_view AS
SELECT
    o.order_id,
    u.user_id,
    o.product,
    o.price,
    u.name,
    u.email
FROM ecomerce_dataset.orders o 
JOIN ecomerce_dataset.users u
    ON o.order_id = u.user_id
;