from flask import Flask, render_template, request, redirect
from TrumpBotModule import TrumpBot
from flask_wtf import Form
from wtforms import SelectField, SubmitField, TextAreaField
from wtforms import validators

# List of vlid topics...
TopicList = ['default','bragging','ocd','media','twitter']

class SpeechSelect(Form):
    SpeechType = SelectField(
        'Speech Type',
        choices=[('default', 'Default'), 
                 ('media', 'Media Bashing'), 
                 ('twitter', 'Twitter'), 
                 ('ocd', 'OCD')]
    )

class TrumpTweet(Form):
    Tweet = TextAreaField(u'Tweet', 
              [validators.optional(), validators.length(max=600)])

app = Flask(__name__)
app.secret_key = "I hate to tell you"

@app.route("/")
def hello():
    url = 'http://www.viclab.org'
    return redirect(url, code=307, Response=None)


@app.route("/TrumpBot", methods=['GET','POST'])
def trumpbot():
    topic = 'Default'
    if request.method == 'POST':
      topic = request.form['SpeechType']
      if topic not in TopicList:
        url = 'http://www.nickelback.com/'
        return redirect(url, code=307, Response=None)

    form = SpeechSelect()
    bot = TrumpBot()
    bot.make_speech(topic)
    speech = bot.speech[:]
    del bot
    return render_template('trumpbot.html', form=form, out=speech)

@app.route("/vic")
def vic():
    url = 'http://www.viclab.org'
    return redirect(url, code=307, Response=None)



if __name__ == "__main__":
    app.run(host='0.0.0.0')
