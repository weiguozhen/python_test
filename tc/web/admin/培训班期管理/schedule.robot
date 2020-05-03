*** Settings ***
Library  pylib.tc.WebOpAdmin
Suite Setup  Run Keywords  DeleteAll  schedule
...  AND  AddCourse  初中语文  1  1
...  AND  AddCourse  初中数学  2  2
...  AND  addTraining  初中班  qq  1  初中语文  初中数学
Suite Teardown  Run Keywords  DeleteAll  course
...  AND  DeleteAll  schedule
...  AND  DeleteAll  training
*** Test Cases ***
case40001
    [Tags]  添加
    addschedule   初中班1期  111  1  初中班

case40002
    [Tags]  检查
    ${list}  getData  schedule
    should be true  $list == ['初中班1期']

