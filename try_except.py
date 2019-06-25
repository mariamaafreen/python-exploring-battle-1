try:
  f = open("git_commands.txt")
  print(f)  

except:
  print("Something went wrong when writing to the file")
  
finally:
  f.close()