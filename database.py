import sqlite3


def main():
    db = sqlite3.connect('test.db')

    # how do you want this to be display
    db.row_factory = sqlite3.Row


    db.execute('DROP TABLE IF EXISTS test')
    db.execute('CREATE TABLE test(t1 text, i1 int)')

    db.execute('INSERT INTO test (t1,i1) VALUES (?,?)', ('two', 2))
    db.execute('INSERT INTO test (t1,i1) VALUES (?,?)', ('three', 3))
    db.execute('INSERT INTO test (t1,i1) VALUES (?,?)', ('four', 4))

    db.commit()


    cursor = db.execute('SELECT * FROM test ORDER BY t1')

    for row in cursor:
        print(dict(row))


if __name__ == '__main__': main()
