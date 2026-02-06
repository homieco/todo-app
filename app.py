from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory storage
messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            messages.append(message)
        return redirect(url_for('index'))
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
