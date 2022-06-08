import sqlite3
from create_bot import bot
from datetime import datetime, time


#функция старта
def sql_start():
    global base, cur
    base = sqlite3.connect('sql_date.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute(' CREATE TABLE IF NOT EXISTS {}( id, date, service, time ) '.format('data'))
    base.commit()

#функция добавления в БД
async def sql_add_command(id, date):
    x= [id]
    for i in date:
        x.append(i)
    x[1] = x[1].strftime("%d:%m:%Y")
    cur.executemany ('INSERT INTO data VALUES (?, ?, ?, ?)', (x, ) )
    base.commit()

 #Функция отправки записей клиента
async def sql_read( message ):
    for ret in cur.execute('SELECT * FROM data WHERE id ==?', ( message.from_user.id, ) ).fetchall():
        await bot.send_message( message.from_user.id, f'Your entries\n {ret[1]} {ret[-1]} {ret[2]}' )



'''
base.execute('CREATE TABLE IF NOT EXISTS {}(id, service)'.format('data'))
base.commit()

cur.execute('INSERT INTO data VALUES(?, ?)', ('123', 'striska'))
base.commit()


cur.execute('INSERT INTO data VALUES(?, ?)', ('364', 'striska2'))
base.commit()
    
r = cur.execute('SELECT service FROM data').fetchall()
r = cur.execute('SELECT service FROM data WHERE id == ?', ('123',)).fetchone()
'''
