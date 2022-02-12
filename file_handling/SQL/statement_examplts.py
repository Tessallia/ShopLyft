CREATE_TABLE =  [
    #table_ref will be the name of the table used to store that type
"""CREATE TABLE IF NOT EXIST type (
    id INTEGER, name VARCHAR(10), table_ref VARCHAR(20), PRIMARY KEY(id))""",
    #
"""CREATE TABLE IF NOT EXIST data_classes (
    id INTEGER, name VARCHAR(30), type INT, time INT, duration INT, PRIMARY KEY(id)), daily INT,
    FOREIGN KEY (type) REFERENCES type(id)""",

    #todo
    #not sure whether to use one hot or binary string. will think on it more late to make pros and cons
    #pros


    #cons



    #days = 0000000 where 1 is occurance and 0 is no occurance
"""CREATE TABLE IF NOT EXIST weekly (
    id INTEGER, tid INT, days INT, PRIMARY KEY (id), FOREIGN KEY (tid) REFERENCES data_classes(id)
    )""",
#    using one hot for weekly stuf
#"""CREATE TABLE IF NOT EXIST weekly (
#    id INTEGER, tid TINYINT, monday TINYINT,tuesday TINYINT,wednesday TINYINT, thursday TINYINT, friday TINYINT,
#    saturday TINYINT, sunday TINYINT, PRIMARY KEY (id), FOREIGN KEY (tid) REFERENCES data_classes(id)
#    )""",
    #
"""CREATE TABLE IF NOT EXIST monthly (
    id INTEGER , tid INT, month int, day int, PRIMARY KEY (id), FOREIGN KEY (tid) REFERENCES data_classes(id))""",
    #
"""CREATE TABLE IF NOT EXIST date(
    id INTEGER, tid INT, epoch INT, PRIMARY KEY (id), FOREIGN KEY (tid) REFERENCES data_classes(id)
    )""",

    #the totals will be modified to be generated collumns based on the cooresponding values
"""CREATE TABLE IF NOT EXIST tags(
    id INTEGER, name INT, daily_total INT, weekly_total INT )""",


]
CREATE_INDEX = [
    """CREATE INDEX IF NOT EXIST names ON data_classes (name)""",
    """CREATE INDEX IF NOT EXIST e_type ON data_classes (type )""",
]

DEFAULT_TYPES = ['once', 'daily', 'weekly', 'monthly']
DEFAULT_TAGS = ['work', 'sleep', 'study', 'free time']