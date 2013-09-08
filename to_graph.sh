#!/bin/bash -u
#
# Usage: ./to_png.sh 'graph expression' xmin xmax ymin ymax xlabel ylabel
#
# Example: ./to_png.sh '\frac{2}{3}'

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
	convert -density 300 equation.pdf -quality 90 equation.png
fi
rm equation.tex *.aux *.log
mv equation.png $8/$9
