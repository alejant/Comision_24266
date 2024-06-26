from flask import Flask
from app.views import index, test, teastar_base, crear_tabla

app = Flask(__name__)

app.route('/', methods=['GET'])(index)
app.route('/test', methods=['GET'])(test)
app.route('/probar_base', methods=['POST'])(teastar_base)
app.route('/tabla/crear', methods=['POST'])(crear_tabla)

if __name__ == '__main__':
    app.run(debug=True)