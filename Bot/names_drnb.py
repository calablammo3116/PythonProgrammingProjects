# For this code, we are going to import a .txt file containing names and store these names in a massive list. Reading in the data from .txt files will make it easier
# to go in and edit the data later on, and because we will be using this data at least for a Discord bot that cna see if someone's nick is their actual name, we will def
# need to go in later and add names, because I guarantee I'll miss one or get something wrong.

# define the "namey()" function
def namey():    # originally, I had an argument in here called "namef" for "name file", but in order to make this work with the Discord "Real Name bot" program, I 
                    # got rid of that and just left it with no argument, that way I could make it so that it is pre-determined in the function that the .txt file being 
                    # inputted into the "namey()" function is "names.txt"
        
        # read in the file data
  namefile = open('names.txt', 'rt')  # originally, the first argument I had put in in the "open()" function was "namef" like my original argument for the "namey()"
                                            # function declared and initially defined above; then I changed it to be only the "names.txt" file as the argument, that way the 
                                            # "namey()" function would still return a value EVEN THOUGH it doesn't have an argument in the main program that I designed it to 
                                            # be imported into (the Discord "Real Name bot" program).

        # Declare a list to store all of our names
  names_list = []

        # Store each line in the inputted data file into its own index in the list, "names_list"
  for line in namefile:
      name = line.rstrip()    # strip the newline character from each line in the inputted .txt file using "rstrip()" and then store it in a variable called "name"
      names_list.append(name) # add the now-newline-character-stripped .txt file line to the end of the "names_list" list using the "append()" function, which is
                                # used to add an element to the end of a list ("NOT A TUPLE," because a tuple can only store a FIXED NUMBER of elements; it is useless for 
                                # anything bigger) by placing a period "." at the end of the name of a list and then it takes as an argument the element desired to read 
                                # in to the end of the list. So basically, its syntax is "list.append(element)".

  namefile.close()

        # print(names_list)     <-- this line prints the list based on the .txt file we imported. I just put it there for testing purposes. You do not actually need it
        #                           it to run the program. It is just there to make sure that the list that is imported actually gets stored in and is able to be put out 
        #                           correctly.

  return names_list

def lnamey():
  lnamefile = open("names.txt","rt")

  lnames_list = []

  for line in lnamefile:
    name = line.rstrip() # get the name, w/o the newline character
    lname = name.lower()  # make the whole name lowercase
    lnames_list.append(lname)   # add the name to the end of the lowercase names list
  
  lnamefile.close()

  return lnames_list

def unamey():
  unamefile = open("names.txt","rt")

  unames_list = []

  for line in unamefile:
    name = line.rstrip()
    uname = name.upper()
    unames_list.append(uname)
  
  unamefile.close()

  return unames_list


# define the "main()" function
def main():
  namey()
  lnamey()
  unamey()
  print("All names retrieved.\n")

# initialize the "main()" function
if __name__ == '__main__': main()