*** Settings ***
Library   pages.login_taidii.Login
Library   pages.staffDevelopment.StaffDevelopment

Suite Setup     run keywords   login sys
                     ...  AND   go to staff train


