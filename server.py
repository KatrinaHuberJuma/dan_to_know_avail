from flask import Flask, request, render_template, jsonify


app = Flask(__name__)
# this sets up an instance of the class Flask
# so app is an object with methods and attributes defined in the flask module



if __name__ == '__main__':
    # if I run this file directly, do this code
    # so `python3 server.py` in the shell
    # this starts the server running and keeps it running until we 1) stop it or 2) break everything
    app.run(debug=True, host='0.0.0.0', port='5000')