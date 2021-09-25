
import unittest
import dodoku.info as info

class infotest(unittest.TestCase):


    def test_info_010shouldreturnmyusername(self):
        expectedresult = {"info:U can complete this assignment"}
        parms = {'op':'info'}
        actualresult = info._info(parms)
        self.assertDictEqual(expectedresult , actualresult)


