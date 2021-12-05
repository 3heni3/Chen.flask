from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def hello():
    args = request.args
    args_msg = '\n'.join([f'Argument {k} With Value of: {v}' for k, v in args.items()]) if args else ''
    return f"Hello User!\nYou Gave Me The Following Args:\n{args_msg}"


@app.route('/homepage')
def homepage():
    return redirect(url_for('hello'))


@app.route('/home')
def home():
    return redirect('/')


if __name__ == '__main__':
    app.run()
