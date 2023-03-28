# # Variable test
# global var1 ,var2,var3,var4,var5,var6,var7,var8,var9
# var1 = "X"
# var2 = "O"
# var3 = "_"
# var4 = "X"
# var5 = "_"
# var6 = "_"
# var7 = "O"
# var8 = "O"
# var9 = "X"

question1 = input("What is your name:  ")
# # The layout

  

# # list2[0].index('O')
# # Players
# # list[0]
# print(list2)
# list2[0][2] = "James"

mydict = {
    "var1" : "X",
    "var2"  : "O",
    "var3" : "_",
    "var4" : "X",
    "var5" : "_",
    "var6" : "_",
    "var7" : "O",
    "var8" : "O",
    "var9" : "X"
}

# for i in range(2):
#     print(mydict["sfs"])

def player1():
    global var1 ,var2,var3,var4,var5,var6,var7,var8,var9
    global list2
    print("Hello",question1,"\nPlease look at the sample and use the numbers as your guide to pick the position you decide to place your pawn\n")

    question2 = int(input("Type in the number you chose as the position for your pawn:  "))

    if question2 == 1 or 2 or 3:
        if question2 == 1:
            mydict["var1"] = "Z"
        elif  question2 == 2:
            mydict["var2"] = "V"
        else:    
            mydict["var3"] = "0"
            
    if question2 == 4 or 5 or 6:
        if question2 == 4:
            mydict["var4"] = "J"
        elif  question2 == 5:
            mydict["var5"] = "0"
        else:    
            mydict["var6"] = "X"
            
    if question2 == 7 or 8 or 9:
        if question2 == 7:
            mydict["var7"] = "0"
        elif  question2 == 8:
            mydict["var8"] = "P"
        else:    
            mydict["var9"] = "E"
        
player1()

list2 = [[mydict["var1"],mydict["var2"],mydict["var3"]],[mydict["var4"],mydict["var5"],mydict["var6"]],[mydict["var7"],mydict["var8"],mydict["var9"]]]

for i in range(len(list2)):
    for j in range(len(list2)):
        print(list2[i][j],end='  ')
    print("\n")        