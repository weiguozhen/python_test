*** Settings ***
Library  pylib.tc.WebOpAdmin
Suite Setup  DeleteAll  course
Suite Teardown  DeleteAll  course
*** Test Cases ***
case10001
    [Tags]  添加
    AddCourse  s  1  2
    AddCourse  p  2  1

case10002
    [Tags]  检查
    ${list}  getData  course
    should be true  $list == ['p','s']

