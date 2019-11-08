from django.test import TestCase
from django.test import SimpleTestCase
from selenium import webdriver
import unittest


# Create your tests here.
class TestMyAcademus(SimpleTestCase):

    @unittest.expectedFailure
    def test_student_form(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8000/student/new")
        self.driver.find_element_by_name("name").send_keys("Pedro dos Santos")
        self.driver.find_element_by_name("birthdate").send_keys("20-11-1996")
        self.driver.find_element_by_name("cpf").send_keys("02288312376")
        self.driver.find_element_by_name("course").send_keys("Matemática")
        self.driver.find_element_by_name("save").click()
        self.driver.close()
        


# Example Test Cases
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
