from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
# Make sure disabling CSRF protection is safe here.
app.config['WTF_CSRF_ENABLED'] = False


@app.route('/<random_string>')
def return_backwards_string(random_string):
    return "".join(reversed(random_string))

@app.route('/get-mode')
def get_mode():
    return os.environ.get("MODE")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)