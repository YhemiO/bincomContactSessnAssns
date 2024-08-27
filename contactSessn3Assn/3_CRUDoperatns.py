import psycopg2
from psycopg2.extras import DictCursor

conn = None
cur = None

try:
    with psycopg2.connect(

       host = 'localhost',
       database = 'postgres', 
       user = 'postgres',
       password = 'admin123',
       port = 5432
    ) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            # CREATE
            cur.execute('DROP TABLE IF EXISTS employee')
            create_script = '''CREATE TABLE IF NOT EXISTS employee(
                                    id int PRIMARY KEY,
                                    name varchar(40) NOT NULL,
                                    salary int,
                                    dept_id varchar(30))'''
            cur.execute(create_script)

            insert_script = 'INSERT INTO employee(id, name, salary, dept_id) VALUES(%s, %s, %s, %s)'
            insert_value = [(1, 'James', 12000,'D1'),(2, 'Robin', 15000, 'D2'),(3, 'Xavier', 20000, 'D3')]
            for record in insert_value:
                cur.execute(insert_script, record)

            # UPDATE
            update_script = 'UPDATE employee SET salary=salary+(salary*0.5)'
            cur.execute(update_script)

             # DELETE
            #delete_script = 'DELETE FROM employee WHERE name = %s'
            #delete_record = ('James', )
            #cur.execute(delete_script, delete_record)
            
            # FETCHING SOME DATA
            cur.execute('SELECT * FROM employee')
            for record in cur.fetchall():
                print(record['id'], record['name'], record['salary'], record['dept_id'])
            

            conn.close
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close