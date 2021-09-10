print("Welcome to the Harry Potter game quiz")
score = 0
playing = input("Do you wish to play this game ? ")

if playing.lower() != "yes":
    print("That's a shame :( ")
    quit()
print("Good choice! Let's get started :) ")

answer = input("First question: Does Harry speaks Parseltongue ? ")
if answer.lower() == "yes":
    print("Someone saw the movies. Good job:) ")
    score+=1
else:
    print("Sorry that's not  the right answer.")
answer = input("Second  question: What is  Parseltongue ? ")
if answer.lower() == "languages of serpents":
    print("Wow :) ")
    score+=1
else:
    print("Sorry that's not  the right answer.")
answer = input("Third question: What is the true name of Voldemort? ")
if answer.lower() == "tom riddle":
    print("Fantastic :) ")
    score+=1
else:
    print("Sorry that's not  the right answer.")
answer = input("Final question: Who was the true owner of the elder wand after the battle of hogwarts ? ")
if answer.lower() == "harry potter":
    print("You are one hell of a fan :) ")
    score+=1
else:
    print("Sorry that's not  the right answer.")
print("Your score is " + str(score) + ".")
if score <= 2:
    print("you did not read the books or pay attention to the movies. ")
elif score >2:
    print("A true Harry potter fan.")
