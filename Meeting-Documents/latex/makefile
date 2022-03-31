.PHONY: clean

all:
	mkdir -p build
	pdflatex -output-directory=build cv_eu.tex

watch:
	ls *.tex | entr -r make

clean:
	rm -r build
