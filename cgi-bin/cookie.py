#! /usr/bin/env python

import cgi
import cgitb
import http.cookies
import os

cgitb.enable(0)

cookie = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
count  = int(cookie["count"].value) if "count" in cookie else 1
cookie["count"] = count + 1

print("Content-type: text/html;charset=utf-8")
print(cookie)
print()

print(
    """
        <!DOCTYPE html>
        <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <title>Cookie</title>
            </head>
            <body>
                <h1>Количество посещений: {count}</h1>
            </body>
        </html>
    """.format(
            count=count
        )
)
