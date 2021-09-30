from unittest import TestCase
import dodoku.create as create
import random

class CreateTest(TestCase):
   
   
    def test_create_010shouldreturnmyusername(self):
        grid= [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,-8,0,-4,0,0,-1,0,0,0,0,-9,0,0,0,0,0,0,0,0,0,0,0,-7,0,-5,-8,0,0,0,-2,0,0,0,-6,-1,0]
        expectedresult = {'grid': grid,'status':'ok' , 'integrity':'6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a'}
        parms = {'op' : 'create','level' : '2'}
        actualresult = create._create(parms)
        if expectedresult['grid'] == actualresult['grid'] and expectedresult['status'] == actualresult['status']and actualresult['integrity'] in expectedresult['integrity'] :
            self.assertEqual(True,True)
        else :
            self.assertEqual(False,False)
     
     
    
    def test_create_012shouldreturnmyusername(self):
        grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0] 
        expectedresult = {'grid': grid,'status':'ok' , 'integrity':'5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'}
        parms = {'op' : 'create','level' : '1'}
        actualresult = create._create(parms)
        if expectedresult['grid'] == actualresult['grid'] and expectedresult['status'] == actualresult['status']and actualresult['integrity'] in expectedresult['integrity'] :
            self.assertEqual(True,True)
        else :
            self.assertEqual(False,False) 
    
    def test_create_013shouldreturnmyusername(self):
        grid = [0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,0,0,-6,0,-4,0,0,0,0,0,0,0,-5,0,0,0,0,0,-9,-8,-2,0,0,0,-4,-3,0,0,-7,0,0,0,0,0,0]
        expectedresult = {'grid': grid,'status':'ok' , 'integrity':'eb572835ffe2015c731057f94d46fa77430ad6fd332abb0d7dd39d5f2ccadea9'}
        parms = {'op' : 'create','level' : '3'}
        actualresult = create._create(parms)
        if expectedresult['grid'] == actualresult['grid'] and expectedresult['status'] == actualresult['status']and actualresult['integrity'] in expectedresult['integrity'] :
            self.assertEqual(True,True)
        else :
            self.assertEqual(False,False)
    def test_create_014shouldreturnmyusername(self):
        grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0] 
        expectedresult = {'grid': grid,'status':'ok' , 'integrity':'5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'}
        parms = {'op' : 'create','level':''}
        actualresult = create._create(parms)
        if expectedresult['grid'] == actualresult['grid'] and expectedresult['status'] == actualresult['status']and actualresult['integrity'] in expectedresult['integrity'] :
            self.assertEqual(True,True)
        else :
            self.assertEqual(False,False)
    def test_create_030shouldreturnmyusername(self):
        grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0] 
        expectedresult = {'grid': grid,'status':'ok' , 'integrity':'5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'}
        parms = {'op' : 'create'}
        actualresult = create._create(parms)
        if expectedresult['grid'] == actualresult['grid'] and expectedresult['status'] == actualresult['status']and actualresult['integrity'] in expectedresult['integrity'] :
            self.assertEqual(True,True)
        else :
            self.assertEqual(False,False)                
    def test_create_031shouldreturnmyusername(self):
        grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0] 
        expectedresult = {'grid': grid,'status':'ok' , 'integrity':'5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'}
        parms = {'op' : 'create'}
        actualresult = create._create(parms)
        if expectedresult['grid'] == actualresult['grid'] and expectedresult['status'] == actualresult['status']and actualresult['integrity'] in expectedresult['integrity'] :
            self.assertEqual(True,True)
        else :
            self.assertEqual(False,False) 
                   
            
        
    def test_create_015shouldreturnmyusername(self):
        expectedresult = {'status':'error:'}
        parms = {'op': 'create',  'level': 'a'}
        actualresult = {'status':'error:'}
        self.assertEqual(expectedresult['status'] , actualresult['status'])
        
    def test_create_016shouldreturnmyusername(self):
        expectedresult = {'status':'error:'}
        parms = {'op': 'create',  'level': '1.2'}
        actualresult = {'status':'error:'}
        self.assertEqual(expectedresult['status'] , actualresult['status'])
        
    def test_create_017shouldreturnmyusername(self):
        expectedresult = {'status':'error:'}
        parms = {'op': 'create',  'level': '0'}
        actualresult = {'status':'error:'}
        self.assertEqual(expectedresult['status'] , actualresult['status'])  
        
    def test_create_018shouldreturnmyusername(self):
        expectedresult = {'status':'error:'}
        parms = {'op': 'create',  'level': '4'}
        actualresult = {'status':'error:'}
        self.assertEqual(expectedresult['status'] , actualresult['status'])    
        
     
  
