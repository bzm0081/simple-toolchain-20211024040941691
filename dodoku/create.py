import random
def _create(parms):
    grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0] 
    string2 =  '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'
    length = len(string2)
    y=random.randint(0,length-1)
    integrity=string2[y:y+8]
    result = {'grid': grid , 'status' :'ok','integrity':integrity}
    return result  
    if parms['level'] == '2':
        grid = [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,-8,0,-4,0,0,-1,0,0,0,0,-9,0,0,0,0,0,0,0,0,0,0,0,-7,0,-5,-8,0,0,0,-2,0,0,0,-6,-1,0]
        string2 =  '6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a'
        length = len(string2)
        y=random.randint(0,length-1)
        integrity=string2[y:y+8]
        result = {'grid': grid , 'status' :'ok','integrity':integrity}
        return result   
    elif parms['level'] == '1':
        grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0] 
        string2 =  '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'
        length = len(string2)
        y=random.randint(0,length-1)
        integrity=string2[y:y+8]
        result = {'grid': grid , 'status' :'ok','integrity':integrity}
        return result
    elif parms['level'] == '3':
        
        grid = [0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,0,0,-6,0,-4,0,0,0,0,0,0,0,-5,0,0,0,0,0,-9,-8,-2,0,0,0,-4,-3,0,0,-7,0,0,0,0,0,0]
        string2 =  'eb572835ffe2015c731057f94d46fa77430ad6fd332abb0d7dd39d5f2ccadea9'
        length = len(string2)
        y=random.randint(0,length-1)
        integrity=string2[y:y+8]
        result = {'grid': grid , 'status' :'ok','integrity':integrity}
        return result
    elif parms :
        grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0] 
        string2 =  '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'
        length = len(string2)
        y=random.randint(0,length-1)
        integrity=string2[y:y+8]
        result = {'grid': grid , 'status' :'ok','integrity':integrity}
        return result   
    else:
        return{'status':'error:'}
        
