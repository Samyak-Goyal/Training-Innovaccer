#List=[]

##1   
#mylist =['item1','item2','item5']
#li2=['item3','item4']
#li3=li2+mylist   #add two lists
#li3+=['item6']   #add an item to the list
#li3.append('item8') #same as above
#li3.remove('item3') #remove an element
#li3.pop() #remove the last element from the list 
#li3.pop(1) #remove the element at index 1
#li3.pop(0) #remove the element at index 0
#print(len(li3))  #print number of elements in the list


#li3.sort()      #sort in ascending order
#li3.sort(reverse=True)      #sort in descending order

#print(li3)



##2
#course1=["Sql Server","Azure","OpenStack","Python Programming","AWS","Java","Linux"] 
#coursename=input("Enter course name to search: ").strip().upper()
#course3=[]
#for x in course1:
#    course3.append(x.upper())

#if(coursename in course3):
#    print(f"{coursename} is available")
#else:
#    print(f"{coursename} is not available")


##3
#pricelist=[450,600,550,1200,709]

#print(max(pricelist))                       #max
#print(min(pricelist))                       #min
#print(sum(pricelist))                       #sum
#print(sum(pricelist)/len(pricelist))        #average
#print(round(sum(pricelist)/len(pricelist))) #round off



##4
#feedbackmail=['akanksha.gupta@sify.com','Deepak.sharma@sify.com','karan.Bhatia@sify.com','sarah.baswa@sify.com','raveesh.bhatt@sify.com','sheetal@Hotmail.com','jatin.sai@saidata.com','andy.maggy@colt.net','prashun.das@sify.com']
#lowerlist=[]
#for x in feedbackmail:
#    lowerlist.append(x.lower())

#sifyid=[]
#notsifyid=[]

#for x in lowerlist:
#    if(x.endswith('@sify.com')):
#        sifyid.append(x)
#    else:
#        notsifyid.append(x)

#print("Sify: ",sifyid)

#print("NotSify: ",notsifyid)

#li1=[]

#for x in lowerlist:
#    if(x.startswith('p') or x.startswith('s')):
#        li1.append(x)

#print("Starting with p or s: ",li1) 

#while(True):
#    fin=input("Enter the id to be searched: ").strip().lower() 

#    if( fin in lowerlist):
#        print(f"{fin} is present in list")
#    else:
#        print(f"{fin} is not present in list")
#    con=input("Check another?y/n: ").strip().lower()

#    if(con=='n'):
#        break

#print("Program Finished!")


#Tuples=() are Immutable
##5
#deptlist=("Purchase",'HR',"FSO","L&D","NIS","Sales")
#print(deptlist)
#newdept=list(deptlist)
#newdept.append("Software Division")
#newdept.sort()
#deptlist=tuple(newdept)
#for x in deptlist:
#    print(x)
#print(len(deptlist))


##6
#stations=('New Delhi','Agra','Kanpur','Aligarh','Mughalsarai','Kanpur' ,'Allahabad') 
#newl=list(stations)
#newl.remove('Mughalsarai')
#newl.remove('Allahabad')
#newl.append("Deen Dayal Upadhaya")
#newl.append("Prayagraj")
#stations=tuple(newl)
#print(stations)


##7
#Maxtemp=(38.7,32.6,40.2,38.3,38.7,39.4,39.8)
#l1=list(Maxtemp)
#print(max(l1))
#print(sum(l1)/len(l1))


##Set={} 
##8
#myset={"Anushka","Rajat","Hitesh","Imran","Jatin","Rajinder","Neelam"} 
#projectset={"Rajat","Imran","Jatin","Rajinder","Anushka","Neelam","Hitesh"} 
#print(myset==projectset) 
# 1. Order of the Elements does not matter in a Set 
# 2. A Set can't contain any Duplicate Values 

#course1=["Sql Server","Ansible","Linux","OpenStack"] 
#course2=["Ansible","Java","AWS","Kubernetes","Linux"] 
#course3=course1+course2 
#overallcourset=set(course3) 
#print(overallcourset) 



##9
#set1=set()
#while True:
#    countryname=input("enter the location: ").strip().title()
#    set1.add(countryname)
#    con=input("Continue?y/n: ").strip().lower()
#    if(con=='y'):
#        continue
#    else:
#        break
#print("the locations are: ")
#for x in set1:
#    print(x)    
#we can also use set1.remove("Usa") to remove from the set

##10
# Other Operations on Set 
# pricorus={"Sales","IT","CSO","FSO","LDM"} 
# symphony={"Sales","CSO","Purchase","HR","Admin"} 

# #symmphony has procured pricorous 
# newdepts=pricorus - symphony # Finding the Difference 
# print("New Depts To Be Formed") 
# print(newdepts) 
# print("Total New Depts = %d " %(len(newdepts))) 
# cdept=pricorus & symphony # & stands for intersection 
# print("Common Depts To Be Formed") 
# print(cdept) 
# print("Total Common Depts = %d "%(len(cdept))) 
# alldepts=symphony | pricorus # | means Union 
# print("Overall Depts Are") 
# print(alldepts) 
# print("Total Depts=%d" %len(alldepts)) 


# #11
# projectset={"P001":("Appraisal Process","Hyderabad",25,"22-Feb-22"), 
# "P022":("HR Recruitment","Kolkata",16,"22-Feb-22"), 
# "P090":("SAP Updation","Bengaluru",16,"23-Feb-22"), 
# "P023":("HR Recruitment","Mumbai"), 
# "P009":("Tax Updation","Kolkata",20)} 

# print(projectset)
# print(len(projectset))
# lastyearproject={"P093":("anything")}
# projectset.update(lastyearproject)  #to add two dictionary
# print(projectset.keys())
# print("********************")
# print(projectset.values())
# print("********************")
# print(projectset.items())
# print(projectset)
#print(projectset.get('P001')) 



# #12
# Location={'Bhopal','Chandigarh','Bhuvaneswar','Chennai','Vizag','Surat'} 
# done={'Bhopal','Chennai','Vizag'}

# notdone=Location-done
# print(notdone)



# #13
# dict1={"P001":("Appraisal Process","Hyderabad",25,"22-Feb-22"), 
# "P022":("HR Recruitment","Kolkata",16,"22-Feb-22"), 
# "P090":("SAP Updation","Bengaluru",16,"23-Feb-22"), 
# "P023":("HR Recruitment","Mumbai"), 
# "P009":("Tax Updation","Kolkata",20)} 
# dict2={'P025':'dwd'}
# dict1.update(dict2)
# print(sorted(dict1))        #sorting a dict in asc
# print(sorted(dict1, reverse=True)) #sorting in desc



#14
feedbackmail=['akanksha.gupta@sify.com','Deepak.sharma@sify.com','karan.Bhatia@sify.com','sarah.baswa@sify.com','raveesh.bhatt@sify.com','sheetal@Hotmail.com','jatin.sai@saidata.com','andy.maggy@colt.net','prashun.das@sify.com']
lambda1= lambda s : s.endswith("@sify.com")
lambda2= lambda s : not s.endswith("@sify.com")

sifylist=filter(lambda1,feedbackmail)  #filter is used when some condition is involved

nonsifylist=filter(lambda2,feedbackmail)

print(tuple(sifylist))

print(tuple(nonsifylist))









