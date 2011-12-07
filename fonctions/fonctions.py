#=[site officiel]=====================
#<<<<<fonctions by W3YZOH0RTH>>>>>
#=====[http://progject.free.fr/]=======

#:::::::::::::::::::::::::::::::::::::::::::::::::
def RANGE(start=0,stop=0,step=1):
      if start != stop and step:
            if stop < start and step > 0:start, stop = stop, start
            elif stop > start and step < 0:start, stop = stop, start
            while start < stop:
                  start += step
                  yield start
      else:yield start

#:::::::::::::::::::::::::::::::::::::::::::::::::
def get_key(dico,x):
    for key in dico.keys():
        if dico[key] == x:
            return key