course = "Python's Course for Beginners"
print(course)
note = 'This is my "maths" notebook'
print(note)
print(note[0]) #print first character
print(note[-3]) #print reverse character from last word
print(note[0:3]) #string slicing=> syntax: string[start:end] means as in this line, start from 0, upto index 3 but not including index 3  so this will print "Thi"

book = '''
Hi Bijaya,
how are you?
i hope you are good, and for your curiosity, i am fine here too
i cook food and eat in time, 
so don't worry about me
i misssssss you sooooooo soooooo muchhhhhhhh
reallyyyyyy
'''
print(book)



#todo
name = 'Jennifer'
print(name[1:-1]) #ennife

#formatted string
first = 'Babita'
last = 'Bhandari'
message = first + ' [' + last + '] is a coder'  # not ideal
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)


course = 'Python for beginner'
print(len(course))#len => no. of character
print(course.upper()) #upper=> convert all characters in upper case
print(course.lower()) #lower=>convert all character in lower case
print(course.find('P')) #simply gives the index value 
print(course.replace('beginner', 'absolute beginners')) #replace the first value by the second one, it may be a single character also
print('Python' in course )


