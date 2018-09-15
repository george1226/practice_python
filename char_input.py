#' Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#' Extras:
#' Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#' Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)#'

#' imports
import datetime

#' input name and age to be computed for years until 100 yrs old
name = input("who are you?")
age = input("how old are you?")

#' convert age as int, input functions returns string
age = int(age)

#' get current date to compute the yr 100yrs from now
now = datetime.datetime.now()
age = ((now.year + 100) - age)

#' print outputs for exercises
#' 1
msg = "hi, " + name + " you will be 100 at " + str(age)
print(msg)

#' extras 1
random_num = int(input("give me a number pls?"))
print("alright: " + str(msg * random_num))

#' extras 2
msg = "\n" + msg
print("alright with enter: " + str(msg*random_num))

#' treat this as sprintf %s
print("hi, {}. You're {} yrs. old".format(name.title(), age))
