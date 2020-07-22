from flask import Flask, render_template, request, redirect

from forms import SubmitForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eiewgioqh95ff6nac'

bootstrap = Bootstrap(app)


@app.route("/index")
def index():
    return "Hello, Flask!"
 
@app.route("/", methods=['GET','POST'])
def home():
    form = SubmitForm()
    if request.method == 'POST' and form.validate():
            return redirect('/submit')
    return render_template('home.html', form = form)

@app.route("/submit", methods=['POST'])
def submit():
    return render_template('submit.html')

@app.route("/stream", methods=['POST'])
def stream():
    return render_template('stream.html')

@app.route("/static", methods=['POST'])
def static_feed():
    return render_template('static.html')

@app.route("/stream_static", methods=['POST'])
def stream_static():
    return render_template('stream_static.html')
