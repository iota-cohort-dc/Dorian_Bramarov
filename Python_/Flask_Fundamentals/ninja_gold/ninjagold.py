from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hisIsSecret'
import random

@app.route('/')
def index():

    if 'sents' in session:
      pass
    else:
      session['sents'] = []

    if 'gold' in session:
      pass
    else:
      session['gold'] = 0

    return render_template('ninjagold.html')

@app.route('/gold', methods=['POST'])
def build():

    if request.form['build'] == 'farm':
      session['randomFarm'] = random.randrange(10, 21)
      farmsent = "Earned "+ str(session['randomFarm'])+  " golds from the farm!"
      session['sents'].append(farmsent)
      #print session['sents']
      session['gold'] += session['randomFarm']


    elif request.form['build'] == 'cave':
      session['randomCave'] = random.randrange(5, 11)
      cavesent = "Earned "+ str(session['randomCave'])+  " golds from the cave!"
      session['sents'].append(cavesent)
      #print session['sents']
      session['gold'] += session['randomCave']

    elif request.form['build'] == 'house':
      session['randomHouse'] = random.randrange(2, 6)
      housesent = "Earned "+ str(session['randomHouse'])+  " golds from the house!"
      session['sents'].append(housesent)
      #print session['sents']
      session['gold'] += session['randomHouse']

    elif request.form['build'] == 'casino':
      randomNum = random.randrange(0, 2)
      if randomNum == 1:
        session['randomCasino'] = random.randrange(1, 51)
        casinosent = "Earned "+ str(session['randomCasino'])+  " golds from the casino!"
        session['sents'].append(casinosent)
        #print session['sents']
        session['gold'] += session['randomCasino']
      elif randomNum == 0:
        session['randomCasino'] = random.randrange(1, 51)
        casinosent = "Lost "+ str(session['randomCasino'])+  " golds from the casino!"
        session['sents'].append(casinosent)
        #print session['sents']
        session['gold'] -= session['randomCasino']
    return redirect('/')

app.run(debug=True)