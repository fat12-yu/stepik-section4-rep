import random

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.ru", "yahoo.com"]
letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]

def get_one_random_domain(domains):
        return domains[random.randint( 0, len(domains)-1)]


def get_one_random_name(letters):
    email_name = ""
    for i in range(7):
        email_name += letters[random.randint(0, len(letters)-1)]
    return email_name


def generate_random_email():
    for i in range(10):
         one_name = str(get_one_random_name(letters))
         one_domain = str(get_one_random_domain(domains))
         return f"{one_name}@{one_domain}"

def generate_random_password():
    newpass = ''
    for i in range(9):
        newpass += letters[random.randint(0, len(letters)-1)]
    return newpass


def main():
    print(generate_random_email())
    print(generate_random_password())

if __name__=='__main__':
    main()
