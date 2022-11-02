from flask import Flask, render_template, request

app = Flask(__name__)
users = ['mike', 'mishel', 'adel', 'keks', 'kamila']

@app.route('/users')
def users_():
    term = request.args.get("term")
    filter_users = filter(lambda i: True if not term else term in i, users)
    return render_template(
        'show.html',
        term=term,
        users=filter_users
    )