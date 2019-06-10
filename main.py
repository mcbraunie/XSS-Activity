import os
import base64

from flask import Flask, request
from model import Message 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        m = Message(content=request.form['content'])
        m.save()

    body = """
<html>
<body>
<h1>Class Message Board</h1>
<h2>Contribute to the Knowledge of Others</h2>
<form method="POST">
    <textarea name="content"></textarea>
    <input type="submit" value="Submit">
</form>
<h2>Wisdom From Your Fellow Classmates</h2>
"""
    # Replacing str with HTML char. sequences (Unicode Hexadecimal)
    for m in Message.select():
        body += """
<div class="message">
{}
</div>
""".format(m.content.replace('<', '&#x003C;').replace('>', '&#x003E;')
    .replace('(', '&#x0028;').replace(')', '&#x0029;').replace("'", '&#x0027;')
    .replace("[", '&#x005B;').replace("]", '&#x005D;').replace("{", '&#x007B;')
    .replace("}", '&#x007D;').replace("!", '&#x0021;'))

    return body 


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

