from electionCount import ElectionCount
import unittest

# Default placeholder for a real key value
key = '0000'

class ElectionCountTest(unittest.Testcase):

	def setUp(self):
		global key
		self.elecInstance = ElectionCount(key)

	def testExist(self):
		assert self.elecInstance is not None

	def testLitmus(self):
		count = self.elecInstance.getSentenceCount('Trump', 'Clinton', [1,9,2016], [1,10,2016])
		assert count[0] == 207278
		assert count[1] == 139784


if __name__ == "__main__":
    unittest.main()