import flask

from web_app import app, get_db_conection

@app.route("/")
@app.route("/home")
def home():
    sql = f"""
    SELECT id, patient_name, doctor_name, appointment_date 
    FROM appointments;
    """
    db_conn = get_db_conection()
    result = db_conn.execute(sql).fetchall()
    result_dict = []

    #transforming result to result_dict
    for row in result:
        result_dict.append(
            {
                "id" : row[0],
                "patient_name" : row[1],
                "doctor_name" : row[2],
                "appointment_date" : row[3],

            }
        )
   
    db_conn.close()
    
    return flask.render_template("appointments.html", appointments = result_dict)


@app.route("/appointments")
def search():
    return flask.redirect("/")

@app.route("/appointment/add")
def add_get():
    return flask.render_template("add.html", email = None, password = None)

@app.route("/appointment/add", methods=["POST"])
def add_post():
    #getting data from html form
    patient_name = flask.request.form["patient_name"]
    doctor_name = flask.request.form["doctor_name"]
    appointment_date = flask.request.form["appointment_date"]
    db_conn = get_db_conection()
    sql = f"""
    INSERT INTO appointments(patient_name, doctor_name, appointment_date)
    VALUES('{patient_name}', '{doctor_name}', '{appointment_date}');
    """
    #excecuting sql in database
    db_conn.execute(sql)
    #saving inserted data in database
    db_conn.commit()
    db_conn.close()

    return flask.redirect("/appointments")

