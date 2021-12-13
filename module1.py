





























def arithmetic(a:float,b:float,c:str):
    """Saab teha +,-,*,/ ja tagastab arv, kui
    vaastus on arv ja "Tundmatu tehe" kui ei
    saa vastust leida.
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetilise tehe
    :rtype:var
    """
    if c=="/":
        if b==0:
            c="Tundmatu tehe"
        else:
            c=a/b
    elif c=="*":
        vaastus=a*c
    elif c=="-":
        vaastus=a-c
    elif c=="+":
        vaastus=a+c
    else:
        vaastus=("Invalid operation")

















#def Pindala(külg1:float,külg2:float)->float:
#    """Riistküliku pindala leidmine 
#    :param float külg1:Riistküliku esimene
#        külg
#    :param float külg2:Riistküliku teine külg
#    :rtype:float
#    """
#    S=külg1*külg2
#    return S
