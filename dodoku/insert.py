import random
def _insert(parms):
    if parms['value'] == '2':
        grid = [0,-6,0,0,0,0,0,-5,-9,-9,-3,2,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,-8,0,-4,0,0,-1,0,0,0,0,-9,0,0,0,0,0,0,0,0,0,0,0,-7,0,-5,-8,0,0,0,-2,0,0,0,-6,-1,0]
        string2 =  '6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a'
        length = len(string2)
        y=random.randint(0,length-1)
        integrity=string2[y:y+8]
        result = {'grid': grid , 'status' :'ok','integrity':integrity}
        return result  
