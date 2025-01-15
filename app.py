from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('record.html')  # Make sure the HTML file name is correct

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
