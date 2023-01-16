from flask import Flask, request, jsonify
import user_data as us

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    passwd = request.form.get('password')
    print(passwd)
    data = us._find_user(user)
    if data[0]['passwd'] == passwd:
        return ({"Msg": "You can login!"}), 200
    else:
        return ({"Msg": "Invalid user"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)