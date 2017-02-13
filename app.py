from flask import Flask, render_template, request
from quotes import PERSONS

app = Flask(__name__)

def getQuotes(person, limit):
	try:
		person = person.lower().replace(' ', '_')
		quotes = PERSONS.get(person)
		if limit and limit != '0':
			try:
				limit = int(limit)
				quotes = quotes[:limit]
			except ValueError:
				quotes = quotes
	except IndexError:
		quotes = []
	return quotes


@app.route('/', methods = ['GET'])
def index():
	person = request.args.get('person', '')
	limit = request.args.get('limit', '')
	quotes = getQuotes(person, limit)
	context = { 'person': person, 'quotes': quotes, 'limit': limit }
	return render_template('index.html', **context)

app.run(debug=True)