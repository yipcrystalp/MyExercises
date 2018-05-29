

#define 'greet()'
def greet():
    print ("Hey there!")
    name = raw_input("Please type your name: ")
    print ("Nice to meet you " + name)
    country = raw_input("So where are you from? ")
    print ("Interesting, so you're from " + country)
    print ("I'd love to visit there someday! :)")


    choice = raw_input("Can I sing a song for you? yes or no? ")

    if choice == "yes":
        s = open("birds.txt", "r")
        song = s.read()
        print song
    else:
        print("Okay, no problem, goodbye! :)")

greet();
