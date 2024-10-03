#!/usr/bin/env python3
import html

def main():

    trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }
    q = trivia[2][question]
    print(q)
    i1 = trivia[4][0]
    i2 = trivia[4][1]
    i3 = trivia[4][2]
    c = trivia[3]
    print(c) 

main()
