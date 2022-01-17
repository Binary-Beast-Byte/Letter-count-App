#You are responsible for writing a program that will get a message and a specific letter from a
# user and then count the number of occurrences of that letter in the given message. You
# program should count “H” and “h” as an occurence of h. Your program will then display a
# message to the user stating the occurrences of the given letter.

print("Welcome to my first official letter counting App!!")

name = input("What is your name : ")
print("\n")
print("Hello  " + name.title() + " Wassup Homies")
print("\n")

print("This app will count any letter present in your sentence...")

message = input("Write your message here: ")
print("\n")
letter_to_count = input("which letter do you want to count:  ")
counted = message.count(letter_to_count)

print("Hey ", name , "your message has", counted, letter_to_count,"'s on it")