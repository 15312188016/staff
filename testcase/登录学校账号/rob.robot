*** Settings ***
Library   pages.staffDevelopment.StaffDevelopment
Library   pages.login_taidii.Login





*** Test Cases ***

进入老师成长-职工培训 001
#校长创建课程并发布，验证是否发布成功，列表中展示该课程

        #进入教师职工界面

        ${coursename}   create online course

        ${courselist}   course list

        should be true  $coursename==$courselist[0]




