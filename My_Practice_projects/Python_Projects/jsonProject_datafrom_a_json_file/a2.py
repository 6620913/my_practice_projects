import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''
	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records



def filter_by_first_name(records, first_name):
    '''
    Description: Searches the records to find all persons with the given first name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - first_name (STRING): The first name

    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given first name
	    Case 1: No person found => Returns an empty list
	    Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''

    id_list = []
    name=first_name
    search=name.lower()
    for i in records:
        if i['first_name'].lower()==search:
            id_list.append(i['id'])
    return id_list
def filter_by_last_name(records,last_name):
    '''
    Description: Searches the records to find all persons with the given last name (case-insensitive)

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - last_name (STRING): The last name


    Returns:
    - A list of INTEGERS denoting the IDs of the persons with the given last name
    	Case 1: No person found => Returns an empty list
    	Case 2: At least one person found => Returns a list containing the IDs of all the persons found
    '''
    id_list = []
    name=last_name
    search=name.lower()
    for i in records:
        if i['last_name'].lower()==search:
            id_list.append(i['id'])
    return id_list

def filter_by_full_name(records, full_name):
    '''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
    name = full_name.split()

    first_name=name[0].lower()
    last_name=name[1].lower()
    id_list = []
    for i in records:
        if i['last_name'].lower()==last_name and i['first_name'].lower()==first_name:
            id_list.append(i['id'])
    return id_list

