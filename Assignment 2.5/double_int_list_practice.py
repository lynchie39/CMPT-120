def main():
  
  #set this to any double
  doubleValue = 12
  
  #set this to any int
  intValue = 3
  
  #print out addition, subtraction, multiplication, and division of these two values
  
  print(doubleValue + intValue)
  print(doubleValue / intValue * intValue - intValue)
  
  #populate this list
  myFriends = ["George", "Tamas", "Henry", "Brandon", "Mark", "Rob", "Glenn"]
  
  #print out your friends at index 2 and index 3

  print(myFriends[2])
  print(myFriends[3])
  
  #populate this list with five numbers
  fiveNumbers = [1, 2, 3, 4, 5]
  
  #do each of the four equations with different numbers each time.

  print(fiveNumbers[1] + fiveNumbers[3])
  print(fiveNumbers[0] - fiveNumbers[4])
  print(fiveNumbers[2] * fiveNumbers[3])
  print(fiveNumbers[3] / fiveNumbers[4])



  
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[1] = 19
  fiveNumbers[4] = 21
  #print out the list
  print(fiveNumbers)
  
main()
