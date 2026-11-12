from flask import Flask,request,jsonify
app=Flask(__name__)

VALID_USERNAME="admin"
VALID_PASSWORD="password123"

@app.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    username=data.get('username',' ')
    password=data.get('password',' ')

    if username==VALID_USERNAME and password==VALID_PASSWORD:
        return jsonify({"sucess":True,"message":"login sucessfull"})
    else:
        return jsonify({"sucess":False,"message":"invalid username or password"}),201

if __name__=='__main__':
    app.run(debug=True)
