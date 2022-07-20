
from flask_blog.models.entries import Entry
from flask_script import Command


class InitDB(Command):
    "create database"

    def run(self):
        if not Entry.exists():
            Entry.create_table(read_capacity_units=5, write_capacity_units=2)
PynamoDBでは、exists()メソッドでそのテーブルが存在しているかどうかを判定す
