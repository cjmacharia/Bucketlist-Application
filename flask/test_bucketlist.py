import unittest
from bucketlist import Bucketlist

class Buckettest(unittest.TestCase):
     #tests for the class
    def setUp(self):
        self.buckets=Bucketlist()


    def test_if_post_empty(self):
        output=self.buckets.create('','this is my bucketlist by the age of 29','owner')
        self.assertEqual(2,output, "please fill all fields")

    def test_if_description_empty(self):
        output=self.buckets.create('By 28','','owner')
        self.assertEqual(2,output, "please fill the description")        
if __name__ == "__main__":
    unittest.main()        