#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time      : 2020/4/10 12:24 下午
# Software  : PyCharm
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select


class WebOpAdmin:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def setupWebTest(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://172.20.10.4:9999/mgr/login/login.html')

    def tearDownWebTest(self):
        self.driver.quit()

    def loginWebSite(self, username, passwd):

        name = self.driver.find_element_by_id('username')
        name.clear()
        name.send_keys(username)
        word = self.driver.find_element_by_id('password')
        word.clear()
        word.send_keys(passwd)
        self.driver.find_element_by_css_selector('[onclick="postLoginRequest()"]').click()
        sleep(1)

    def AddCourse(self, name, desc, idx):
        self.driver.find_element_by_css_selector('[ui-sref="course"]').click()
        self.driver.find_element_by_css_selector('.btn-md').click()
        self.driver.find_element_by_css_selector('[ng-model="addData.name"]').clear()
        self.driver.find_element_by_css_selector('[ng-model="addData.desc"]').clear()
        self.driver.find_element_by_css_selector('[ng-model="addData.display_idx"]').clear()
        self.driver.find_element_by_css_selector('[ng-model="addData.name"]').send_keys(name)
        self.driver.find_element_by_css_selector('[ng-model="addData.desc"]').send_keys(desc)
        self.driver.find_element_by_css_selector('[ng-model="addData.display_idx"]').send_keys(idx)
        self.driver.find_element_by_css_selector('[ng-click="addOne()"]').click()
        sleep(1)

    def addTeacher(self, realnamme, username, desc, idx, lesson):
        self.driver.find_element_by_css_selector('a[ui-sref=teacher]').click()
        sleep(1)
        self.driver.find_element_by_css_selector('button[ng-click^=showAddOne]').click()
        self.driver.find_element_by_css_selector("input[ng-model='addEditData.realname']").clear()
        self.driver.find_element_by_css_selector("input[ng-model='addEditData.username']").clear()
        self.driver.find_element_by_css_selector("textarea[ng-model='addEditData.desc']").clear()
        self.driver.find_element_by_css_selector("input[ng-model='addEditData.display_idx']").clear()

        self.driver.find_element_by_css_selector("input[ng-model='addEditData.realname']").send_keys(realnamme)
        self.driver.find_element_by_css_selector("input[ng-model='addEditData.username']").send_keys(username)
        self.driver.find_element_by_css_selector("textarea[ng-model='addEditData.desc']").send_keys(desc)
        self.driver.find_element_by_css_selector("input[ng-model='addEditData.display_idx']").send_keys(idx)
        del_courses = self.driver.find_elements_by_css_selector('[ng-click="addEditData.delTeachCourse(course)"]')
        for _ in del_courses:
            _.click()
            # sleep(1)
        self.driver.find_element_by_css_selector("select[ng-model*=courseSelected]").send_keys(lesson)
        self.driver.find_element_by_css_selector("button[ng-click*=addTeachCourse]").click()
        self.driver.find_element_by_css_selector('button[ng-click^=addOne]').click()
        sleep(1)

    def addTraining(self, trainname, desc, idx, *contains):
        self.driver.find_element_by_css_selector('[ui-sref="training"]').click()
        sleep(1)
        self.driver.find_element_by_css_selector('[ng-click="showAddOne=true"]').click()
        self.driver.find_element_by_css_selector('[ng-model="addEditData.name"]').clear()
        self.driver.find_element_by_css_selector('[ng-model="addEditData.desc"]').clear()
        self.driver.find_element_by_css_selector('[ng-model="addEditData.display_idx"]').clear()

        self.driver.find_element_by_css_selector('[ng-model="addEditData.name"]').send_keys(trainname)
        self.driver.find_element_by_css_selector('[ng-model="addEditData.desc"]').send_keys(desc)
        self.driver.find_element_by_css_selector('[ng-model="addEditData.display_idx"]').send_keys(idx)
        del_courses = self.driver.find_elements_by_css_selector('[ng-click="addEditData.delTeachCourse(course)"]')
        for _ in del_courses:
            _.click()
        for i in contains:
            select = Select(self.driver.find_element_by_css_selector('[ng-options*="courseList"]'))
            select.select_by_visible_text(i)
            sleep(1)
            self.driver.find_element_by_css_selector('[ng-click="addEditData.addTeachCourse()"]').click()
        self.driver.find_element_by_css_selector('[ng-click="addOne()"]').click()
        sleep(1)

    def addschedule(self, schedule, desc, idx, *training):
        self.driver.find_element_by_css_selector('[ui-sref="traininggrade"]').click()
        self.driver.find_element_by_css_selector('[ng-click="showAddOne=true"]').click()
        self.driver.find_element_by_css_selector('[ng-model="addEditData.name"]').clear()
        self.driver.find_element_by_css_selector('[ng-model="addEditData.desc"]').clear()
        self.driver.find_element_by_css_selector('[ng-model="addEditData.display_idx"]').clear()

        self.driver.find_element_by_css_selector('[ng-model="addEditData.name"]').send_keys(schedule)
        self.driver.find_element_by_css_selector('[ng-model="addEditData.desc"]').send_keys(desc)
        self.driver.find_element_by_css_selector('[ng-model="addEditData.display_idx"]').send_keys(idx)
        del_courses = self.driver.find_elements_by_css_selector('[ng-click="addEditData.delTeachCourse(course)"]')
        for _ in del_courses:
            _.click()
        for i in training:

            select = Select(self.driver.find_element_by_css_selector('[ng-options*="trainingList"]'))
            select.select_by_visible_text(i)
            sleep(1)
        self.driver.find_element_by_css_selector('[ng-click="addOne()"]').click()
        sleep(1)

    def getData(self, objName):
        if objName == 'course':
            self.driver.find_element_by_css_selector('[ui-sref="course"]').click()
        elif objName == 'teacher':
            self.driver.find_element_by_css_selector('ul.nav a[href*=teacher]').click()
        elif objName == 'training':
            self.driver.find_element_by_css_selector('[ui-sref="training"]').click()
        elif objName == 'schedule':
            self.driver.find_element_by_css_selector('[ui-sref="traininggrade"]').click()
        eles = self.driver.find_elements_by_css_selector("tr>td:nth-child(2) span")
        data = [i.text for i in eles]
        return data

    def DeleteAll(self, objName):
        if objName == 'course':
            self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        elif objName == 'teacher':
            self.driver.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
        elif objName == 'training':
            self.driver.find_element_by_css_selector('[ui-sref="training"]').click()
        elif objName == "schedule":
            self.driver.find_element_by_css_selector('[ui-sref="traininggrade"]').click()
        else:
            raise Exception('keyword DeleteAll get unknow obj Name %s' % objName)

        self.driver.implicitly_wait(2)
        while True:
            delButtons = self.driver.find_elements_by_css_selector('*[ng-click^=delOne]')

            if delButtons == []:
                break

            delButtons[0].click()
            self.driver.find_element_by_css_selector('.modal-footer  .btn-primary').click()
            sleep(1)

        self.driver.implicitly_wait(10)

    # def DeleteAllCourse(self):
    #     self.driver.find_element_by_css_selector('a[href*=teacher]').click()
    #     for _ in range(20):
    #         sleep(1)
    #         self.driver.implicitly_wait(2)
    #         eles = self.driver.find_elements_by_xpath('button[@ng-click="delOne(one)"]')
    #         if eles == []:
    #             break
    #         else:
    #             eles[0].click()
    #             self.driver.find_element_by_css_selector('button.btn-primary').click()
    #     self.driver.implicitly_wait(10)
