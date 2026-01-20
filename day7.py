import random
stages = ['''
 +-------+
 |       |
 0       |
/|\      |
/ \      |

=============
''','''
+-------+
 |       |
 0       |
/|\      |
/        |

=============
''','''
+-------+
 |       |
 0       |
/|\      |
         |

=============''','''
+-------+
 |       |
 0       |
/|       |
         |

=============''','''
+-------+
 |       |
 0       |
/        |
         |

=============''','''
+-------+
 |       |
 0       |
         |
         |

=============''','''
+-------+
 |       |
 0       |
/|\      |
/ \      |

=============''']
lives = 6
word_list = ["aardvarrk","baboon","camel"]
choosen_word = random.choice(word_list)
print(choosen_word)

placeholder = " "
word_lenth = len(choosen_word)
for position in range(word_lenth):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter>>>").lower()
    print(guess)
    display = " "

    for letter in choosen_word:
        if letter == guess:
             display += letter
             correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
             display += "_"
    print(display)
    # if guess not in choosen_word:
    #     lives -= 1
    #     if lives == 0:
    #         game_over = True
    #         print("You lose!")
    # if "_" not in display:
    #     game_over = True
    #     print("you win")
    # print(stages[lives])