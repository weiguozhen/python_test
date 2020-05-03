*** Settings ***
Library  pylib.tc.WebOpAdmin
Suite Setup  Run Keywords  DeleteAll  training
...  AND  AddCourse  初中语文  1  1
...  AND  AddCourse  初中数学  2  2
Suite Teardown  Run Keywords  DeleteAll  training
...  AND  DeleteAll  course
*** Test Cases ***
case30001
    [Tags]  添加
    addTraining  初中班  qq  1  初中语文  初中数学


case30002
    [Tags]  检查
    getData  training
    ${list}  getData  training
    should be true  $list == ['初中班']