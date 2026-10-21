#sets 
skills = {"Python", "Java", "C++", "JavaScript"}
print("Skills:", skills)
required_skills = {"Python", "Java", "C++"}

#common skills between skills and required_skills
common_skills = skills & required_skills
print("Common skills:", common_skills)

#forzen sets
forzen = frozenset({"Python", "Java", "C++", "JavaScript"})
print("Frozen set:", forzen)

#use all operations in sets
#union
union_skills = skills | required_skills
print("Union of skills and required_skills:", union_skills) 

#intersection
intersection_skills = skills & required_skills
print("Intersection of skills and required_skills:", intersection_skills)   

#difference
difference_skills = skills - required_skills
print("Difference of skills and required_skills:", difference_skills)   

#symmetric difference
symmetric_difference_skills = skills ^ required_skills
print("Symmetric difference of skills and required_skills:", symmetric_difference_skills)   

#subset
is_subset = required_skills <= skills   
print("Is required_skills a subset of skills?:", is_subset)

#superset
is_superset = skills >= required_skills
print("Is skills a superset of required_skills?:", is_superset)

#disjoint
is_disjoint = skills.isdisjoint(required_skills)
print("Are skills and required_skills disjoint?:", is_disjoint) 

#clear
skills.clear()
print("Skills after clearing:", skills)

#copy
skills_copy = skills.copy()
print("Copy of skills:", skills_copy)

#update
skills.update({"HTML","CSS","COBAL","SQL"})
print("Skills after update:", skills)

#remove
skills.remove("CSS")
print("Skills after removing CSS:", skills)  

#discard
skills.discard("SQL")
print("Skills after discarding SQL:", skills)

#pop
popped_skill = skills.pop()
print("Popped skill:", popped_skill)

#len
skills_length = len(skills)
print("Length of skills:", skills_length)   


#use frozenset operations to set loop functionality
frozen_set1 = frozenset({"Python", "Java", "C++"})
frozen_set2 = frozenset({"Python", "JavaScript", "C#"})
forzen_set3 = frozenset({"Python", "Java", "C++", "JavaScript"})
#for loop to iterate through the frozen sets
for skill in frozen_set1:
    print("Skill in frozen_set1:", skill)
for skill in frozen_set2:
    print("Skill in frozen_set2:", skill)
for skill in forzen_set3:
    print("Skill in forzen_set3:", skill)   






