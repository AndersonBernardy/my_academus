from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


# Create your tests here.

class MyAcademusTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("C:\Ellen\chromedriver.exe")

    def tearDown(self):
        self.browser.close()

    def test_student_form(self):
        self.browser.get("http://localhost:8000/student/new")
        self.browser.find_element_by_name("name").send_keys("Pedro dos Santos")
        self.browser.find_element_by_name("birthdate").send_keys("20/11/1996")
        self.browser.find_element_by_name("cpf").send_keys("02288312376")
        self.browser.find_element_by_name("course").send_keys("Matemática")
        time.sleep(20)
        # self.browser.find_element_by_name("save").click()
    
    # def test_course_form(self):
    #     self.browser.get("http://localhost:8000/course/new")
    #     self.browser.find_element_by_name("name").send_keys("Administração")
    #     self.browser.find_element_by_name("initials").send_keys("ADM")
    #     self.browser.find_element_by_name("description").send_keys("Descrição do curso aqui")
    #     self.browser.find_element_by_name("duration").send_keys("Quatro Anos")
    #     # self.browser.find_element_by_name("save").click()
    
    # def test_discipline_form(self):
    #     self.browser.get("http://localhost:8000/discipline/new")
    #     self.browser.find_element_by_name("name").send_keys("Engenharia de Software 1")
    #     self.browser.find_element_by_name("initials").send_keys("ES1")
    #     self.browser.find_element_by_name("description").send_keys("Descrição da matéria aqui")
    #     self.browser.find_element_by_name("course").send_keys("Ciência da Computação")
    #     self.browser.find_element_by_name("academic_period").send_keys("Terceiro Ano")
    #     # self.browser.find_element_by_name("save").click()

    # def test_class_form(self):
    #     self.browser.get("http://localhost:8000/class/new")
    #     self.browser.find_element_by_name("code").send_keys("ES1_2019A")
    #     self.browser.find_element_by_name("discipline").send_keys("CC - Engenharia de Software 1")
    #     self.browser.find_element_by_name("start_date").send_keys("10/02/2019")
    #     self.browser.find_element_by_name("end_date").send_keys("20/11/2019")
    #     self.browser.find_element_by_name("assessment[]").send_keys("Prova 1")
    #     self.browser.find_element_by_name("add_assessment").click()
    #     self.browser.find_element_by_name("assessment[]").send_keys("Trabalho 1")
    #     self.browser.find_element_by_name("class_week[]").send_keys("Terça")
    #     self.browser.find_element_by_name("class_time[]").send_keys("17:00")
    #     self.browser.find_element_by_name("add_class_time").click()
    #     self.browser.find_element_by_name("class_week[]").send_keys("Quinta")
    #     self.browser.find_element_by_name("class_time[]").send_keys("10:30")
    #     #self.browser.find_element_by_name("save").click()
    #     time.sleep(20)