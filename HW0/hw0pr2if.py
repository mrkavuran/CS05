import random

print("""
Where am I? There are only 1s and 0s in here! I can't see anything!!!

""")

print(""" 
HAHAH! You are locked in the computer! But I am a mercyful device... I have an offer for you. We will play RPS with you!
If you win, I will let you go. If I win, you will clean my keyboard and screen everyday! Because the owner of this too busy (lazy) to do that...
""")
playerReady = input('Are you ready? yes/no')

if playerReady == 'yes':
    player = input('Great! Lets play... I will count from three! 3...2...1.. :')
    if player == 'rock':
        player = input('I am paper! You lost. 2 more games...')
        if player == 'rock':
            player = input('I am paper again! HAHAHA... This is your last chance...')
            if player == 'rock':
                print("""I am paper again! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'paper':
                print("""I am scissors! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'scissors':
                print("""I am rock! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
        if player == 'paper':
            player = input('I am scissors! HAHAHA... This is your last chance...')
            if player == 'rock':
                print("""I am paper! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'paper':
                print("""I am scissors! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'scissors':
                print("""I am rock! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
        if player == 'scissors':
            player = input('I am rock! HAHAHA... This is your last chance...')
            if player == 'rock':
                print("""I am paper! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'paper':
                print("""I am scissors! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'scissors':
                print("""I am rock! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
    if player == 'paper':
        player = input('I am scissors! You lost. 2 more games...')
        if player == 'rock':
            player = input('I am paper again! HAHAHA... This is your last chance...')
            if player == 'rock':
                print("""I am paper again! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'paper':
                print("""I am scissors! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'scissors':
                print("""I am rock! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
        if player == 'paper':
            player = input('I am scissors! HAHAHA... This is your last chance...')
            if player == 'rock':
                print("""I am paper! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'paper':
                print("""I am scissors! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'scissors':
                print("""I am rock! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
        if player == 'scissors':
            player = input('I am rock! HAHAHA... This is your last chance...')
            if player == 'rock':
                print("""I am paper! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'paper':
                print("""I am scissors! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'scissors':
                print("""I am rock! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
    if player == 'scissors':
        player = input('I am rock! You lost. 2 more games...')
        if player == 'rock':
            player = input('I am paper again! HAHAHA... This is your last chance...')
            if player == 'rock':
                print("""I am paper again! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'paper':
                print("""I am scissors! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'scissors':
                print("""I am rock! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
        if player == 'paper':
            player = input('I am scissors! HAHAHA... This is your last chance...')
            if player == 'rock':
                print("""I am paper! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'paper':
                print("""I am scissors! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'scissors':
                print("""I am rock! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
        if player == 'scissors':
            player = input('I am rock! HAHAHA... This is your last chance...')
            if player == 'rock':
                print("""I am paper! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'paper':
                print("""I am scissors! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)
            if player == 'scissors':
                print("""I am rock! Now go and clea... 
                        The player wakes up at the dorm because of noise. What time is it? 2 AM!! What is going on???

                        Upperclassman: FROSH RUUUUUUUN!!!
                        """)