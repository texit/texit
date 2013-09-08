import os;
import json;
from subprocess import check_output, CalledProcessError

#Constants
_TREE_PATH="data/tex/";


def renderTex(query):
	"""
		Returns the path to a png file that
		contains the tex render of the query.
		Creates the png file itself if it 
		does not already exist.
	"""
	#Compute the hash of the query string
	qhash = hashFunc(query); 


	if (not os.path.exists(_TREE_PATH+str(qhash))):

		#Create bucket if it doesn't already exist.
		os.makedirs(_TREE_PATH+str(qhash));

		#Create the lookup table for the bucket.
		bucketTableFile=open(_TREE_PATH+str(qhash)+"/lookup.json",'w');
		bucketTableFile.write("{}");
		bucketTableFile.close();



	#Load bucketTable
	bucketTableFile=open(_TREE_PATH+str(qhash)+"/lookup.json",'r+');
	bucketTable = json.loads(bucketTableFile.read());

	if query not in bucketTable.keys():

		#File is not cache! Create PNG in bucket.
		filename=str(len(os.listdir(_TREE_PATH+str(qhash))))+".png"
		if not TeXToPng(query,_TREE_PATH+str(qhash),filename):
			#An error has occurred while rendering the LaTeX. 
			return open(handleTeXRenderError("An error has occurred while rendering LaTeX."));

		#Update bucketTable
		bucketTable[query]=filename;

		#Write back to bucketTableFile
		bucketTableFile.seek(0);
		bucketTableFile.write(json.dumps(bucketTable));
		bucketTableFile.close();

	#Return path to newly created/existing file
	return open(_TREE_PATH+str(qhash)+"/"+bucketTable[query]).read();




#Pointless comment

def hashFunc(s):
	"""
	Call some hashfunc and return the result.
	Goes "hashy hashy".
	"""
	return abs(hash(s));

def TeXToPng(query,targetDir,name):
	"""
		Renders a latex string in query to a png in targetDir named name. Return true if successful, false if not.
	"""
	print (query,targetDir+"/"+name);
	try:
		check_output(["./to_png.sh",query]);
		check_output("mv equation.png {0}".format(targetDir+"/"+name).split());
	except CalledProcessError:
		return False
	return True
	

def handleTeXRenderError(errorMsg):
	"""
		Handles an error encountered while attempting to render a TeX string
	"""
	print errorMsg;
	return "assets/img/error.png"
