
CREATE OR REPLACE PROCEDURE upsert_user(u_name TEXT, u_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = u_name) THEN
        UPDATE phonebook SET phone = u_phone
        WHERE username = u_name;
    ELSE
        INSERT INTO phonebook(username, phone)
        VALUES (u_name, u_phone);
    END IF;
END;
$$;



CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    invalid_data TEXT := '';
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP

        IF phones[i] ~ '^[0-9]+$' AND length(phones[i]) >= 5 THEN
            
            IF EXISTS (SELECT 1 FROM phonebook WHERE username = names[i]) THEN
                UPDATE phonebook SET phone = phones[i]
                WHERE username = names[i];
            ELSE
                INSERT INTO phonebook(username, phone)
                VALUES (names[i], phones[i]);
            END IF;

        ELSE
            invalid_data := invalid_data || names[i] || ':' || phones[i] || E'\n';
        END IF;

    END LOOP;

    RAISE NOTICE 'Invalid data:\n%', invalid_data;
END;
$$;



CREATE OR REPLACE PROCEDURE delete_user(identifier TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = identifier
       OR phone = identifier;
END;
$$;