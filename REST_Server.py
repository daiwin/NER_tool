from flask import Flask
from flask_restful import Resource, Api, reqparse
import hashlib
import main


class REST_server(Resource):

	filename=""
	
	def NER(self):
		parser = reqparse.RequestParser()
		parser.add_argument('text', type=str, required=True, location='json')
		args = parser.parse_args(strict=True)
		self.filename = hashlib.sha224(args['text'].encode('utf-8')).hexdigest()
		
		try:
			file = open("input\\"+self.filename+".txt", "w")
			file.write(args['text'])
		except:
			print("Error")
		finally:
			file.close

	def post(self):
		entities=[]
		NE_system = main.system()    
		self.NER()
		NE_system.run() 
		output_data=[]
		try:
			output_data = filter(None,open("output\\"+self.filename+".txt", "r").read().split("\n"))		
		except:
			entities.append({'tag':'','entity':''})
		finally:	
			for a in output_data:
				NE = a.split(':')
				entities.append({'tag':NE[0],'entity':NE[1]})
			if (len(entities)==0):
				entities.append({'tag':'','entity':''})			
		return entities

app = Flask(__name__)
api = Api(app)
api.add_resource(REST_server, '/')


if __name__ == '__main__':
	app.run(debug=True)
