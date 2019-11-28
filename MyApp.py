import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import sqlite3 as sql

class Start(BoxLayout):
    user = ObjectProperty()
    password = ObjectProperty()

    def get_started(self):
        print('here we go')

    def add_user(self):
        con = sql.connect('user.db')
        cur = con.cursor()
        cur.execute("""INSERT INTO id (user,password) VALUES (?,?)""",(self.user.text,self.password.text)
                    )
        con.commit()
        con.close()



class MyApp(App):
    con = sql.connect('user.db')
    cur = con.cursor()
    cur.execute(""" CREATE TABLE id(
    user text,
    password text)
    """)
    con.commit()
    con.close()

if __name__ == '__main__':
    MyApp().run()
