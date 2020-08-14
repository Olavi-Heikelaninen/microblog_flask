from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Igor'}
    return """
    <html>
    <head>
        <title>Microblog Home</title>
    </head>
    <body>
        <h1>Hello """+ user['username'] +"""!</h1>
    </body>
    </html>
    """
