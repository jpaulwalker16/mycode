#!/usr/bin/env python3

failed_logins = 0
success_logins = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as readfile:

    for line in readfile: 

        if "----] Authorization failed" in line:
            failed_logins += 1

        elif "----] INFO" in line:
            success_logins += 1

print("\nthe number of successful login is:", success_logins)
print("the number of failed logins is:", failed_logins)
