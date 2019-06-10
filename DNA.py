#  File: DNA.py

#  Description:Select the longest common sequence of DNA pairs 

#  Student Name: Tuan Nguyen



def shortlong(firstStr, secondStr):
  # return a short strand, a long strand and the length of the shorter strand

  if len(firstStr) < len(secondStr):
      return (firstStr, secondStr, len(firstStr))
  return (secondStr, firstStr, len(secondStr))

def main():
  # main function to find common sequences in a given sequence of DNA 

  #get number of pairs and print header
  in_file = open('dna.txt', 'r')
  pairs = in_file.readline().rstrip('\n')
  print("Longest Common Sequences")

  for pair in range(eval(pairs)): #loop over number of pairs of strands

    #get a pair of strands
    print()
    firstStr = in_file.readline().upper().strip('\n')
    secondStr = in_file.readline().upper().strip('\n')

    #initialize parameters
    shortStr, longStr, length = shortlong(firstStr, secondStr)
    longest = []
    sequenceLength = length

    #loop over pair to find sequences
    while ((not longest) and sequenceLength >= 2):
      #loop to control length of sequence
      for x in range(length - sequenceLength + 1):
        #loop to control position of sequence
        newSequence = shortStr[x:x+sequenceLength]
        if (newSequence in longStr):
          #check if sequence from first is in second
          longest.append(newSequence)
      sequenceLength -= 1

    #print results
    print("Pair %d:" %(pair + 1), end='')
    if longest:
      for x in longest:
        print('\t%s' %x)
    else:
      print("\tNo Common Sequence Found")

  in_file.close()

main()
