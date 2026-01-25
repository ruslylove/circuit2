#!/bin/bash
cd tex
latex -interaction=nonstopmode practice_16_13_a.tex
dvisvgm --no-fonts practice_16_13_a.dvi -o ../public/practice_16_13_a.svg
latex -interaction=nonstopmode practice_16_13_b.tex
dvisvgm --no-fonts practice_16_13_b.dvi -o ../public/practice_16_13_b.svg
latex -interaction=nonstopmode practice_16_13_c.tex
dvisvgm --no-fonts practice_16_13_c.dvi -o ../public/practice_16_13_c.svg
