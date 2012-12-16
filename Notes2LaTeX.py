#!/usr/bin/python

#Copyright 2012 Luca Stickley Raquel Munoz
#Distributed under the terms of the GNU General Public License v2

import sys #utility for cmd line
import datetime #date module

def main():
    today = datetime.date.today()
    date = str(today) # convert date to string
    filename = sys.argv[1] #import from cmd line 
    docname = filename + ' ' + date #combine date and filane name
    intro1 = '+----------------+'
    intro2 = '| Notes To LaTeX |'
    intro3 = '+----------------+'   
    f = open(docname, 'w+')
    f.write('\documentclass[11pt,a4paper]{article} \n')
    f.write('\\addtolength{\oddsidemargin}{-.5in} \n')
    f.write('\\addtolength{\evensidemargin}{-.5in} \n')
    f.write('\\addtolength{\\textwidth}{1.76in} \n')
    f.write('\usepackage[T1]{fontenc} \n')
    f.write('\usepackage{titling} \n')
    f.write('\\newenvironment{list1}{ \n')
    f.write('  \\begin{list}{\ding{113}}{% \n')
    f.write('      \setlength{\itemsep}{0.05in} \n')
    f.write('      \setlength{\parsep}{0in} \setlength{\parskip}{0in} \n')
    f.write('      \setlength{\\topsep}{0.2in} \setlength{\partopsep}{0in} \n')
    f.write('      \setlength{\leftmargin}{-.5in}}}{\end{list}} \n')
    f.write('\setlength{\droptitle}{-7em} \n')
    f.write('\n')
    f.write('\\title{')
    f.write(filename)
    f.write('} \n')
    f.write('\\author{Add Author name into script} \n')
    f.write('\date{')
    f.write(date)
    f.write('} \n')
    f.write('\\begin{document} \n')
    f.write('\maketitle \n')


    explanation = 'First type in the question then hit enter, at which point you will be asked to enter the answer'

    print intro1
    print intro2
    print intro3
    print explanation
   
    check_question = "y"
    check_notes = "n"

    while(check_question=="y"):
        question = raw_input('Question: ')
        f.write('\\begin{list1} \n')
        f.write('\item[] {\\bf ')
        f.write(question)
        f.write('?} \n')
        answer = raw_input('Answer: ')
        f.write('\item[] ')
        f.write(answer)
        f.write(' \n')
        check_notes = raw_input("Do you want to add notes to this answer? (y/n)")
        if (check_notes == "y"):
           notes = raw_input("Notes: ")
           f.write('\item[] \\textit{ ')
           f.write(notes)
           f.write('} \n')
           check_notes = "n"
        f.write('\end{list1} \n')
        check_question = raw_input('Continue? (y/n) ')

    f.write('\end{document} \n')
    f.close()

if __name__ == '__main__':
    main()