def filter_by_age_range(records, min_age, max_age):
    '''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
    id_list=[]
    for i in records:
        if min_age<=i['age']<=max_age:
            id_list.append(i['id'])
    
    return id_list

def count_by_gender(records):
    '''
    Description: Counts the number of males and females

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)

    Returns:
    - A dictionary with the following two key-value pairs:
    	KEY        VALUE
    	"male"     No of males (INTEGER)
    	"female"   No of females (INTEGER)
    '''

    gender_count={}
    female_count=0
    male_count=0
    
    for i in records:
        if i['gender']=='male':
            male_count=male_count+1
        if i['gender']=='female':
            female_count=female_count+1

    gender_count["male"]=male_count
    gender_count["female"]=female_count
    return gender_count

def filter_by_address(records, address):
    '''
    Description: Filters the person records whose address matches the given address. 

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
    	Some examples are:
			Case 1: {} 
    			=> All records match this case
			
    		Case 2: { "block": "AD", "city": "Delhi" } 
    			=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
			
    		Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

    Returns:
    - A LIST of DICTIONARIES with the following two key-value pairs:
    	KEY            VALUE
    	"first_name"   first name (STRING)
    	"last_name"    last name (STRING)
    '''

    list=[]
    for i in records:
        add={}
        j= i["address"]
        house_no=j['house_no']
        add["house_no"]=house_no
        add["block"]=j["block"].lower()
        add["city"]=j["city"].lower()
        add["town"]=j["town"].lower()
        add["state"]=j["state"].lower()
        add["pincode"]=j["pincode"]

        if 'block' in address:
            address["block"]=address["block"].lower()
        if 'city' in address:
            address["city"]=address["city"].lower()
        if 'town' in address:
            address["town"]=address["town"].lower()
        if 'state' in address:
            address["state"]=address["state"].lower()
        if address.items()<=add.items():
            id_dic={}
            id_dic['first_name']=i['first_name']
            id_dic['last_name']=i['last_name']
            list.append(id_dic)
    return list

def find_alumni(records, institute_name):
    '''
    Description: Find all the alumni of the given institute name (case-insensitive). 
	
    Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - institute_name (STRING): Name of the institute (case-insensitive) 

    Returns:
    - A LIST of DICTIONARIES with the following three key-value pairs:
    	KEY            VALUE
    	"first_name"   first name (STRING)
    	"last_name"    last name (STRING)
    	"percentage"   percentage (FLOAT)
    '''
    list=[]
    for i in records:
        for j in i['education']:
            if j['ongoing']==False:
                if j['institute']==institute_name:
                    id_dic={}
                    id_dic['first_name']=i['first_name']
                    id_dic['last_name']=i['last_name']
                    id_dic['percentage']=j['percentage']
                    list.append(id_dic)
    return list

def find_topper_of_each_institute(records):
    '''
    Description: Find topper of each institute

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)

    Returns:
    - A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

    Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	'''
    toper={}
    institutes=[]
    for i in records:
        for j in i['education']:
            if j['institute'] in institutes:
                pass     
            else:
                institutes.append(j['institute'])

    for i in institutes:
        percentage=0
        for j in records:
            for k in j['education']:
                if k['institute']==i:
                    if k['ongoing']==False:
                        if k['percentage']>percentage:
                            toper[i]=j['id']
                            percentage=k['percentage']
    return toper


def find_blood_donors(records, receiver_person_id):
    '''
    Description: Find all donors who can donate blood to the person with the given receiver ID.

    	Note: 
    	- Possible blood groups are "A", "B", "AB" and "O".

    	Rules:
    	BLOOD GROUP      CAN DONATE TO
    	A                A, AB
    	B                B, AB
    	AB               AB
    	O                A, B, AB, O

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - receiver_person_id (INTEGER): The ID of the donee
    	Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

    Returns:
    - A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
    '''
    donar={}
    for i in records:
        if i['id']==receiver_person_id:
            reciver=i['blood_group']
        
    for i in records:
        if reciver=='A':
            if i['blood_group']=='A' and i['id']!=receiver_person_id:
                donar[i['id']]=i['contacts']
            if i['blood_group']=='O' and i['id']!=receiver_person_id:
                donar[i['id']]=i['contacts']
        if reciver=='AB':
            if i['blood_group']=='A' and i['id']!=receiver_person_id:
                donar[i['id']]=i['contacts']
            if i['blood_group']=='O' and i['id']!=receiver_person_id:
                donar[i['id']]=i['contacts']
            if i['blood_group']=='B' and i['id']!=receiver_person_id:
                donar[i['id']]=i['contacts']
            if i['blood_group']=='AB' and i['id']!=receiver_person_id:
                donar[i['id']]=i['contacts']
        if reciver=='B':
            if i['blood_group']=='B' and i['id']!=receiver_person_id:
                donar[i['id']]=i['contacts']
            if i['blood_group']=='O' and i['id']!=receiver_person_id:
                donar[i['id']]=i['contacts']
        if reciver=='O':
            if i['blood_group']=='O' and i['id']!=receiver_person_id:
                donar[i['id']]=i['contacts']
    return donar

def get_common_friends(records, list_of_ids):
    '''
    Description: Find the common friends of all the people with the given IDs

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

    Returns:
    - A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
    '''
    b=()
    for i in records:
        for j in list_of_ids:
            if j==i['id']:
                a=set(i['friend_ids'])
                if b==():
                    b=a
                else:
                    b=a&b
    id_list=list(b)

    return id_list

def is_related(records, person_id_1, person_id_2):
    '''
    **** BONUS QUESTION ****
    Description: Check if 2 persons are friends

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id_1 (INTEGER): first person ID
    - person_id_2 (INTEGER): second person ID

    Returns:
    - A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
    '''
    for i in records:
        if i['id']==person_id_1:
            if i['friend_ids']==[]:
                r=False
                return r
            if person_id_2 in i['friend_ids']:
                r=True
                return r
    return True


def delete_by_id(records, person_id):
    '''
    Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
	
    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    ''' 
    for i in records:
        if i['id']==person_id:
            records.remove(i)
        if person_id in i['friend_ids']:
            i['friend_ids'].remove(person_id)
    
    return records

def add_friend(records, person_id, friend_id):
    '''
    Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.  

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - friend_id (INTEGER): The friend id
	
    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    for i in records:

        if i['id']==person_id:
            if friend_id in i['friend_ids']:
                pass
            else:
                i['friend_ids'].append(friend_id)
        if i['id']==friend_id:
            if person_id in i['friend_ids']:
                pass
            else:
                i['friend_ids'].append(person_id)

    return records

def remove_friend(records, person_id, friend_id):
    '''
    Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - friend_id (INTEGER): The friend id
	
    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    for i in records:
        if i['id']==person_id:
            if friend_id in i['friend_ids']:
                i['friend_ids'].remove(friend_id)
        if i['id']==friend_id:
            if person_id in i['friend_ids']:
                i['friend_ids'].remove(person_id)

    return records

def add_education(records, person_id, institute_name, ongoing, percentage):
    '''
    Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

    Parameters:
    - records (LIST): A list of person records (each of which is a dictionary)
    - person_id (INTEGER): The person id
    - institute_name (STRING): The institute name (case-insensitive)
    - ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
    - percentage (FLOAT): The person's score in percentage

    Returns:
    - A LIST of Dictionaries representing all the records (the updated version).
    In case there were no updates, return the original records.
    '''
    for i in records:
        if i['id']==person_id:
            edu={}
            edu['institute']=institute_name
            edu['ongoing']=ongoing
            if ongoing==False:
                edu['percentage']=percentage
            i['education'].append(edu)
    return records