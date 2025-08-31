from flask import Flask, render_template, request, jsonify
from validator import validate_email   # ✅ Import your validator function
import webbrowser, threading #To run automatically on server

app = Flask(__name__)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    email = data.get("email", "")

    # ✅ Use validator.py function
    result = validate_email(email)

    if result == "Valid Email":
        # Save email if valid
        with open("emails.txt", "a") as f:
            f.write(email + "\n")
        return jsonify({"valid": True, "message": result})
    else:
        return jsonify({"valid": False, "message": result})

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=False)
