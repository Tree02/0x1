from flask import Flask, render_template, jsonify, request, redirect
import traceback
from base import insert, sessionmaker, engine, Historial, deleteId
import sqlalchemy

app = Flask(__name__, static_folder='staticFiles', template_folder='templates')

Session = sessionmaker(bind=engine)

@app.route("/")
def index():
    try:
        return render_template('index.html')
    except:
        return jsonify({'trace': traceback.format_exc()}) 


#Insert data client
@app.route("/nuevo", methods=['POST'])
def nuevo():
    if request.method == 'POST':
        m = request.form.get('aam')#amount
        d = str(request.form.get('dde'))#description
        insert(d, m)
        return render_template('index.html')


# History, select delete, filter date = timestamps, modify description
@app.route("/historial", methods=['GET'])
def history():
    if request.method == 'GET':
        session = Session()
        data = session.query(Historial).all()
        return render_template('historial.html', data=data)


#Delete id - History // input client
@app.route("/delete/<id>", methods=['GET', 'POST'])
def elimId(id):
    if request.method == 'POST':
        deleteId(id=id)
        return redirect('/historial')

if __name__ == '__main__':
    app.run(host="192.168.100.2", port=5000)