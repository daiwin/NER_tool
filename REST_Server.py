from flask import Flask
from flask_restful import Resource, Api, reqparse
import hashlib
import main
import threading

class Pokemon(Resource):

	filename=""

	def foooooooo(self):
		parser = reqparse.RequestParser()
		parser.add_argument('text', type=str, required=True, location='json')
		args = parser.parse_args(strict=True)
		self.filename = hashlib.sha224(args['text'].encode('utf-8')).hexdigest()
		file = open("input\\"+self.filename+".txt", "w")
		file.write(args['text'])
		file.close

	def post(self):
		pokemon=[]
		NE_system = main.system()    
		self.foooooooo()
		NE_system.run()     
		mass = filter(None,open("output\\"+self.filename+".txt", "r").read().split("\n"))
  
		for a in mass:
			NE = a.split(':')
			pokemon.append({'tag':NE[0],'entity':NE[1]})

		return pokemon

app = Flask(__name__)
api = Api(app)
api.add_resource(Pokemon, '/')


if __name__ == '__main__':
	app.run(debug=True)
