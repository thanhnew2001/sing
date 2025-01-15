from flask import Flask, render_template
import os

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('record.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
