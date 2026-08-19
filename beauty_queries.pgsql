DROP TABLE IF EXISTS beauty CASCADE;
 
CREATE TABLE beauty (
    row_id        INT,
    order_id      TEXT,
    order_date    TIMESTAMP,
    customer_id   TEXT,
    segment       TEXT,
    city          TEXT,
    state         TEXT,
    country       TEXT,
    country_lat   NUMERIC,
    country_lng   NUMERIC,
    region        TEXT,
    market        TEXT,
    subcategory   TEXT,
    category      TEXT,
    product       TEXT,
    quantity      INT,
    sales         NUMERIC,
    discount      NUMERIC,
    profit        NUMERIC
);
 
COPY beauty FROM '/tmp/beauty_clean.csv' WITH (FORMAT csv, HEADER true);
