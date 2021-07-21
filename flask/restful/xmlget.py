from flask import Flask
from flask_restful import Resource, Api
from flask import Response

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        soapstr = '<?xml version="1.0" encoding="UTF-8"?>'
        soapstr = soapstr + '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\n'
        soapstr = soapstr + '   <soap:Body>\n'
        soapstr = soapstr + '     <getProductDetails xmlns="http://warehouse.example.com/ws">\n'
        soapstr = soapstr + '       <productId>827635</productId>\n'
        soapstr = soapstr + '     </getProductDetails>\n'
        soapstr = soapstr + '   </soap:Body>\n'
        soapstr = soapstr + '</soap:Envelope>\n'

        return Response(soapstr, mimetype='text,xml')

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
