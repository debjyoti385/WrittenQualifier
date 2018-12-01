all: compile1 compile2 compile3 merge

1: compile1 merge

2: compile2 merge

3: compile3 merge

compile1:
	cd 1_problem  && 	pdflatex -shell-escape main.tex
	cd 1_problem  && bibtex main
	cd 1_problem  && pdflatex -shell-escape main.tex

compile2:
	cd 2_problem  && 	pdflatex -shell-escape main.tex
	cd 2_problem  && bibtex main
	cd 2_problem  && pdflatex -shell-escape main.tex

compile3:
	cd 3_problem  && 	pdflatex -shell-escape main.tex
	cd 3_problem  && bibtex main
	cd 3_problem  && pdflatex -shell-escape main.tex


merge:
	pdftk 1_problem/01_question.pdf 1_problem/main.pdf 2_problem/02_question.pdf 2_problem/main.pdf 3_problem/03_question.pdf 3_problem/main.pdf cat output final.pdf

clean:
	rm -f final.pdf
