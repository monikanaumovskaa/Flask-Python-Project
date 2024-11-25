from flask import Flask, jsonify, render_template
import sqlite3
import requests
from flask import request

connection = sqlite3.connect('users.db')
#cursor is used to execute our SQL queries
cursor = connection.cursor()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/total_spent/<int:user_id>', methods=['GET'])
def total_spent_per_person(user_id):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    #? means that the value will be substitued at runtime
    query = ("SELECT user_id, sum(money_spent)AS total_spent FROM user_spending WHERE user_id = ? GROUP BY user_id")

    cursor.execute(query, (user_id, ))
    result = cursor.fetchone()

    if result:
        return jsonify({
            "user_id": result[0],
            "total_spent": result[1]
        })

@app.route('/average_spending_by_age', methods = ['GET'])
def average_spending_by_age():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    query1 = '''
        SELECT 
            CASE 
                WHEN age BETWEEN 18 AND 24 THEN '18-24years'
                WHEN age BETWEEN 25 AND 30 THEN '25-30years'
                WHEN age BETWEEN 31 AND 36 THEN '31-36years'
                WHEN age BETWEEN 37 AND 47 THEN '37-47years'
                ELSE '>47years'
            END AS age_group,
            AVG(money_spent) AS average_spent
        FROM user_spending
        JOIN user_info ON user_info.user_id = user_spending.user_id
        GROUP BY age_group
    '''
#SELECT user_spending.user_id, avg(user_spending.money_spent) AS avg_spent FROM user_spending JOIN user_info ON user_spending.user_id = user_info.user_id WHERE user_info.age<24 and user_info.age>18 GROUP BY user_spending.user_id

    cursor.execute(query1)
    result1 = cursor.fetchall()

    age_groups = {}
    for row in result1:
        age_groups[row[0]] = row[1]
    return jsonify((age_groups))

@app.route('/w', methods=['POST'])
def high_spending_user():
    data = request.get_json()
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    user_id = data["user_id"]
    total_spending = data['total_spending']

    if not user_id or not total_spending:
        return jsonify({"error": "Missing user_id or total_spending"}), 400

    print("VLEZE")
    cursor.execute('INSERT INTO high_spenders (user_id, total_spending) VALUES (?, ?)', (user_id, total_spending))
    connection.commit()
    connection.close()

    return jsonify({"message": f"User {user_id} with spending {total_spending} added to high_spending_users."}), 201


if __name__ == "__main__":
    app.run(debug=True)
