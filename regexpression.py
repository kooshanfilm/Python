

import re

def main():

 fh = open('sclices.py')
 for line in fh:
      match = re.search('(main)',line)
 if match:
     print(match)
     print(match.group())






if __name__ == '__main__': main()

