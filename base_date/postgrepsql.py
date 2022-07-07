from create_bot import bot
from datetime import datetime, time
import psycopg2 as ps
import os

#функция старта
def sql_start():
    global base, cur
    base = ps.connect(os.environ.get( "DATABASE_URL" ), sslmode= 'require')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')

#функция добавления в БД
async def sql_add_command(id, date):
    x= [str(id)]
    for i in date:
        x.append(i)
    x[1] = x[1].strftime("%d:%m:%Y")
    cur.execute ("INSERT INTO entry (id, date, service, time) VALUES (%s, %s, %s, %s)", x)
    base.commit()

 #Функция отправки записей клиента
async def sql_read( message ):
    for ret in cur.execute('SELECT * FROM entry WHERE id ==?', ( message.from_user.id, ) ).fetchall():
        await bot.send_message( message.from_user.id, f'Your entries\n {ret[1]} {ret[-1]} {ret[2]}' )