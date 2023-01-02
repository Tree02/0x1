from flask import Flask, render_template, jsonify, request
import traceback
from base import insert, deleteId

app = Flask(__name__, static_folder='staticFiles', template_folder='templates')

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
        m = request.form.get('aam')
        d = str(request.form.get('dde'))
        insert(d, m)
    
        return render_template('index.html')


# History, select delete, filter date = timestamps, modify description
@app.route("/historial.html", methods=['GET'])
def history():
    if request.method == 'GET':
        return render_template('historial.html')


#Delete id - History // input client
"""
@app.route("/historial/delete/<id>", methods=['GET', 'POST'])
def elimId(id):
    if request.method == 'POST':
        deleteId(id=id)
        return render_template('historial.html')
"""

if __name__ == '__main__':
    print('Inove@Server start!')
    app.run(host="192.168.100.122", port=5000)