import os
import json
from subprocess import check_output, CalledProcessError

#Constants
_TREE_PATH="data/graph/"

def renderGraph(query):
	"""
		Returns the path to a png file that
		contains the graph render of the query.
		Creates the png file itself if it 
		does not already exist.
	"""
	#Compute the hash of the query string
	qhash = hashFunc(query)

	if (not os.path.exists(_TREE_PATH+str(qhash))):

		#Create bucket if it doesn't already exist.
		os.makedirs(_TREE_PATH+str(qhash))

		#Create the lookup table for the bucket.
		bucketTableFile=open(_TREE_PATH+str(qhash)+"/lookup.json",'w')
		bucketTableFile.write("{}")
		bucketTableFile.close()

	#Load bucketTable
	bucketTableFile=open(_TREE_PATH+str(qhash)+"/lookup.json",'r+')
	bucketTable = json.loads(bucketTableFile.read())

	if query not in bucketTable.keys():

		#File is not cache! Create PNG in bucket.
		filename=str(len(os.listdir(_TREE_PATH+str(qhash))))+".png"


		fn=query.split(",")[0]
		rest=query.split(",")[1:]
		myParams={i[0]:i[1] for i in map(lambda x:x.split("="),rest)}



		if not TeXToGraph(fn,_TREE_PATH+str(qhash),filename,myParams):
			#An error has occurred while rendering the LaTeX. 
			return open(handleTeXRenderError("An error has occurred while rendering LaTeX."))

		#Update bucketTable
		bucketTable[query]=filename

		#Write back to bucketTableFile
		bucketTableFile.seek(0)
		bucketTableFile.write(json.dumps(bucketTable))
		bucketTableFile.close()

	#Return path to newly created/existing file
	return open(_TREE_PATH+str(qhash)+"/"+bucketTable[query]).read()

def hashFunc(s):
	"""
	Call some hashfunc and return the result.
	Goes "hashy hashy".
	"""
	return abs(hash(s))

def TeXToGraph(fn,targetDir,name,paramsIn):
	"""
		Renders a graph in query to a png in targetDir named name. Return true if successful, false if not.
	"""
	params={
		'xmin':-10,
		'xmax':10,
		'ymin':-10,
		'ymax':10,
		'xlabel':"x",
		'ylabel':"y",
	}
	for i in paramsIn:
		if i!='xlabel' and i !='ylabel':
			params[i]=int(paramsIn[i])
		else:
			params[i]=paramsIn[i]
	print params
	print fn
	try:
		check_output("./to_graph.sh {0} {1} {2} {3} {4} {5} {6} {7} {8}".format(fn,params['xmin'],params['xmax'],params['ymin'],params['ymax'],params['xlabel'],params['ylabel'],targetDir,name).split())
	except CalledProcessError:
		return False
	return True


def handleTeXRenderError(errorMsg):
	"""
		Handles an error encountered while attempting to render a TeX string
	"""
	print errorMsg
	return "assets/img/error.png"
