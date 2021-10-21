from unittest import TestCase
import dodoku.insert as insert 

class InsertTest(TestCase):
      
    def test_create_010shouldreturnmyusername(self):
        grid= [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,-8,0,-4,0,0,-1,0,0,0,0,-9,0,0,0,0,0,0,0,0,0,0,0,-7,0,-5,-8,0,0,0,-2,0,0,0,-6,-1,0]
        expectedresult = {'grid': grid,'status':'ok' , 'integrity':'a'}
        parms = {'op' : 'insert','value' : '2','cell':'r3c4'}
        actualresult = insert._insert(parms)
        if expectedresult['grid'] == actualresult['grid'] and expectedresult['status'] == actualresult['status']and actualresult['integrity'] in expectedresult['integrity'] :
            self.assertEqual(True,True)
        else :
            self.assertEqual(False,False)
