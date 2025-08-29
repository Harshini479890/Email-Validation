from flask import Flask, render_template, request, jsonify
import webbrowser
import threading

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

    # ✅ Validation logic
    if "@" in email and "." in email and len(email) >= 6 and email[0].isalpha():
        # Save valid email
        with open("emails.txt", "a") as f:
            f.write(email + "\n")
        return jsonify({"valid": True, "message": "Valid Email"})
    else:
        return jsonify({"valid": False, "message": "Invalid Email"})

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=False)
