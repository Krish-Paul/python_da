set1={1,3,5,7}
set2={2,4,5,1,6}

set1.add(9)

set1.remove(10)

set1.discard(10)

set1.union(set2)

set1.intersection(set2)

set1.difference(set2)

set1.update(set2)

set1.symmetric_difference(set2)

set1.isdisjoint(set2)

set1.issubset(set2)

{2,4}.issubset(set2)

list1=[1,2,3,4,2,3,1]
set(list1)



#dict
dic1={"name":"raj","age":20,"gender":"male"}
dic1


dic1.keys()

dic1.values()

dic1["name"]

dic1["place"]="india"
dic1

del dic1["age"]
dic1

len(dic1) 

"name"in dic1#only check keys. give false for values

"raj"in dic1

dic1.items()

dic1.update({"place": "india", "profession": "student"})
print(dic1)

dic1.pop("gender")
print(dic1)  # Output: {'name': 'raj', 'age': 20, 'place': 'india', 'profession': 'student'}

dic1.clear()
print(dic1)  # Output: {}



dic2={"name":["ram","ran","ras"],
      "age":[14,12,13],
      "city":["pune","mumbai","bangalore"]}
dic2




dic1 = {"name": "raj", "age": 20}
dic2 = {"gender": "male", "place": "india"}
merged_dic = {**dic1, **dic2}
print(merged_dic)  # Output: {'name': 'raj', 'age': 20, 'gender': 'male', 'place': 'india'}


dic1 = {"name": "raj", "age": 20, "gender": "male"}
for key, value in dic1.items():
    print(f"{key}: {value}")


dic1 = {"name": "raj", "age": 20, "gender": "male"}
sorted_dic1 = dict(sorted(dic1.items()))
print(sorted_dic1)  # Output: {'age': 20, 'gender': 'male', 'name': 'raj'}
