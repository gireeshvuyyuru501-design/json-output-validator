import unittest
from validator import validate, evaluate_cases

class ValidatorTests(unittest.TestCase):
    def test_required(self):
        self.assertEqual(validate({}, {'type':'object','required':['x']})[0]['path'], '$.x')
    def test_bool_is_not_number(self):
        self.assertTrue(validate(True, {'type':'number'}))
    def test_nested_array(self):
        self.assertEqual(validate({'x':[1, 'bad']}, {'type':'object','properties':{'x':{'type':'array','items':{'type':'integer'}}}})[0]['path'], '$.x[1]')
    def test_invalid_json(self):
        self.assertFalse(evaluate_cases([{'id':'bad','output':'{oops'}], {'type':'object'})['results'][0]['valid'])
    def test_valid(self):
        self.assertEqual(validate({'x':'ok'}, {'type':'object','required':['x'],'properties':{'x':{'type':'string'}}}), [])

if __name__ == '__main__':
    unittest.main()
