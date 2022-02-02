#question 1
irongate = ["townhome", "2-story single family", "3-story single family"]
print("There are", len(irongate), "types of homes in this community.")


#2nd question
irongate = ["townhome","2-story single family","3-story single family"]
irongate.append("condo")
print(irongate)

#3rd question
irongate = ["townhome","2-story single family","3-story single family"]
irongate.insert(1,"ranch home")
print(irongate)

#4th question
irongate = ["townhome","2-story single family","3-story single family"]
print(irongate.index("3-story single family"))

#5th question
irongate = ["townhome","2-story single family","3-story single family"]
print("farmhouse" in irongate)
print("farmhouse" not in irongate)

#6th question
irongate = ["townhome","2-story single family","3-story single family"]
irongate.append("farmhouse")
print(irongate)

#7th question
irongate = ["townhome","2-story single family","3-story single family"]
irongate.insert(2,"detached home")
print(irongate)

#10th question
irongate = ["townhome","2-story single family","3-story single family"]
irongate.sort()
print(irongate)

#8th question
irongate = ["townhome","2-story single family","3-story single family"]
#irongate2 = ["townhome"]
#irongate.extend(irongate2)
irongate.append("townhome")
print(irongate)

#9th question
irongate.remove("townhome")
print(irongate)

jordanranch = ["townhome", "2-story single family", "ranch home"]
fallonrd = irongate + jordanranch
print(fallonrd)

print(set(fallonrd))

#irongate = ["townhome", "2-story single family", "3-story single family"]


