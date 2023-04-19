from api import app

# @app.route('/')
# def home():
#     return 'Hello, World!'

app.run(host='localhost', port=8000, debug=True)