# Name - 
# Roll No - 

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''
# Write the code here for creating an interactive program.

import a2
a=a2.read_data_from_file('data.json')
c=0
while(True):
    print('_'*70)
    print('_'*70)
    if c==0:
        print('                              Wlcome')
        print('_'*70)
        print('_'*70)
        print('Hello! Which task you want to perform?')
        c=c+1
    else:
        print("entere -1 to end or continue further tasks")
    print('Following are the available tasks...\n\n')	
    print()
    print("1. read data from file \n2. filter by first name\n3. filter by last name\n4. filter by full name\n5. filter by age range\n6. count by gender\n7. filter by address\n8. find alumni\n9. find topper of each institute\n10. find blood donors\n11. get common friends\n12. is related\n13. delete by id\n14. add friend\n15. remove friend")
    print('')
    code=int(input("Enter the code of task you want to perform or -1 to end:")) 
    if code==1:
        print('_'*70)
        print('_'*70)
        print('Do you again want to read Data from your file? \nit delete all changes you performed before')
        print('Entere 0 if you want to live or enter 1 to proceed')
        respo=int(input("Responce:"))
        if respo==1:
            a=a2.read_data_from_file('data.json')
            print("Task compleated..\n")
        if respo==0:
            print('end task by the user\n')
        input("Enter to continue:")
    if code==2:
        print('_'*70)
        print('_'*70)
        print("Enter the First name you want to search ")
        name=input()
        ids=a2.filter_by_first_name(a,name)
        if ids==[]:
            print("No one found with the given first name")
        else:
            print("following are the Id's of persons with provided first name")
            print(ids)
        input("Enter to continue:")
    if code==3:
        print('_'*70)
        print('_'*70)
        print("Enter the Last name you want to search ")
        name=input()
        ids=a2.filter_by_first_name(a,name)
        if ids==[]:
            print("no one with the given last name")
        else:
            print("following are the Id's of persons with provided last name")
            print(ids)
        input("Enter to continue:")
    if code==4:
        print('_'*70)
        print('_'*70)
        print("Enter the Full name you want to search ")
        name=input()
        ids=a2.filter_by_first_name(a,name)
        if ids==[]:
            print("no one with the given Full name")
        else:
            print("following are the Id's of persons with provided Full name")
            print(ids)
        input("Enter to continue:")
    if code==5:
        print('_'*70)
        print('_'*70)
        print("Enter the  age limits you want to search ")
        min_age=int(input("Enter min age:"))
        max_age=int(input("Enter max age:"))
        ids=a2.filter_by_age_range(a, min_age, max_age)
        if ids==[]:
            print("no one with the given Age limit")
        else:
            print("following are the Id's of persons with provided age limit")
            print(ids)
        input("Enter to continue:")
    if code==6:
        print('_'*70)
        print('_'*70)
        print("Result")
        count=a2.count_by_gender(a)
        print(count)
        input("Enter to continue:")
    if code==7:
        print('_'*70)
        print('_'*70)
        address={}

        print('Enter the address you want to search')
        print("leave Blanck if you dont wanna enter any field")
        house_no=input('house no:')
        block=input("Enter block: ")
        town=input("Enter town name:")
        city=input("Enter city name:")
        state=input("Enter state:")
        pincode=input("Enter pincode:")
        if house_no!='':
           address["house_no"]=int(house_no)
        if block!='':
            address["block"]=block
        if city!='':
            address["city"]=city
        if town!='':
            address["town"]=town
        if state!='':   
            address["state"]=state
        if pincode!='':
            address["pincode"]=int(pincode)
        result=a2.filter_by_address(a,address)
        print("your result")
        print(result)
        input("Enter to continue:")
    if code ==8:
        print('_'*70)
        print('_'*70)
        institute=input('Enter the institute name whosse aluminies you want :')
        result=a2.find_alumni(a, institute)
        print('')
        if result==[]:
            print("No one found")
        else:
            print("your result")
            print(result)
        input("Enter to continue:")
    if code==9:
        print('_'*70)
        print('_'*70)
        print('topers of institutes  \n')
        result=a2.find_topper_of_each_institute(a)
        print(result)
        input("Enter to continue:")
    if code==10:
        print('_'*70)
        print('_'*70)
        id=int(input("Entere receiver id : "))
        donar=find_blood_donors(a,id)
        print('Donars are')
        print(donar)
        input("Enter to continue:")
    if code==11:
        print('_'*70)
        print('_'*70)
        x = list(map(int, input("Enter the id's of persons (space-separated): ").split()))
        ids=a2.get_common_friends(a,x)
        if ids==[]:
            print('No comman friend found ')
        else:
            print('below is the list of comman friends found')
            print(ids)
        input("Enter to continue:")
    if code==12:
        print('_'*70)
        print('_'*70)
        print('Enter the ids of friend whose about whome you find that they are friend of each other ,directly or indirectly or not')
        person_id_1=int(input("first person id:"))
        person_id_2=int(input("secound person id:"))
        result12=a2.is_related(a, person_id_1, person_id_2)
        if result12:
            print('the persons are friends of each other, directly or indirectly')
        else:
            print('the persons are Not friends of each other, directly or indirectly')
        input("Enter to continue:")
    if code==13:
        print('_'*70)
        print('_'*70)
        id=int(input("Enter person id you want to delete:"))
        a=a2.delete_by_id(a,id)
        print("the given id %d is deleted",id)
        input("Enter to continue:")
    if code==14:
        print('_'*70)
        print('_'*70)
        print("Entere the id's of persons which are now friends")
        id1=int(input("enter id of first person:"))
        id2=int(input('Entere id of secound person:'))
        a=a2.add_friend(a, id1,id2)
        print("Task completed..")
        input("Enter to continue:")
    if code==15:
        print('_'*70)
        print('_'*70)
        print("Entere the id's of persons which are now not friends")
        id1=int(input("Entere id of first person:"))
        id2=int(input('Entere id of secound person:'))
        a=a2.remove_friend(a, id1,id2)
        print("Task completed..")
        input("Enter to continue:")
    if code==16:
        print('_'*70)
        print('_'*70)
        print("Entere the education details")
        person_id=int(input('Enter the person id'))
        institue_name=input('Enere institute name:')
        ong=input("Enter y if student is going to the institute and if Passed the institute enter n")
        if ong=='y':
            ongoing=True
        if ong=='n':
            ongoing=False
        if ongoing!='':
            edu["ongoing"]=ongoing
        if ongoing==False:
            percentage=Float(input("Enter perentage of student:"))
        a=a2.add_education(a, person_id, institute_name, ongoing, percentage)
        input("Enter to continue:")
    if code==-1:
        break