from flask import Flask, request
import subprocess
app = Flask(__name__)

@app.route('/index', methods=['POST'])
def convert_doc():
    word_filename = request.args.get('document')
    if not word_filename:
        return "Please provide document"

    try:
      subprocess.check_call(["unoconv", word_filename])
    except subprocess.CalledProcessError:
        return "Something went wrong. Make sure you specify the correct path"

    return "Success!"