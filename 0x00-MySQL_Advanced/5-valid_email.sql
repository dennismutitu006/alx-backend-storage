-- A script that creates a triggger that resets the attribute valid_email
-- Create trigger to reset valid_email when email is changed
-- triggers for a valid email
DELIMITER $$
CREATE TRIGGER reset_valid_email -- trigger named reset..
BEFORE UPDATE ON users -- specify the trigger will fire b4 an update oper on u
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN -- if new email is diff frm old
        SET NEW.valid_email = 0;
    END IF;
END $$
DELIMITER ;
