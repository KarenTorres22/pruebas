def palindromos(s):
    return s[::-1] == s

def reverso(n):
    n=str(n)
    return int(n[::-1])

def es_primo(n):
    cont = 0
    for i in range(1,n):
        if n%i == 0:
            cont += 1
    if cont > 2:
        return False
    else:
        return True

def par(n):
    return n%2 == 0

def impar(n):
    return n%2 != 0 

def par1(n):
    return f"Y si armamos un baretooo??"