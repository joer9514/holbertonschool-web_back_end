-- Script that creates trigger
-- Decreases the quantity of an item after adding
CREATE TRIGGER sub_quantity AFTER INSERT ON orders
FOR EACH ROW UPDATE items
SET
quantity = quantity - NEW.number
WHERE name = NEW.item_name;
