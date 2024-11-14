from result import TestResult
from loader import TestLoader
from runner import TestRunner

class TestProgram(object):
	def __init__(self):
		self.result = TestResult()
		self.loader = TestLoader()
		self.runner = TestRunner()

	#def __call__(self):
	#	return run()

	def run(self, test_regs, test_suites, test_cases):
		print "here is function run for main TestProgram"
		print "self.result:{}".format(self.result)
		self.result = self.runner(self.result, self.loader, test_regs, test_suites, test_cases)