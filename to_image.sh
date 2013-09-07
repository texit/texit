#!/bin/bash -u
#
# Usage: ./to_image.sh 'LaTeX Equation to Render'
#
# Examples: 
#   ./to_image.sh '\frac{2}{3}' png
#   ./to_image.sh '\frac{3}{2}' svg

echo ''$1'' > equation.tex
pdflatex -interaction=nonstopmode template.tex
if [ $? -eq 0 ]; then
  convert -density 120 template.pdf -quality 90 "equation.$2"
fi
rm equation.tex *.aux *.log
