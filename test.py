import unittest
import main

class TestGame(unittest.TestCase):

  def test_input_right_guess(self):
    result = main.run_guess(5, 5)
    self.assertTrue(result)
    
  def test_input_wrong_guess(self):
    result = main.run_guess(5, 6)
    self.assertFalse(result)
      
  def test_input_wrong_number(self):
    result = main.run_guess(5, 11)
    self.assertFalse(result)

  def test_input_wrong_type(self):
    result = main.run_guess(5, '11')
    self.assertFalse(result)


if __name__ == '__main__':
  unittest.main()
# class TestMain(unittest.TestCase):

#   def setUp(self):

#     print('about to test function')

#   def test_do_stuff(self):
#     test_param = 10
#     result = main.do_stuff(test_param)
#     self.assertEqual(result, 15)

#   def test_do_stuff2(self):
#     test_param = 'ergreg'
#     result = main.do_stuff(test_param)
#     self.assertIsInstance(result, ValueError)

#   def test_do_stuff3(self):
#     test_param = None
#     result = main.do_stuff(test_param)
#     self.assertEqual(result, 'please enter number')

#   def test_do_stuff4(self):
#     test_param = ''
#     result = main.do_stuff(test_param)
#     self.assertEqual(result, 'please enter number')

#   def tearDown(self):
#     print('cleaning up')


# if __name__ == '__main__':
#   unittest.main()
