from unittest import TestCase
import dodoku.create as create
import random

class CreateTest(TestCase):
    def test_create_010shouldreturnmyusername(self):
        grid= [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,-8,0,-4,0,0,-1,0,0,0,0,-9,0,0,0,0,0,0,0,0,0,0,0,-7,0,-5,-8,0,0,0,-2,0,0,0,-6,-1,0]
        expectedresult = {'grid': grid,'status':'ok'}
        parms = {'op' : 'create','level' : '2'}
        actualresult = create._create(parms)
        if expectedresult['grid'] == actualresult['grid'] and expectedresult['status'] == actualresult['status']and actualresult['integrity'] in expectedresult['integrity'] :
            self.assertequal(True,True)
        else :
            self.assertequal(False,False)
  
    def test_create_011shouldreturnmyusername(self):
        grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0] 
        expectedresult = {'grid': grid,'status':'ok'}
        parms = {'op' : 'create', 'level' : '1'}
        actualresult = create._create(parms)
        self.assertEqual(expectedresult , actualresult)
        
    def test_create_013shouldreturnmyusername(self):
        expectedresult = {'status' : 'error:'}
        parms = {'op' : 'create', 'level' : 'a'}
        actualresult = create._create(parms)
        self.assertEqual(expectedresult['status'] , actualresult['status'])
  
