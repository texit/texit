#!/bin/bash -u
#
# Usage: ./to_png.sh 'LaTeX Equation to Render'
#
# Example: ./to_png.sh '\frac{2}{3}'

echo ''$1'' > equation.tex
pdflatex -interaction=nonstopmode template.tex
if [ $? -eq 0 ]; then
  pdf2svg template.pdf equation.svg
fi
rm equation.tex *.aux *.log
