import pymysql
import comm.settings

db = pymysql.connect(
    host=comm.settings.host
    , port=comm.settings.port
    , user=comm.settings.user
    , passwd=comm.settings.password
    , db=comm.settings.database
    , charset='utf8'
)

cursor = db.cursor()


def logincheck(compid, userid, userpass):
    cur = db.cursor()
    sql = "select userNo,userName,userRole from swc_user u left join swc_company c on u.compNo = c.compNo where u.userId=%s and u.userPasswd=password(%s) and c.compId=%s and u.attrib not like %s"
    cur.execute(sql, (userid, userpass, compid, 'XXX%'))
    results = cur.fetchone()
    cur.close()
    return results


def listsopp():
    cur = db.cursor()
    sqlf = "select a.regDatetime,d.desc03, f.desc03,a.soppTitle,a.soppNo, c.custName,g.custName,b.userName,a.soppTargetAmt,e.desc03,a.soppTargetDate from swc_sopp a left join swc_user b on a.userNo = b.userNo left join swc_cust c on a.custNo = c.custNo left join swc_code d on a.soppType = d.codeNo left join swc_code e on a.soppStatus = e.codeNo left join swc_code f on a.cntrctMth = f.codeNo left join swc_cust g on a.buyrNo = g.custNo"
    sqlc = " where a.attrib not like %s"
    sqls = "order by a.soppTargetDate desc"
    sql = sqlf + sqlc + sqls
    print(sql)
    cur.execute(sql, 'XXX%')
    results = list(cur.fetchall())
    cur.close()
    return results


def detailsopp(soppno):
    cur = db.cursor()
    sql = "select * from swc_sopp where soppNo = %s and attrib not like %s"
    cur.execute(sql, (soppno, 'XXX%'))
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


def listcust():
    cur = db.cursor()
    sql = "select * from swc_cust where attrib not like %s"
    cur.execute(sql, 'XXX%')
    results = list(cur.fetchall())
    cur.close()
    return results


def detailcust(custno):
    cur = db.cursor()
    sql = "select * from swc_cust where custNo=%s and attrib not like %s"
    cur.execute(sql, (custno, 'XXX%'))
    results = list(cur.fetchall())
    cur.close()
    return results


def listsched():
    cur = db.cursor()
    sql = "select * from swc_sched where attrib not like %s"
    cur.execute(sql, 'XXX%')
    results = list(cur.fetchall())
    cur.close()
    return results


def listsales():
    cur = db.cursor()
    sql = "select * from swc_sales where attrib not like %s"
    cur.execute(sql, 'XXX%')
    results = list(cur.fetchall())
    cur.close()
    return results
