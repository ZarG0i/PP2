CREATE OR REPLACE FUNCTION add_numbers(a INT, b INT)
RETURNS INT AS $$
BEGIN
    RETURN a + b;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION check_even(n INT)
RETURNS TEXT AS $$
BEGIN
    IF n % 2 = 0 THEN
        RETURN 'Even';
    ELSE
        RETURN 'Odd';
    END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE insert_user(u_name TEXT, u_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO phonebook(username, phone)
    VALUES (u_name, u_phone);
END;
$$;


DECLARE
    total INT := 0;


IF total > 10 THEN
    RAISE NOTICE 'Greater';
ELSE
    RAISE NOTICE 'Smaller';
END IF;

LOOP
    total := total + 1;
    EXIT WHEN total = 5;
END LOOP;


FOR i IN 1..5 LOOP
    RAISE NOTICE 'Value: %', i;
END LOOP;

CREATE OR REPLACE FUNCTION get_total()
RETURNS INT AS $$
BEGIN
    RETURN 100;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_users()
RETURNS TABLE(id INT, username TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT id, username FROM phonebook;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION safe_divide(a INT, b INT)
RETURNS INT AS $$
BEGIN
    RETURN a / b;
EXCEPTION
    WHEN division_by_zero THEN
        RAISE NOTICE 'Cannot divide by zero';
        RETURN NULL;
END;
$$ LANGUAGE plpgsql;