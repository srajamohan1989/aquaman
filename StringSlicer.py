#Given a string of odd length greater 7, return a string made of the
#  middle three chars of a given String

def strslicer(str):
    if(len(str)<=7):
        print("Enter string with length greater than 7")
    else:
        middleindex= int(len(str)/2)
        print(text[middleindex-1:middleindex+2])
        
text=input("Enter a string of lenght odd and greater than 7: ")
strslicer(text)