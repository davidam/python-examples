from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index(index=None):
    return render_template('index.html', index=index)

@app.route('/org-mode.html')
@app.route('/orgmode.html')
@app.route('/orgmode')
def orgmode(orgmode=None):
    return render_template('orgmode.html', orgmode=orgmode)

@app.route('/r.html')
@app.route('/r')
def r(r=None):
    return render_template('r.html', r=r)

@app.route('/elisp-es.html')
@app.route('/elisp-es')
@app.route('/elispes')
def elispes(elispes=None):
    return render_template('elisp-es.html', elispes=elispes)

@app.route('/gcc.html')
@app.route('/gcc')
def gcc(gcc=None):
    return render_template('gcc.html', gcc=gcc)

@app.route('/python.html')
@app.route('/python')
def python(python=None):
    return render_template('python.html', python=python)

@app.route('/bash.html')
@app.route('/bash')
def bash(bash=None):
    return render_template('bash.html', bash=bash)

@app.route('/debian.html')
@app.route('/debian')
def debian(debian=None):
    return render_template('debian.html', debian=debian)

@app.route('/acerca.html')
@app.route('/acerca')
def acerca(acerca=None):
    return render_template('acerca.html', acerca=acerca)


if __name__ == "__main__":
    app.run()
