# function to get contact details by first name
def readByFirstName(fname):
  if fname in fileList:
    foundContacts = []
    outcome = ""
    for itr in range(len(fileList)):
      if(fileList[itr] == fname):
        getContacts = []
        getFName = fileList[itr]
        getLName = fileList[(itr - 1)]
        getPhoneNumber = fileList[(itr + 1)]

        getContacts.append(getFName)
        getContacts.append(getLName)
        getContacts.append(getPhoneNumber)
        foundContacts.append(getContacts)
    
    for elem in foundContacts:
      userContactDetails = ""
      for subElem in elem:
        userContactDetails += subElem + "\n"
      outcome += userContactDetails

    return outcome

  else:
    return "No such entry found!"

# function to get contact details by last name
def readByLastName(lname):
  if lname in fileList:
    foundContacts = []
    outcome = ""
    for itr in range(len(fileList)):
      if(fileList[itr] == lname):
        getContacts = []
        getLName = fileList[itr]
        getFName = fileList[(itr + 1)]
        getPhoneNumber = fileList[(itr + 2)]

        getContacts.append(getFName)
        getContacts.append(getLName)
        getContacts.append(getPhoneNumber)
        foundContacts.append(getContacts)
    
    for elem in foundContacts:
      userContactDetails = ""
      for subElem in elem:
        userContactDetails += subElem + "\n"
      outcome += userContactDetails

    return outcome
  else:
    return "No such entry found!"

# function to get contact details by phone number
def readByPhoneNumber(phone):
  if phone in fileList:
    foundContacts = []
    for itr in range(len(fileList)):
      if(fileList[itr] == phone):
        getContacts = []
        getPhoneNumber = fileList[itr]
        getFName = fileList[(itr - 1)]
        getLName = fileList[(itr - 2)]

        getContacts.append(getFName)
        getContacts.append(getLName)
        getContacts.append(getPhoneNumber)
        foundContacts.append(getContacts)
    
    for elem in foundContacts:
      userContactDetails = ""
      for subElem in elem:
        userContactDetails += subElem + "\n"
      outcome += userContactDetails

    return outcome
  else:
    return "No such entry found!"

# function to display result (this function will call itself again-and-again if everytime the user select a wrong option)
def dispResult(getChoice):
  if(getChoice == "1"): 
    getLastName = input("Please enter the last name you would like to search for:\n")
    print(readByLastName(getLastName))
  elif(getChoice == "2"):
    getFirstName = input("Please enter the first name you would like to search for:\n")
    print(readByFirstName(getFirstName))
  elif(getChoice == "3"):
    getPhoneNumber = input("Please enter the phone number you would like to search for:\n")
    print(readByPhoneNumber(getPhoneNumber))
  elif(getChoice == "0"):
    exit()
  else:
    print("Bad choice! please select a number from 1,2,3 or 0")
    getChoice = input("Enter a choice: ")
    dispResult(getChoice)

# main program with Exception handling
try:
  file = open("entries.txt", "r")
  fileList = []
  for e in file:
    fileList.append(e.replace("\n", "")) # appending each line of the file in a list by removing new-line character from it

  print("My Contacts File Program\n")
  print("Please choose from the following options:")
  print("1. Look up contact by last name")
  print("2. Look up contact by first name")
  print("3. Look up contact by phone number")
  print("0. QUIT")
  
  getFirstName = ""
  getLastName = ""
  getPhoneNumber = ""

  getChoice = input("Enter a choice: ")
  if(getChoice == "1"): 
    getLastName = input("Please enter the last name you would like to search for:\n")
    print(readByLastName(getLastName))
  elif(getChoice == "2"):
    getFirstName = input("Please enter the first name you would like to search for:\n")
    print(readByFirstName(getFirstName))
  elif(getChoice == "3"):
    getPhoneNumber = input("Please enter the phone number you would like to search for:\n")
    print(readByPhoneNumber(getPhoneNumber))
  elif(getChoice == "0"):
    exit()
  else:
    print("Bad choice! please select a number from 1,2,3 or 0")
    getChoice = input("Enter a choice: ")
    dispResult(getChoice)

except:
  print("unable to open the file!")
finally:
  file.close()