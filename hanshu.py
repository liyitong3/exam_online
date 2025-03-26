from mysql_util import MysqlUtil as mysql

def chaxunsuoyou(neirong:str):
    db=mysql()
    sql=neirong
    if neirong=='zcbh' or neirong=='syr' or neirong=='cfdd':
        sql="select DISTINCT %s from zcxx202310 " % (neirong)
        sql = "select DISTINCT %s from zcxx202401 " % (neirong)
    else:
        return '不支持的查询条件'
    print(sql)
    jieguo = db.fetchall(sql)
    id_list = []
    for i in jieguo:
        id_list.append(i[neirong])

    return id_list