import csv
import re
from PyInquirer import prompt
"""
expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]
"""

spender = ""


def retrieve_users():
    res = []
    with open('users.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            res.append(row[0])
    return res

def retrieve_involved():
    res = []
    with open('users.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if row[0] != spender:
                res.append({"name":row[0]})
    return res

def isNumber(amount):
    try:
        float(amount)
    except:
        return False


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
        'validate': lambda amount: 'Amount must be a number' \
            if isNumber(amount) == False else True
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": retrieve_users()
    },
    {
        "type":"checkbox",
        "message":"Select people who are involved in the expense: ",
        "name":"involved-users",
        "choices": retrieve_involved()
    }
]



def new_expense(*args):
    retrieve_users()
    infos = prompt(expense_questions)
    isName = False
    with open('expense_report.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if row == ['amount,label,spender,involved-people']:
                isName = True
    with open('expense_report.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if not isName:
            spamwriter.writerow(["amount", "label", "spender","involved-people"])
        spamwriter.writerow([infos["amount"], infos["label"], infos["spender"], infos["involved-users"]])
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True


