
import unittest
#继承unittest.TestCase类
class TestStringMethods(unittest.TestCase):
#assertEqual()来判断预期结果，
#assertTrue()和assertFalse来做是非判断
#assertRaises()来判断预期的异常是否有被抛出
	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s='hello world'
		self.assertEqual(s.split(),['hello','world'])
		with self.assertRaises(TypeError):
			s.split(2)
'''
if __name__ == '__main__':
	unittest.main()
'''
suite=unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)