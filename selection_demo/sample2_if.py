# ---------------------------------

# File          : 
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  :  
# Modified Date : 
# Description   :
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

if __name__ == '__main__':
    grade = 75
    module = "Python"

    if (grade >= 70) and module == "Python":
        print("You have a distinction")
    elif(grade >= 60):
        print("You have secured M.1")
    elif (grade >= 50):
        print("You have secured M.2")
    elif(grade >= 40):
        print("You have secured M.3")
    else:
        print("You have failed")