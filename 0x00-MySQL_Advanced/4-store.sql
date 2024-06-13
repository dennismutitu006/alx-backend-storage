-- creating a trigger
-- it decreases the quantity of items in stock if a new order is placed

DELIMITER $$
CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END $$
DELIMITER ; 
