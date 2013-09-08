texit.
======
Texit is a simple webservice for rendering LaTeX mathematical expressions to png files.

Usage
-----
	**Render png for latex string**
	curl http://tex.sh/tex/$<your latex code here>$.png

	Example:
	curl http://tex.sh/tex/$\integral_{-\infty}^{\infty}f(t)e^{-2\pi i\omega t}dt$.png
	![Alt Text](http://tex.sh/tex/$\integral_{-\infty}^{\infty}f(t)e^{-2\pi i\omega t}dt$.png "Image")

	

	**Render png for graph**
	curl http://tex.sh/graph/<your function expression here>
