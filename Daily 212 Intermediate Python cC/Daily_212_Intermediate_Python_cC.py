questions = ['Is your animal a mammal : ','Does it have a tail: ', 'Does it bark: ' ]
answers = [([1,1,1],'Dog'),([1,1,0],'Cat')]

x = []

def add():
    global questions
    global answers

    global x

    animal = input('What is your animal: ')

    add = input('What is a good question I could have asked to find \
    out your animal: ')

    questions.extend([add + ': '])
    answers[-1][0].extend([0])

    x.extend([1])

    answers.extend([(x,animal)])
    x = []
    ask()

def guess():
    for a in answers:
        global x
        if x == a[0]:
            c = input('Is your animal a ' + a[1] + ': ')

            if c == 'y':
                print('Got it correct.')
                x = []
                print('Play again.')
                ask()
            else:
                print("Got it wrong.")
                add()

def ask():
    for q in questions:
        global x
        guess()
        a = input(q)
        if a == 'y':
            n = questions.index(q)
            x.extend([1])
            guess()

        elif a == 'n':
            x.extend([0])
            guess()

        else:
            print('You must answer this y or n.')
            x = []
            ask()

def welcome():
    print('Welcome, think of an animal and I will try to guess it.')
    ask()

welcome()
add()