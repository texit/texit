import os;
import json;

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
			handleTeXRenderError("An error has occurred while renering LaTeX");

		#Update bucketTable
		bucketTable[query]=filename;

		#Write back to bucketTableFile
		bucketTableFile.write(json.dumps(bucketTable));

	#Return path to newly created/existing file
	return _TREE_PATH+str(qhash)+bucketTable[query];




#Pointless comment

def hashFunc(s):
	"""
	Call some hashfunc and return the result.
	Goes "hashy hashy".
	"""
	return hash(s);

def TeXToPng(query,targetDir,name):
	"""
		Renders a latex string in query to a png in targetDir named name. Return true if successful, false if not.
	"""
	pass

def handleTeXRenderError(errorMsg):
	"""
		Handles an error encountered while attempting to render a TeX string
	"""
	print errorMsg;
	#TODO: Handle errors and tell the user what an idiot he is for submitting malformed syntax in a way that doesn't cause the server to terminate like it does now.
	raise RuntimeException("Something bad happened.");
