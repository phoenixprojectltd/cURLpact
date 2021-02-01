import os

loop = True
while True:
 link = input("Enter a link: ")
 outfile = input ("Enter the name of the output file (leave blank for none): ")
 args = input ("Enter any arguments you would like to use (leave blank for none): ")

 print("Now CURLing...")

 if outfile == "" and args == "":
    os.system("curl " + link)

 elif outfile == "" and args != "":
    os.system("curl "+ link + " " + args) 

 elif outfile != "" and args != "":
    os.system("curl " + link + " -o " + outfile + " " + args)

 elif outfile != "" and args == "":
    os.system("curl " + link + " -o " + outfile)

 if link == "":
    restart = input("Seems like you've not entered a link. Press ENTER to try again. ")