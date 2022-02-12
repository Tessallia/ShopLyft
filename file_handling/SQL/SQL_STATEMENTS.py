TEMP_DATA_TABLES = [
    #
    """
    CREATE TABLE IF NOT EXIST urls (
    action_name VARCHAR(20), link VARCHAR(200) 
    )
    """,
]

TEMP_DATA_INDEX = [
    """
    CREATE INDEX IF NOT EXIST level ON urls (level)
    """
]

TEMP_DATA = [TEMP_DATA_TABLES, TEMP_DATA_INDEX]

STORE_LIBRARY = {
    """CREATE TABLE IF NOT EXIST store (
    id INTEGER,
    store_name VARCHAR(30),
    store_home VARCHAR(100),
    PRIMARY KEY (id)
    )""",
    """
    CREATE TABLE IF NOT EXIST actions(
    id INTEGER,
    action_name VARCHAR(20)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS store_actions(
    st_id INTEGER,
    store_id VARCHAR(30),
    step INT,
    action_id VARCHAR(20),
    PRIMARY KEY(st_id),
    FOREIGN KEY store_id REFERENCES store(id),
    FOREIGN KEY action_id REFERENCES actions(id)
    )
    """,
    """
    CREATE TABLE IF NOT EXIST pattern (
    st_id INTEGER,
    pattern_number INT, 
    step INT,
    tag VARCHAR(30),
    )
    """


}

DEFAULT_ACTIONS=['search', 'search_results', 'product_data', "reviews"]
