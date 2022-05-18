final/paper.pdf: paper.tex plot-data.png
	pdflatex -output-directory final paper.tex &> /dev/null

plot-%.png: %.dat plot.py
	python plot.py $*.dat $@

watch:
	find . -type f -not -path "./final/*" | entr make
