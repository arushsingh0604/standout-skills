from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Home route to test if app is running
@app.route("/")
def home():
    return "Standout App Layer is Live"

# API route to fetch available skills from database
@app.route("/available-skills")
def available_skills():
    try:
        db = mysql.connector.connect(
            host="10.0.3.180",           # Replace with actual private IP of DB instance
            user="appuser",              # Replace with actual DB username
            password="yourpassword",     # Replace with actual DB password
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
