# Hangman game.
import random

MotMystere=["mercury","venus","earth","march","jupiter","saturn","uranus","neptune"]

while True:
    jouer=input("write play to play to Hangman game, write another thing to quit")
    if jouer != 'play':
       print("good bye")
       break
    print("\nlet's go !\n \nyou have 6 life\n")
    vie = 6
    mot = random.choice(MotMystere)
    longueur = len(mot)
    lettres = set(mot)
    barre = ["_"]
    barre = barre * longueur
    grandeur = longueur
    resultat = longueur * "_ "
    while True :
        print(resultat,'\n')
        lettre_choisi = input("choose a letter  ")
        if lettre_choisi in mot :
            if lettre_choisi in barre:
                print ("you had already chosen\n")
            else:
                print("well played!\n")
                index = 0
                lettres.remove(lettre_choisi)
                while index < longueur - 1:
                    try:
                        index = int(mot.index(lettre_choisi, index))
                        barre[index] = lettre_choisi
                        index = index + 1
                    except ValueError:
                        break
            resultat = ' '.join(barre) + '\n'
        else:
            print("Raté\n")
            vie=vie-1
            print("you still have",vie,"life\n")
        if vie==0 :
            print("you lose\n")
            print("it was: ",mot,'\n')
            break
        elif len(lettres)==0 :
            print(resultat)
            print("Congratulation ! you find the word!\n")
            break