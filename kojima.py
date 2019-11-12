import random

print("Welcome to the Automated Kojima Name Generator.")
print("As a Kojima character, you may have multiple names.")
print("Determining how many names you have...")
randnum1 = random.randrange(1,6)
if randnum1 == 6:
    print("You have one name and six alternate names. After completing this generator, complete it again.")
else:
    print("You only have one name. Thank goodness, that makes this easier.")
print("First, I need some information from you.")
realname = input("What is your name? ")
longjob = input("What do you do at your occupation? ")
shortjob = input("Condense the verb in your answer to a single -er noun. ")
petbreed = input("What was your first pet's specific species/breed? If you never had a pet, please answer with an animal you wish you owned. ")
longmemory = input("What's your most embarrassing childhood memory? Be specific. ")
shortmemory = input("Now condense that memory into two words! ")
dontstab = input("What is the object you'd least like to be stabbed by? ")
talent = input("What is something you are good at? (verb ending in -ing) ")
carrots = input("How many carrots do you believe you could eat in one sitting, if someone,like, forced you to eat as many carrots as possible? ")
intfear = input("What is your greatest intangible fear? (e.g. death, loneliness, fear itself) ")
tfear = input("What is your greatest tangible fear? (e.g. horses) ")
recent = input("What is the last thing you did before starting this worksheet? ")
condition = input("What condition is your body currently in? (single word answer) ")
state = input("Favorite state of matter? ")
kinda = input("A word your name kind of sounds like? (e.g. Brian -> Brain) ")
zodiac = input("What is your Zodiac sign? ")
mbti = input("If you had to define your personality in one word, what would it be? ")
print("Great! Now some other information. ")
print("See, Kojima character names reflect his own idiosyncrasies. He can't help himself. ")
kurt = input("Who is your favorite film character? (NOTE: must be played by Kurt Russell) ")
stan = input("What is the last word of the title of your favorite Kubrick film? ")
band = input("What is the first word in the title of your favorite Joy Division album? ")
npr = input("What is a scientific term you picked up from listening to NPR once? ")
guns = input("What is a piece of military hardware you think looks cool even though war is bad? ")
longmads = input("What is something you'd enjoy watching Mads Mikkelson do? Be specific. ")
shortmads = input("Now condense that to one word. ")
print("Great! Now some quick things to clear up. ")
print("Sometimes, a character will have a plot-based condition that affects their name. ")
print("You, too, might have a condition that affects your name. ")
print("Determining if you have The-Man Condition...")
randnum2 = random.randrange(1,4)
if randnum2 == 4:
    print("You have this condition.")
    print("Your last name will include the suffix-man.")
    print("If your name already has -man at the end of it, I guess you're just going to have -manman at the end of your name.")
    theman = "man"
else:
    print("You do not have this condition.")
    theman = ""
print("Determining if you have the Condition Condition...")
randnum3 = random.randrange(1,8)
if randnum3 == 5:
    print("You have this condition.")
    print("You're big.")
    print("Your name must have the word Big at the beginning of it.")
    stat = "Big "
elif randnum3 == 7:
    print("You have this condition.")
    print("You're older than you once were.")
    print("Your nane must have the word Old at the beginning of it.")
    stat = "Old "
elif randnum3 == 8:
    print("You have this condition.")
    print("You know how you currently are.")
    stat = condition+" "
else:
    print("You do not have this condition.")
    stat = ""
print("Determining if you have the Clone condition...")
randnum4 = random.randrange(1, 12)
if randnum4 == 12:
    print("You are a clone of someone else, or you have been brainwashed into becoming a mental doppelganger of someone else.")
    print("Find someone who has completed this worksheet and replace 50% ofyour Kojima name with 50% of their Kojima name.")
else:
    print("You do not have this condition.")
print("Determining if you have the Kojima Condition...")
randnum5 = random.randrange(1, 100)
if randnum5 == 69:
    print("Oh no.")
    print("You are Hideo Kojima.")
    print("Hideo Kojima created you and is also you.")
    print("You are the man who created himself and there is nothing you can do about it.")
    print("You're in Kojima's world—your world—and that's just the breaks, pal.")
    print("Stop this worksheet now. You're Hideo Kojima. Go do the things that Hideo Kojima does.")
else:
    print("You do not have this condition.")
print("Great! Time to determine your name category.")
randnum6 = random.randrange(1,20)
if randnum6 == 1:
    print("You have a normal name.")
    kojimaname = stat+realname+theman
    print("Your Kojima name is.... ",kojimaname, ".")
    print("That's your name. Your Kojima name is probably just your actual name. Sorry if you were expecting something wild.")
elif randnum6 < 7:
    print("You have an occupational name.")
    randnum7 = random.randrange(1,4)
    if randnum7 == 1:
        fname = mbti
    elif randnum7 == 2:
        fname = talent
    elif randnum7 == 3:
        fname = kinda
    else:
        fname = kurt
    kojimaname = stat+fname+" "+shortjob+theman
    print("Your Kojima name is.... ",kojimaname,".")
elif randnum6 < 11:
    print("You have a horny name.")
    print("Kojima's characters and stories are irrevocably horny. Weirdly horny, sure, but horny nonetheless.")
    randnum7 = random.randrange(1,4)
    if randnum7 == 1:
        fname = state
    elif randnum7 == 2:
        fname = "Naked"
    elif randnum7 == 3:
        fname = talent
    else:
        fname = zodiac
    middle = input("Do you want your middle name to be Lickable? ")
    if middle == "Yes":
        mname = "Lickable "
    else:
        mname = ""
    kojimaname = stat+fname+" "+mname+petbreed+theman
    print("Your Kojima name is.... ",kojimaname,".")
elif randnum6 < 14:
    print("You have a The name.")
    randnum7 = random.randrange(1,4)
    if randnum7 == 1:
        lname = intfear
    elif randnum7 == 2:
        lname = tfear
    elif randnum7 == 3:
        lname = shortmemory
    else:
        lname = guns
    kojimaname = "The "+stat+lname+theman
    print("Your Kojima name is....",kojimaname,".")
elif randnum6 < 18:
    print("You have a cool name.")
    print("Kojima loves to be cool. Sometimes, his idea of cool is a bit strange, but it is always cool to Hideo Kojima, and that's what matters.")
    randnum7 = random.randrange(1,6)
    if randnum7 == 1:
        lname = stan
    elif randnum7 == 2:
        lname = band
    elif randnum7 == 3:
        lname = npr
    elif randnum7 == 4:
        lname = talent
    elif randnum7 == 5:
        lname = intfear
    else:
        lname = kinda
    kojimaname = stat+shortmads+" "+lname+theman
    print("Your Kojima name is....",kojimaname,".")
elif randnum6 < 20:
    print("You have a violent name.")
    randnum7 = random.randrange(1,4)
    if randnum7 == 1:
        lname = npr
    elif randnum7 == 2:
        lname = state
    elif randnum7 == 3:
        lname = guns
    else:
        lname = tfear
    kojimaname = stat+dontstab+" "+lname+theman
    print("Your Kojima name is....",kojimaname,".")
else:
    print("You have a name that lacks subtext.")
    kojimaname = stat+recent+theman
    print("Your Kojima name is....",kojimaname,".")
print("Now come up with a great backstory for your name. That's it. Bye.")
