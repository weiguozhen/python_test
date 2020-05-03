*** Settings ***
Library  pylib.tc.WebOpAdmin
Suite Setup  Run Keywords  DeleteAll  teacher
...  AND  DeleteAll  course
...  AND  AddCourse  初中语文  1  1
...  AND  AddCourse  初中数学  2  2
Suite Teardown  Run Keywords  DeleteAll  teacher
...  AND  DeleteAll  course
*** Test Cases ***
case20001
    [Tags]  添加
    addTeacher   小三  111  333  2  初中语文
    addTeacher   小四  444  666  1  初中数学


case20002
    [Tags]  检查
    ${list}  getData  teacher
    should be true  $list==['小四','小三']
