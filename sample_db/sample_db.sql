-- THIS IS A SAMPLE OF WHAT THE DATABASE WILL
-- LOOK LIKE

CREATE TABLE database (
  -- We want to give each row a id
  ID INTEGER PRIMARY KEY,
  -- We want a terminal name
  TERMINAL_TYPE TEXT NOT NULL,
  -- We want a .db connection
  CONNECT_TO TEXT UNIQUE,
  -- token
  TOKEN TEXT UNIQUE
);

-- This most likely won't be added for the actual database
-- But in case we feel the need, this will..and should be, what it will look like
ALTER TABLE database
-- The name and type will be different, of course
ADD COLUMN COLUMN_NAME TEXT UNIQUE DEFAULT "NoINFO";

-- This is fake data for the sample database
-- type 1, type2 etc do not stand for anything. I just do not know how many row types there will be for the database
-- TYPE 1
INSERT INTO database (ID, TERMINAL_TYPE, CONNECT_TO, TOKEN)
VALUES (1, "TERMUX", "MAIN.db", "180a01");
-- Type 2
INSERT INTO database (ID, TERMINAL_TYPE, CONNECT_TO, TOKEN)
VALUES (2, "TERMUX", "another_file.db", "18bda01");
-- Type 3
INSERT INTO database (ID, TERMINAL_TYPE, CONNECT_TO, TOKEN)
VALUES (3, "TERMUX", "aa_file.db", "1809io");
