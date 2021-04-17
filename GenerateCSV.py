#!/usr/bin/python

# Import of the libraries
import csv
import random
from faker import Faker 
fake = Faker() 

# def - is a function
def createCsvLine(arr):
  # print(arr)
  return '"'  + '","'.join(arr) + '"\n'

#number of the inserts
records=10
#print("Making %d records\n" % records)

# names of the columns
fieldnames=['id','name','mail','city']

#open file, w - is for write
writer = open("peopleCheckFaker.csv", "w")

# base of names and cities
names=['Deepak', 'Sangeeta', 'Geetika', 'Anubhav', 'Sahil', 'Akshay']
cities=['Delhi', 'Kolkata', 'Chennai', 'Mumbai']
states=['Delhi', 'Kolkata', 'Chennai', 'Mumbai']

# column names write in file
writer.write(createCsvLine(fieldnames))

# loop must start empty value
item = []
for i in range(0, records):
  # str(i) - id to string
  # random.choice(names) - random choice from names
  # str is for string
  #
  item = [str(i),random.choice(names),fake.email(), random.choice(cities),  random.choice(states)]
  # push item to the file
  writer.write(createCsvLine(item))

writer.close()


