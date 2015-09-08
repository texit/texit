#!/bin/bash -u
#
# Usage: ./to_graph.sh 'graph expression' xmin xmax ymin ymax xlabel ylabel
#
# Example: ./to_graph.sh '\frac{2}{3}'

echo $2 > test.txt

echo '
\documentclass[preview]{standalone}
\usepackage{tikz,pgfplots}
\begin{document}
\begin{tikzpicture}
  \begin{axis}[
  	xmin='$2',
  	xmax='$3',
  	ymin='$4',
  	ymax='$5',
	samples=500,
	smooth,
    xlabel='$6',
    ylabel='$7',
  ]
    \addplot[domain='$2':'$3'] {'$1'};
  \end{axis}
\end{tikzpicture}
\end{document}' > equation.tex


pdflatex -interaction=nonstopmode equation.tex
if [ $? -eq 0 ]; then
  pdf2svg equation.pdf equation.svg
fi
rm equation.tex *.aux *.log
mv equation.svg $8/$9
