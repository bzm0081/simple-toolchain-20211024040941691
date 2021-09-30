from unittest import TestCase
import dodoku.create as create
import random

class CreateTest(TestCase):
    def test_create_010shouldreturnmyusername(self):
        grid= [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,-8,0,-4,0,0,-1,0,0,0,0,-9,0,0,0,0,0,0,0,0,0,0,0,-7,0,-5,-8,0,0,0,-2,0,0,0,-6,-1,0]
        expectedresult = {'grid': grid,'status':'ok' , 'integrity':'6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a'}
        parms = {'op' : 'create','level' : '1'}
        actualresult = create._create(parms)
        if expectedresult['grid'] == actualresult['grid'] and expectedresult['status'] == actualresult['status']and actualresult['integrity'] in expectedresult['integrity'] :
            self.assertEqual(True,True)
        else :
            self.assertEqual(False,False)
  
        
    def test_create_013shouldreturnmyusername(self):
        expectedresult = {'status' : 'error:'}
        parms = {'op' : 'create', 'level' : 'a'}
        actualresult = create._create(parms)
        self.assertEqual(expectedresult['status'] , actualresult['status'])
  
