text= "world"
print ("find 'python':", text.find("python")) #This is used to find the word
replaced_text=text.replace("python", "html")
print ("replaced text:", replaced_text)
print ("length of the string", len(text))
print ("uppercase of the string", text.upper())
print ("lowercase of the string", text.lower())
reverse_text=text[::-1]
print ("reversed text is", reverse_text)
word="Hello"
split_text=text.split()
print ("the split word is", split_text)
join_text="#".join(text)
print ("The join word is", join_text)
greeting="Hello"
name="Raeena"
concate=greeting+name
print ("concatenated string", concate)
print ("Slice[3:5]", text[3:5])
try:
    index_value=text.index("world")
    print ("index value of the word", index_value)
except ValueError:
    print ("the word is not found")
   