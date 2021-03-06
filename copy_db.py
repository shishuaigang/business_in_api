import pymssql

# 8088数据库直接分离备份
import os


def copy_database():
    conn = pymssql.connect(host="192.168.31.99\\sql2012", user="sa", password="Esl91n",
                           database="master")
    cur = conn.cursor()
    print("Connect database successfully")
    print("关闭所有链接")
    sql1 = '''
    use master
    begin transaction
    DECLARE @sql NVARCHAR(500)
    DECLARE @spid NVARCHAR(20)

    DECLARE #tb CURSOR FOR
    SELECT spid=CAST(spid AS VARCHAR(20)) FROM master..sysprocesses WHERE dbid=DB_ID('InroadTest')
    OPEN #tb
    FETCH NEXT FROM #tb INTO @spid
    WHILE @@fetch_status = 0 
        BEGIN
            EXEC('kill '+@spid)
            FETCH NEXT FROM #tb INTO @spid
        END
    CLOSE #tb
    DEALLOCATE #tb
    commit transaction
    commit transaction
    '''
    cur.execute(sql1)
    print("done")
    print("分离数据库")
    cur.callproc('sp_detach_db', ("InroadTest",))
    print("done")
    print("copy 数据库")
    os.system("net use * /del /y")
    os.system(r"net use \\192.168.31.99\ipc$ Esl91n /user:Administrator")
    os.system(r"xcopy  \\192.168.31.99\d$\DB\InroadTest.mdf   \\192.168.31.99\e$\TestDb\InroadTestBak  /s/e/y/r/q")
    os.system(r"xcopy  \\192.168.31.99\d$\DB\InroadTest_1.ldf   \\192.168.31.99\e$\TestDb\InroadTestBak  /s/e/y/r/q")
    os.system("net use * /del /y")
    print("done")
    sql2 = '''
    begin transaction
    commit transaction
    '''
    cur.execute(sql2)
    cur.callproc('sp_attach_db', ('InroadTest', 'E:\TestDb\InroadTestBak\InroadTest.mdf',))
    print("分离备份完成")
    # conn.commit()
    cur.close()
    conn.close()


copy_database()
