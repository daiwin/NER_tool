from flask import Flask
from flask_restful import Resource, Api, reqparse
import hashlib
import codecs
import main


class Pokemon(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str, required=True, location='json')
        args = parser.parse_args(strict=True)
        

        filename = hashlib.sha224(args['text'].encode('utf-8')).hexdigest()
        file = codecs.open("input\\"+filename+".txt", "w", "utf-8")
        file.write(args['text'])
        file.close
        
        
        pokemon=[]

        main.main()
        mass = filter(None,open("output\\"+filename+".txt", "r").read().split("\n"))
        
        for a in mass:
             NE = a.split(':')
             pokemon.append({'tag':NE[0],'entity':NE[1]})

        return pokemon
     
app = Flask(__name__)
api = Api(app)
api.add_resource(Pokemon, '/')



if __name__ == '__main__':
     app.run(debug=True)
