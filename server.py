from flask import Flask
from flask import Response
from tex import renderTex;
from graph import renderGraph;
app = Flask(__name__)
app.debug = True

@app.route('/tex/<query>')
def tex(query):
	print query;
	return Response(renderTex(query[:query.rindex(".")].replace(" ","")),mimetype='image/png')

@app.route('/graph/<query>')
def graph(query):
	return renderGraph(query);

#Pointless comment

if __name__=="__main__":
	app.run();
