all:
	cd 1_problem  && 	pdflatex -shell-escape main.tex
	cd 1_problem  && bibtex main
	cd 1_problem  && pdflatex -shell-escape main.tex
	pdftk 1_problem/01_question.pdf 1_problem/main.pdf cat output final.pdf

clean:
	rm -f final.pdf
