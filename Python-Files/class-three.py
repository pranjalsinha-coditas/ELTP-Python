message: str = "This is a message"
name: str = "Pranjal"

concat_message = message + " " + name
print(concat_message)

message = f"{message} {name}"
print(message)

# sentence = "This is a message"
# length = len(message)

# new_length = sentence._len_(sentence)
# print(length)

#slicing

word: str = "bottle"

#btl
print(word[0:5:2])
print(word[-6:-1:2])
print(word[0:-1:2])
print(word[0:-1:2])
print(word[-6:5:2])

#tle
print(word[3:6:1])
print(word[-3::1])
print(word[-3:6:])


#lt 
print(word[4:-7:-2])
print(word[4::2])





