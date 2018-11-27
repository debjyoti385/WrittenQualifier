all:
	pdflatex -shell-escape main.tex
	bibtex main
	pdflatex -shell-escape main.tex

pdf:
	bibtex main
	pdflatex -shell-escape main.tex
	pdflatex -shell-escape main.tex

clean:
	rm -f main.aux main.bbl main.blg main.log main.pdf main.out
