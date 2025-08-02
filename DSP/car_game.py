name=""
started=False
while name.lower()!="quit":
    name=input("> ").lower()
    if name.lower()=="start":
        if started:
            print("car already started !")
        else:
            started=True
            print("let's go !")
    elif name.lower() =="stop":
        if not started:
            print("car is in rest")
        else:
            started=False
            print("stopped !")
    elif name.lower()=="help":
        print("start=start the car !")
        print("stop=stop the car !")
        print("quit=to exit the game")
    elif name.lower()=="quit":
        break
    else:
        print("wrong input")



