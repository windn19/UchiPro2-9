CREATE TABLE IF NOT EXISTS original_names(
    id INTEGER PRIMARY KEY,
    title TEXT,
    FOREIGN KEY(id) REFERENCES movies(id)
);
