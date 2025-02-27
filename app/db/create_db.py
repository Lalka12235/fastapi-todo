import sqlite3 as sq

def create_db():
    with sq.connect('db/tasks.db') as con:
            cur = con.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS tasks (
                    username TEXT,
                    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT,
                    description TEXT,
                    is_completed BOOLEAN DEFAULT false
                )
            """)

            con.commit()
            cur.close()

if __name__ == '__main__':
      create_db()