from flask import Flask
from flask import Response
from tex import renderTex;
from graph import renderGraph;
from settings import *;
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)
app.debug = not PRODUCTION
if (PRODUCTION):
	app.wsgi_app=ProxyFix(app.wsgi_app);

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

@app.route('/css/<filename>')
def img(filename):
	return Response(open("assets/img/"+filename),mimetype='text/css')

@app.route('/tex/<path:query>')
def tex(query):
	return Response(renderTex(query.replace(".png","").replace("$","").replace("/","\\")),mimetype='image/png')

@app.route('/graph/<path:query>')
def graph(query):
	return Response(renderGraph(query.replace(".png","").replace(" ","")),mimetype='image/png')

#Pointless comment

if __name__=="__main__":
	app.run();
