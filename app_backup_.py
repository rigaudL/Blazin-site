from flask import Flask, render_template, request
import sqlite3



app = Flask(__name__)



# Function to initialize the SQLite3 database
def init_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users_enquiries
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              email TEXT, 
              message TEXT)
    ''')
    conn.commit()
    conn.close()

init_database()


@app.route("/")
def Home():
    return render_template("/Home.html")


@app.route("/Products")
def Products():
    return render_template("/Products.html")


@app.route("/About")
def About():
    return render_template("/About.html")

@app.route("/Book")
def Book():
    return render_template("/Book.html")


# An API to receive formData 

@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Access form data.
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    print(f"Name: {name}\nEmail: {email}\nMessage: {message}")

    # Save data to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''INSERT INTO users_enquiries (name, email, message)
            VALUES (?, ?, ?)''', (name, email, message))
    conn.commit()
    conn.close()
    
    return "Form submitted successfully and data saved to database."


if __name__ == "__main__":
    app.run(debug=True)
    
