DROP TABLE IF EXISTS item;

CREATE TABLE item (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  itsname TEXT UNIQUE NOT NULL,
  sell_in INTEGER,
  quality INTEGER
);