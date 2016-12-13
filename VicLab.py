from flask import Flask, render_template, request, redirect
from TrumpBotModule import TrumpBot

app = Flask(__name__)

@app.route("/")
def hello():
    url = 'http://www.viclab.org'
    return redirect(url, code=307, Response=None)


@app.route("/TrumpBot")
def trumpbot():
    bot = TrumpBot()
    bot.make_speech()
    speech = ""
    for line in bot.speech:
      speech = speech + line + "\n"
    del bot
    return render_template('trumpbot.html', out = speech)

@app.route("/vic")
def vic():
    url = 'http://www.viclab.org'
    return redirect(url, code=307, Response=None)



if __name__ == "__main__":
    app.run(host='0.0.0.0')
