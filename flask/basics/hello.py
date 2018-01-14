from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello(name=None):
    return 'Hello, world'

@app.route('/projects/')
@app.route('/projects/<projects>')
def projects(projects=None):
    return render_template('projects.html', projects=projects)

@app.route('/about')
def about():
    return 'The about page'

if __name__ == "__main__":
    app.run()
