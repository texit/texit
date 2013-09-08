# texit

A simple web service that makes beautiful typesetting easy anywhere on the web.

## Usage

### Equations

Get rendered PNG of provided ![LaTeX](http://tex.sh/tex/$LaTeX$.png) equation.

    http://tex.sh/tex/$<latex equation here>$.png

#### Markdown Example

You'll have to escape backslashes and friends when using Markdown.

    ![Discrete Fourier Transform](http://tex.sh/tex/$\\sum_{i=-\\infty}^{\\infty} x[n] e^{-i\\omega t}$)

becomes ![Example](http://tex.sh/tex/$\\sum_{i=-\\infty}^{\\infty} x[n] e^{-i\\omega t}$)

### Graphs

Get a graph of a function:

    http://tex.sh/graph/x^2

Output:

![Basic Parabola](http://tex.sh/graph/x^2)

#### Parameters

Parameters are passed after the function to graph.

    http://tex.sh/graph/x^2,xmin=-5,xmax=+5,ymin=0,xlabel=label

This renders out to the following.

![Example Graph](http://tex.sh/graph/x^2,xmin=-5,xmax=+5,ymin=0,xlabel=label)

| Valid parameters |
| ---------------- |
| xmin             |
| xmax             |
| ymin             |
| ymax             |
| xlabel           |
| ylabel           |
