loginy = ["kon","kar","bar"]
hasla = ["123","456","789"]


def pobieranie_loginu():
    login = ""
    verify = None
    while login == "" or verify == False:
        if verify == False:
            print("Niepoprawny login")
        login=input("Podaj login:\n")
        verify = login in loginy
    return login



def logowanie(a,b):
    p = loginy.index(user)
    if haslo == hasla[p]:
        print("logowanie powiodło się")
        return True
    else:
        print("Logowanie nie powiodło się")
        return False


user = pobieranie_loginu()
haslo = input("Podaj hasło:")
logowanie(user,haslo)





     
