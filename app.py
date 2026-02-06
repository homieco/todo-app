from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'dev_secret_key'

# In-memory storage
todos = []
users = {
    'admin': 'password'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('todo_list'))
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/todos', methods=['GET', 'POST'])
def todo_list():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        item = request.form.get('item')
        if item:
            todos.append(item)

    return render_template('todos.html', todos=todos, user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
