from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

app = Flask(__name__)


@app.route('/<random_string>')
def return_backwards_string(random_string):
    # comment
    return "".join(reversed(random_string))



@app.route('/get-mode')
def get_mode():
    #raise Exception() # fail 
    return os.environ.get("MODE")


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=8080)