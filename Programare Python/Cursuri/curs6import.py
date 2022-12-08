class Test_case1:
    def printeaza_test_case1(self):
        print('running Test case 1')

class Test_case2:
    def printeaza_test_case(self):
        print('running Test case 2')

class Test_case3:
    def __init__(self, name, summary):
        self.name = name
        self.summary = summary
    def retun_name(self):
        return self.name
    def return_summery(self):
        return self.summary
    def printeaza_test_case(self):
        print('running Test case 3')

