from django.test import TestCase
from django.test import SimpleTestCase
from selenium import webdriver


# Create your tests here.

class MyAcademus(SimpleTestCase):

    def test_student_form(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8000/student/new")
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_name("newaluno").click()
        # self.driver.find_element_by_name("name").send_keys("Pedro dos Santos")
        # self.driver.find_element_by_name("birthdate").send_keys("20/11/1996")
        # self.driver.find_element_by_name("cpf").send_keys("02288312376")
        # self.driver.find_element_by_name("course").send_keys("Matemática")
        # self.driver.find_element_by_name("save").click()
        self.driver.close()
        self.driver.quit()
        
if __name__ == '__main__':
    academus = MyAcademus()
    academus.test_student_form()