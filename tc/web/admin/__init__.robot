*** Settings ***
Library  pylib.tc.WebOpAdmin
Variables  cfg.py
Suite Setup  loginWebSite  ${user1['name']}  ${user1['pwd']}

