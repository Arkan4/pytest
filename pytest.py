#!/usr/bin/python

print "Hello world"

num1 = 1
num2 = 1.1
var1 = "Maly mnau"

#print(type(num1))


string1 = "male maciatko papalo buchtu"
string2 = "maciatko"

#if string2 in string1:
#    print "Success"
#else:
#    print "Nope"


cuteAnimalsList = ['kittens', 'maciatko', 'puppies', 'ducklings', 'parrots']
#print cuteAnimalsList[0]

#if "puppies" in cuteAnimalsList:
#    print "Puppies located"

count = 0
animals = ['','','']
position = 0

#print animals
#animals[position] = str(num1)
#print animals




for x in cuteAnimalsList:
    print "Currently on " + x
    if 'a' in x:
        count += 1
        print x + ": letter a located"
        animals[position] = str(x)
        position += 1


print "Number of animals containing letter 'a' in list is: %d " %(count) + " and they are: " + str(animals)
