import random

list = [

    {
        "name": "Cristiano Ronaldo",
        "description" : "a football player",
        "number of follower": "346",
        "country": "portugal",
    },

    {
        "name": "Ariana Grande",
        "description" : "Musician and actress",
        "number of follower": "183",
        "country": "United States",
    },

    {
        "name": "Dwayne johnson",
        "description" : "Actor",
        "number of follower": "181",
        "country": "United States",
    },

    {
        "name": "Selena Gomez",
        "description" : "Musician and actress",
        "number of follower": "174",
        "country": "United States",
    },

    {
        "name": "kylie Jenner",
        "description" : "Reality show",
        "number of follower": "172",
        "country": "United States",
    },

    {
        "name": "Kim Kardashian",
        "description" : "Musician and actress",
        "number of follower": "167",
        "country": "United States",
    },

    {
        "name": "Lionel messy",
        "description" : "Footballer",
        "number of follower": "149",
        "country": "Argentina",
    },

    {
        "name": "Beyance",
        "description" : "Musician",
        "number of follower": "145",
        "country": "United States",
    }

]

def compare(a, b):
    if a > b:
        return "a"
    else:
        return "b"

def choose_a(l):
    a = l[random.randint(0, len(l) - 1)]
    return  a
def choose_b(l):
    b = l[random.randint(0, len(l) - 1)]
    return b

print("Welcome to the game")
end = False
score = 0
a = choose_a(list)
b = choose_b(list)
while not end:
    if a != b:
        guess= input(f"Who has the more followers?\nA: {a["name"]} a {a["description"]} from {a["country"]}\nor B: {b["name"]} a {b["description"]} from {b["country"]} type A,or B:").lower()
        if guess != "a" and guess !="b":
            print("Please enter either A or B")
            break
        result = compare(int(a["number of follower"]),int(b["number of follower"]))
        if result == guess:
            score += 1
            print(f"You got it! your score is {score}")
            a = b
            choose_b(list)

        else:
            end = True
            print(f" sorry it was wrong. Your score is: {score}")
    else:
        b = choose_b(list)















