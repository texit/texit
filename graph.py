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
        if not TeXToGraph(query,_TREE_PATH+str(qhash),filename):
            #An error has occurred while rendering the LaTeX. 
            handleTeXRenderError("An error has occurred while rendering LaTeX.")

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

def TeXToGraph(fn,targetDir,name,optionalParams):
    """
        Renders a graph in query to a png in targetDir named name. Return true
        if successful, false if not.
    """

    params = {
        'xmin': -10,
        'xmax': 10,
        'ymin': -10,
        'ymax': 10,
        'xlabel': 'x',
        'ylabel': 'y',
    }

    for k, v in optionalParams:
        params[k] = v

    print("./to_graph.sh '{0}' '{1}' '{2}' '{3}' '{4}' '{5}' '{6}' {7} {8}".format(
        fn,
        params['xmin'],
        params['xmax'],
        params['ymin'],
        params['ymax'],
        params['xlabel'],
        params['ylabel'],
        params['targetdir'],
        params['name']))
    try:
        check_output("./to_graph.sh {0} {1} {2} {3} {4} {5} {6} {7} {8}".format(fn,xmin,xmax,ymin,ymax,xlabel,ylabel,targetDir,name).split())
    except CalledProcessError:
        return False
    return True


def handleTeXRenderError(errorMsg):
    """
        Handles an error encountered while attempting to render a TeX string
    """
    print errorMsg
    #TODO: Handle errors and tell the user what an idiot he is for submitting malformed syntax in a way that doesn't cause the server to terminate like it does now.
    raise Exception("Something really bad happened.")

def paramsIn(query):
    return { x[0]:x[1] for x in map(lambda x:x.split("="),query.split("|")) }
