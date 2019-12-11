person ={'name':'','id':0}
team =[]
print(id(team))  #address
for i in range(3):
    x = person  #do not create a new object,use the same object of globe
    x['id'] =i
    team.append(x)

team[0]['name'] = 'jack'
team[1]['name'] = 'pony'
team[2]['name'] = 'Crossin'
print(team[0])#variable person outside the for loop,person in team is the same one
print(team[1])
print(team[2])
print(id(team))#value in list team change,but address not change
team =[]#use [] declare a list will creat a new list object
print(id(team))
for i in range(3):
    person ={'name':'','id':0}
    x = person
    x['id'] =i
    team.append(x)

team[0]['name'] = 'jack'
team[1]['name'] = 'pony'
team[2]['name'] = 'Crossin'
print(team[0])#variable person inside the for loop,different person append to team
print(team[1])
print(team[2])

testList =[1,2,3]
print(id(testList))
testList = [2,3,4]
print(id(testList))
testList =[5]
print(id(testList))
testList = []
print(id(testList))
testList =[1,2,3]
print(id(testList))
testList =[1,2,3]
print(id(testList))
testList = [2,3,4]
print(id(testList))
testList =[5]
print(id(testList))
testList = []
print(id(testList))
testList =[1,2,3]
print(id(testList))
print('-------')
testList1 = [1,2,3]#logic here is,every time declare a variable use different address to the last declare than
print(id(testList1))#if value is the same as variable in 'pool'(declared before) use the address in the pool
testList1 = [1,2,3]#the line before this line use the address of line 31,the address is different of line 50,even they have the same value
print(id(testList1))#and why line 54 use a new address,not use address of line 49?
testList1 = [1,2,3]
print(id(testList1))
testList1 = [1,2,3]
print(id(testList1))
testList1 = [1,2,3]
print(id(testList1))
testList1 = [1,2,3]
print(id(testList1))
print('-------')
t1 =[5,5,5]
print(id(t1))
t2 =[5,5,5]
print(id(t2))
t3 =[5,5,5]
print(id(t3))
t4 =[5,5,5]
print(id(t4))
print('-------')
tt1 =[1,2,3]
print(id(tt1))
tt2 =[1,2,3]
print(id(tt2))
tt3 =[1,2,3]
print(id(tt3))
tt4 =[1,2,3]
print(id(tt4))
print('-------')
ttt1 =20
print(id(ttt1))
ttt2 =20
print(id(ttt2))
ttt3 =20
print(id(ttt3))
ttt4 = 20
print(id(ttt4))
print('-------')
tttt1 =20
print(id(ttt1))
ttt1 =20
print(id(ttt1))
ttt1 =20
print(id(ttt1))
ttt1 = 20
print(id(ttt1))
print('-------')
tttt2 =20
print(id(ttt2))
ttt2 =30
print(id(ttt2))
ttt2 =40
print(id(ttt2))
ttt2 = 20
print(id(ttt2))