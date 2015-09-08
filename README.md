# texit

A simple web service that makes beautiful typesetting easy anywhere on the web.

## Usage

### Equations

Get rendered SVG of provided LaTeX equation.

    https://texit.apps.zachlatta.com/tex/$<latex goes here>$

#### Markdown Example

You'll have to escape backslashes and friends when using Markdown.

    ![Discrete Fourier Transform](https://texit.apps.zachlatta.com/tex/$\\sum_{i=-\\infty}^{\\infty} x[n] e^{-i\\omega t}$)

becomes ![Example](https://texit.apps.zachlatta.com/tex/$\\sum_{i=-\\infty}^{\\infty} x[n] e^{-i\\omega t}$)

### Graphs

Get a graph of a function:

    https://texit.apps.zachlatta.com/graph/x^2

Output:

![Basic Parabola](https://texit.apps.zachlatta.com/graph/x^2)

#### Parameters

Parameters are passed after the function to graph.

    https://texit.apps.zachlatta.com/graph/x^2,xmin=-5,xmax=+5,ymin=0,xlabel=label

This renders out to the following.

![Example Graph](https://texit.apps.zachlatta.com/graph/x^2,xmin=-5,xmax=+5,ymin=0,xlabel=label)

| Valid parameters |
| ---------------- |
| xmin             |
| xmax             |
| ymin             |
| ymax             |
| xlabel           |
| ylabel           |
