from flask import Flask
from flask import Response
from tex import renderTex;
from graph import renderGraph;
app = Flask(__name__)
app.debug = True
@app.route('/')
def homePage():
	return html("index");

@app.route('/<page>')
def html(page):
	return Response(open("assets/html/"+page+".html"),mimetype='text/html')

@app.route('/js/<filename>')
def js(filename):
	return Response(open("assets/js/"+filename),mimetype='text/js')

@app.route('/css/<filename>')
def css(filename):
	return Response(open("assets/css/"+filename),mimetype='text/css')

@app.route('/tex/<path:query>')
def tex(query):
	return Response(renderTex(query.replace(".png","").replace("$","").replace("/","\\")),mimetype='image/png')

@app.route('/graph/<path:query>')
def graph(query):
	return Response(renderGraph(query.replace(".png","").replace(" ","")),mimetype='image/png')

#Pointless comment

if __name__=="__main__":
	app.run();
