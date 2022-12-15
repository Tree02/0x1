from flask import Flask, render_template
app = Flask(__name__, static_folder='staticFiles', template_folder='templates')

@app.route("/")
def index():
    try:
        return render_template('index.html')
    except:
        return render_template('historial.html')

"""
@app.route("/historial.html", methods=['GET'])
def history():
"""

if __name__ == '__main__':
    print('Inove@Server start!')
    app.run(host="192.168.100.122", port=5000)

