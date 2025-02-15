from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

score = 0
balance = 0
autoclickers = 0
click_multiplier = 1
booster_active = False
booster_end_time = 0

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/click')
def click():
	global score, balance, click_multiplier
	score += click_multiplier
	balance += click_multiplier
	return jsonify(score=score, balance=balance)

@app.route('/buy_autoclicker')
def buy_autoclicker():
	global balance, autoclickers
	if balance >= 100:
		balance -= 100
		autoclickers += 1
		return jsonify(success=True, balance=balance, autoclickers=autoclickers)
	return jsonify(success=False, balance=balance, autoclickers=autoclickers)

@app.route('/buy_multiplier')
def buy_multiplier():
	global balance, click_multiplier
	if balance >= 20:
		balance -= 20
		click_multiplier += 1
		return jsonify(success=True, balance=balance, click_multiplier=click_multiplier)
	return jsonify(success=False, balance=balance, click_multiplier=click_multiplier)

@app.route('/buy_booster')
def buy_booster():
	global balance, booster_active, booster_end_time
	if balance >= 50 and not booster_active:
		balance -= 50
		booster_active = True
		booster_end_time = time.time() + 10  
		return jsonify(success=True, balance=balance, booster_active=True)
	return jsonify(success=False, balance=balance, booster_active=booster_active)

@app.route('/get_data')
def get_data():
	global score, balance, autoclickers, booster_active, booster_end_time
	
	score += autoclickers
	balance += autoclickers

	
	if booster_active and time.time() < booster_end_time:
		score += autoclickers
		balance += autoclickers
	else:
		booster_active = False

	return jsonify(score=score, balance=balance, autoclickers=autoclickers, booster_active=booster_active)

if __name__ == '__main__':
	app.run(debug=True)
