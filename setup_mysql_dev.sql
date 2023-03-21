--- SQL
!/usr/bin/python3
"""Task 3"""

import MySQLdb
import sys

if __name__ == "__main__":

db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=hbnb_dev,
        passwd=hbnb_dev_pwd,
        db=hbnb_dev_db
    )

    cursor = db.cursor()
    cursor.execute("GRANT ALL PRIVILEGES ON hbnb_dev_db \
                    TO 'hbnb_dev'@'localhost'")

    cursor.execute("GRANT SELECT ON performance_schema \
                    TO 'hbnb_dev'@'localhost'")

    cursor.close()
    db.close()
