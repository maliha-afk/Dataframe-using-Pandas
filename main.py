import pandas as pa

data={
    "name":["atiya","ryan","zaheen","tahmid"],
    "class":[6,6,8,8],
    "age":[12,13,16,15]
}

myd=pa.DataFrame(data)

#print(myd)

#print(myd["name"])

#myd2=pa.DataFrame(data,index=["st1","st2","st3","st4",])
#print(myd2["name"])

myd["math mark"]=[97,98,90,95]
#print(myd)

#print(myd.sort_values("age"))

print(myd.info())