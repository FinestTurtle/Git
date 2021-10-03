import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth


cred = credentials.Certificate('./Sprint1/AccountServiceKey.json')
firebase_admin.initialize_app(cred)

data = firestore.client()
choice = None

doc_ref = data.collection(u'employees')


def new_user(new_email, new_password):
    user = auth.create_user(
        email=new_email,
        password=new_password,
        )
    print('Sucessfully created new user.')

def viewEmployeeList():
    #This function will gather the information from the database and view what is being held in that database.
    user_ref = data.collection(u'employees')
    #the stream function will allow all the data within the collection to be sent over.
    employee_docs = user_ref.stream()

    for doc in employee_docs:
        print(f'{doc.id} => {doc.to_dict()}')

def addEmployee():
    name = input('Employee name: ')
    job = input('Job position: ')
    doc_ref = data.collection(u'employees').document(name)
    #set will allow us to set that information in that document.
    doc_ref.set({
        u'name':name,
        u'job':job
    })

def updateEmployee():
    name = input('Employee name: ')
    update_job = input('New job: ')
    doc_ref = data.collection(u'employees').document(name)
    doc_ref.update({
        u'job':update_job
    })

def removeEmployee():  
    name = input('Employee name to remove: ')
    data.collection(u'employees').document(name).delete()


# answer = input('Do you have an existing email?(Y/N) ')
# if answer == 'N':
#     email = input('Please enter email: ')
#     password = input('Please enter password: ')
#     new_user(email, password)
# else:
#     email = input('Please enter existing email: ')
#     password = input('Please enter your password: ')
#     user = auth.get_user_by_email(email)
#     if email == user:
#         print('error')
#     else:
while choice != '5':
    print('1) View employee list')
    print('2) Add employee')
    print('3) Update employee')
    print('4) Remove employee')
    print('5) Quit')
    choice = input('> ')
    if choice == '1':
        viewEmployeeList()
    elif choice == '2':
        addEmployee()
    elif choice == '3':
        updateEmployee()
    elif choice == '4':
        removeEmployee()


