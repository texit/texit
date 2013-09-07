#!/bin/bash -u

echo ''$1'' > equation.tex
pdflatex -interaction=nonstopmode template.tex
if [ $? -eq 0 ]; then
  convert -density 300 template.pdf -quality 90 equation.png
fi
rm equation.tex *.aux *.log
