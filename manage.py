#!/usr/bin/env python
import os
import sys
import mysql.connector

mydb = mysql.connector.connect(
  host="https://serwer2092649.home.pl/sql:3306",
  user="32853696_app",
  passwd="_sQ98AM",
  database="32853696_app",
)



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "facebook.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
