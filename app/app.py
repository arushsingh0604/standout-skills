from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route("/available-skills")
def available_skills():
    try:
        db = mysql.connector.connect(
            host="10.0.3.180",
            user="appuser",
            password="yourpassword",
            database="employee_db"
        )
        cursor = db.cursor()
        cursor.execute("SELECT name, skill, location, experience_years FROM employees WHERE available = 1")
        results = cursor.fetchall()
        return jsonify([
            {"name": name, "skill": skill, "location": loc, "experience": exp}
            for name, skill, loc, exp in results
        ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

