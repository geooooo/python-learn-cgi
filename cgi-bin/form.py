#! /usr/bin/env python

import os
import cgi
import cgitb
import html

cgitb.enable(0)

print("Content-type: text/html;charset=utf-8")
print()

name = "Guest"
if os.environ["REQUEST_METHOD"].lower() == "post":
    form = cgi.FieldStorage()
    name = html.escape(form.getfirst("name"))

print(
    """
        <!DOCTYPE html>
        <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <title>Form</title>
            </head>
            <body>
                <form action="{action}" method="post">
                    <label>
                        Введите ваше имя:
                        <input type="text" name="name" value="{name}">
                    </label>
                    <input type="submit" value="Отправить">
                </form>
                <h1>Привет, {name} !</h1>
            </body>
        </html>
    """.format(
            action=os.environ["SCRIPT_NAME"],
            name=name
        )
)
