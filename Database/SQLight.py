# -*- coding: utf-8 -*-
import sqlite3
from random import randint
import numpy
from array import array

class SQLiteInsertError(Exception):
    def __init__(self, message):
        self.message = message
        super(SQLiteInsertError, self).__init__('{0}'.format(self.message))


class SQLight:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

# GETTER ----------------------------------
    def get_from_table(self, table, value, where):
        with self.connection:
            total = 0
            liste = u''
            synonyme = ''
            punkte = 0
            if len(where)>0:
                synonyme = self.cursor.execute('SELECT ' +str(value)+ ' FROM ' + str(table) + ' WHERE ' + str(where)).fetchall()
            else:
                synonyme = self.cursor.execute('SELECT ' +str(value)+ ' FROM ' + str(table)).fetchall()
            for syn in synonyme:
                for s in syn:
                    liste = liste + unicode(s) + u': '
                liste = liste + u'\n'
            return liste
        
    def get_ranking(self):
        with self.connection:
            total = 0
            liste = u''
            alle = self.get_player()
            i = 0
            p_p = [(0,''),] * len(alle)
            for player in alle:
                total = 0
                synonyme = self.cursor.execute('SELECT ID FROM Synonym WHERE Chat_id='+str(player[1])).fetchall()
                punkte = len(self.cursor.execute('SELECT * FROM Rating WHERE Rating=1 AND Chat_id='+str(player[1])).fetchall())
                total = total + 0.5*punkte
                for syn in synonyme:
                    punkte = len(self.cursor.execute('SELECT * FROM Rating WHERE Rating<1 AND Synonym_id='+str(syn[0])).fetchall())
                    total = total + punkte
                p_p[i] = (total, player[2])
                i = i + 1
            for p in sorted(p_p, key=lambda p: -p[0]):
                liste = liste + unicode(p[1]) + u' hat: \t\t' + unicode(p[0]) + u' Punkte\n'
            return liste

    def get_setting(self, chat_id):
        with self.connection:
            settings = self.cursor.execute('SELECT Auto FROM Settings WHERE Chat_id='+str(chat_id)).fetchone()
            if settings:
                return settings[0]
            else:
                return 0


    def get_player(self):
        with self.connection:
            alle = self.cursor.execute('SELECT * FROM Player').fetchall()
            return alle

    def get_by_id(self, table, value, word_id):
        with self.connection:
            syn = self.cursor.execute('SELECT ' +str(value)+ ' FROM ' + str(table) + ' WHERE ID=' + str(word_id)).fetchone()[0]
            return syn

# SETTER ----------------------------------
        

    def insert_player(self, chat_id, name):
        with self.connection:
            anzahl = len(self.cursor.execute('SELECT * FROM Player WHERE Chat_id='+str(chat_id)).fetchall())
            if anzahl < 1:
                if self.cursor.execute('INSERT INTO Player (Chat_id, Name) values (?, ?)',
                                       (chat_id, name)).rowcount < 0:
                    raise SQLiteInsertError('Failed to insert data')
                # self.connection.commit()
            return True


    def delete(self, table, value_id):
        with self.connection:
            self.cursor.execute('DELETE FROM ' +str(table)+ ' WHERE ID='+str(value_id))
            # self.connection.commit()
            return True
            
    def execute(self, code):
        with self.connection:
            try:
                self.cursor.execute(code)
            except:
                pass

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()


