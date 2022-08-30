from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.9cihgwo.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/ds", methods=["POST"])
def web_ds_post():
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']
    passwordCheck_receive = request.form['passwordCheck_give']
    phone_receive = request.form['phone_give']
    address_receive = request.form['address_give']
    gender_receive = request.form['gender_give']

    doc = {
        'id': id_receive,
        'password': password_receive,
        'passwordCheck': passwordCheck_receive,
        'phone': phone_receive,
        'address': address_receive,
        'gender': gender_receive
    }
    db.ds.insert_one(doc)

    return jsonify({'msg': '회원가입 완료!'})


@app.route("/ds", methods=["GET"])
def web_mars_get():
    order_list = list(db.ds.find({}, {'_id': False}))
    return jsonify({'orders': order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5700, debug=True)
