def largestWord(inputted_string):
    inputted_string = sorted(inputted_string, key = len)
    print(inputted_string[-1])
  

if __name__ == "__main__":
    inputted_string = input()
    l = list(inputted_string.split(" "))
    largestWord(l)
