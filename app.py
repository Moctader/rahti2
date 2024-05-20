import os
from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()

PORT = os.environ.get('PORT', 8080)

app = Flask(__name__)

with app.app_context():
    # Init code here
    print(f'Flask app running on port {PORT}')
    print('change 1')

@app.route("/")
def index():
    print(f'{request.method} request from {request.remote_addr}')
    ret = {
        'msg': 'Rahti Flask demo works.',
        'port': PORT,   
        'env': os.environ.get('ENV_VAR', 'not working'), 
        'method': request.method
    }

    return ret



if __name__ == "__main__":
    app.run(debug=True, port=PORT, host='0.0.0.0' )
    
