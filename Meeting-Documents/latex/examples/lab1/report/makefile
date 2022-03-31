.PHONY: clean

all:
	mkdir -p build
	pdflatex -output-directory=build main.tex

watch:
	zathura build/main.pdf &
	ls *.tex | entr make

clean:
	rm ./build/*
