import pymysql
import settings

db = pymysql.connect(
        host=settings.host
        , port=settings.port
        , user=settings.user
        , passwd=settings.password
        , db=settings.database
        , charset='utf8'
        )

cursor = db.cursor()

def logincheck(compid,userid,userpass):
    cur = db.cursor()
    sql = "select userNo,userName,userRole from swc_user u left join swc_company c on u.compNo = c.compNo where u.userId=%s and u.userPasswd=password(%s) and c.compId=%s and u.attrib not like %s"
    cur.execute(sql,(userid,userpass,compid,'XXX%'))
    results = cur.fetchone()
    cur.close()
    return results

def listsopp():
    cur = db.cursor()
    sql = "select * from swc_sopp where attrib not like %s"
    cur.execute(sql, 'XXX%')
    results = list(cur.fetchall())
    cur.close()
    return results

def detailsopp(soppno):
    cur = db.cursor()
    sql = "select * from swc_sopp where soppNo = %s and attrib not like %s"
    cur.execute(sql, (soppno,'XXX%'))
    results = list(cur.fetchall())
    cur.close()
    return results

def listcont():
    cur = db.cursor()
    sql = "select * from swc_cont where attrib not like %s"
    cur.execute(sql, 'XXX%')
    results = list(cur.fetchall())
    cur.close()
    return results

def detailcont(contno):
    cur = db.cursor()
    sql = "select * from swc_cont where contNo = %s and attrib not like %s"
    cur.execute(sql, (contno, 'XXX%'))
    results = list(cur.fetchall())
    cur.close()
    return results

