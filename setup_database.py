from web_app import get_db_conection
db_conn = get_db_conection()

sql = """
CREATE TABLE IF NOT EXISTS appointments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name CHAR(50),
    doctor_name CHAR(50),
    appointment_date CHAR(20)
);
"""

#creating table in database
db_conn.execute(sql)

