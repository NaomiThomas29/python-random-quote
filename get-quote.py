import random
def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
 
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  
  #adding lines
  file_object = open('quotes.txt', 'a')
  
  file_object.write('new line \n')
  
  file_object.close()


  
  # printing 5 quotes
  i = 1
  while i<6:
    rnd = random.randint(0, last)
    #removing extra line when printing
    print(quotes[rnd].strip("\n"))
    i+=1

if __name__== "__main__":
  primary()
