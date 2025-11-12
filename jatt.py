print("welcome")

def run():
    print("pres 1 for contionus")
    print("press 2 for exit")

    a =int(input("press number for continue & exit"))

    if a==1:
        book()
    elif a==2:
        print("thanks for visit")



def book():
    print("press 1 for book1")
    print("press 2 for book2")
    print("press 1 for book1")
    print("press 1 for book1")

    b=int(input("enter book number to continue"))
    if b==1:
       print("English:--the poetry of a king")
       
       run()


    elif b==2:
      print("Ramyan:--it is a ancient book")

      run()

    elif b==3:
      print("hanuman chailsa:-- hanuman chailsa is devoional hym praising lord hanuman")

    run()

book()



     
