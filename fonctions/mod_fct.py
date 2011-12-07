#=[site officiel]=====================
#<<<<<mod_fct by W3YZOH0RTH>>>>>
#=====[http://progject.free.fr/]=======

# fonctions
#	get_vars_function(fonction)
#		-> list
#	get_args_function(fonction)
#		-> list
#	get_vals_function(fonction)
#		-> tuple
#	get_valarg_function(fonction)
#		-> list
#	get_code_function(fonction)
#		-> string

def get_vars_function(fonction):
    if "im_func" not in dir(fonction): return fonction.func_code.co_varnames
    return fonction.im_func.func_code.co_varnames

#:::::::::::::::::::::::::::::::::::::::::::::::::
def get_args_function(fonction):
    return get_vars_function(fonction)[:fonction.func_code.co_argcount]

#:::::::::::::::::::::::::::::::::::::::::::::::::
def get_vals_function(fonction):
	args = get_args_function(fonction)[:fonction.func_code.co_argcount]
	if "im_func" not in dir(fonction): vals = list(fonction.func_defaults)
	else: vals = list(fonction.im_func.func_defaults)
	dif = len(args)-len(vals)
	return dif,  vals

#:::::::::::::::::::::::::::::::::::::::::::::::::
def get_valarg_function(fonction):
    args = get_args_function(fonction)[:fonction.func_code.co_argcount]
    if "im_func" not in dir(fonction): vals = list(fonction.func_defaults)
    else: vals = list(fonction.im_func.func_defaults)
    dif = len(args)-len(vals)
    liste = [(a, ) for a in args[:dif]]
    return liste + [(a, v) for a, v in zip(args[dif:], vals)]

#:::::::::::::::::::::::::::::::::::::::::::::::::
def get_code_function(fonction):
    if "im_func" in dir(fonction): fonction = fonction.im_func
    fichier = open(fonction.func_code.co_filename, "r")
    string = fichier.readline()
    code = ""
    save = actif = False
    indentation = 0

    while string:
        if "def " in string and fonction.func_name in string and not save:
            temp = string.split(fonction.func_name)
            temp[0] = temp[0].replace(" ", "").replace("\t", "")
            temp[1] = temp[1].split("(")[0]
            if temp[0] == "def" and not temp[1]:
                save = True
                indentation = string.index("d")
                code += string
                actif = False
        if save:
            if actif:
                if string[indentation] == " " or string[indentation] == "\t":
                    code += string
                else:
                    break
            else:
                actif = True
        string = fichier.readline()

    fichier.close()
    return code
