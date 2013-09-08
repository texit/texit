from urllib2 import urlopen

def generateTeXQuery(s):
	"""
	Returns the texit latex query for the argument latex string.
	"""
	return "http://tex.sh/tex/$"+s+"$.png"

def generateGraphQuery(s):
	"""
	Returns the texit graph query for the argument expression.
	"""
	return "http://tex.sh/graph/$"+s+"$.png"

def getGraphImage(s):
	"""
	Returns a stream containing a render of latex string s.
	"""
	return urlopen(generateTeXQuery(s));

def getTexImage(s):
	"""
	Returns a stream containing a graph of expression s.
	"""
	return urlopen(generateGraphQuery(s));
