def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  for quote in quotes[3:7]:
    print(quote)

if __name__== "__main__":
  primary()
