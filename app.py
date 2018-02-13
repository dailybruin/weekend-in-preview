# copy pasta from
# https://realpython.com/blog/python/primer-on-jinja-templating/

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)