from flask import Flask,render_template,flash, redirect
from gevent import pywsgi
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from gan import GAN

class InputForm(FlaskForm):
    poeminput = StringField('Seed', validators=[DataRequired()])
    submit = SubmitField('submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
# ... add more variables here as needed

@app.route('/',methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        print("receive")
        print(form.poeminput.data)
        a = gan.generate_poem(count=8, temperature=1.00, seed=form.poeminput.data)
        print(a)
        flash('Output of seed \'{}\': \n {} '.format(form.poeminput.data,a))
        # print(form.username.data,form.remember_me.data)
        return redirect('/index')
    return render_template('index.html', title='Poem Generate', form=form)

if __name__ == '__main__':
    # server = pywsgi.WSGIServer(('0.0.0.0',80), app)
    # server.serve_forever()
    gan = GAN()
    gan.build()
    app.run(debug='True')