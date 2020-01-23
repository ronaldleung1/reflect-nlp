from flask import Flask
from flask import request
from flask import jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def parseIntent():
	if request.is_json:
		intent = request.get_json()["intent"]

		print(intent)

		if "work" not in intent:
			return jsonify({'status': 'bad intent'}), 403
		return jsonify({'status': 'ok'}), 200

	return jsonify({'status': 'bad json'}), 400

if __name__ == '__main__':
	# bind to Heroku defined port, if not defined, bind to 5000
    app.run(host='localhost', port=int(os.environ.get('PORT', 5000)))
