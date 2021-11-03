from PyInquirer import prompt
import csv
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name"
    }

]

def add_user(*args):
    infos = prompt(user_questions)
    with open('users.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([infos["name"]])
    print("User Added !")
    # This function should create a new user, asking for its name
    return True