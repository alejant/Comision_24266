def scope_test():
    def actualizar_local():
        variable = "ahora soy variable local "

    def actualizar_nonlocal():
        nonlocal variable
        variable = "ahora soy variable nonlocal"

    def actualizar_global():
        global variable
        variable = "ahora soy variable global"

    variable = "soy variable"
    actualizar_local()
    print("Despues de actualizar variable en método como local:", variable)
    actualizar_nonlocal()
    print("Despues de actualizar variable en método como nonlocal:", variable)
    actualizar_global()
    print("Despues de actualizar variable en método como global:", variable)

#variable = "variable"
scope_test()
print("En el scope global:", variable)