CREATE TABLE DATABASE_ (
  -- We want a id
  ID INTEGER PRIMARY KEY,
  -- We want a terminal type
  SYSTEM_ TEXT NOT NULL,
  --  WE WANT A TOKEN
  -- For the fact that there can be more than one system in the database we will make it NOT NULL
  TOKE TEXT NOT NULL
);
