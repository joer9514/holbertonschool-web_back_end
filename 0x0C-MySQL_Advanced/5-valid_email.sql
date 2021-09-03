-- SQL script that creates a trigger that resets the attributes.
DELIMITER $$
CREATE TRIGGER new_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
	SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;
