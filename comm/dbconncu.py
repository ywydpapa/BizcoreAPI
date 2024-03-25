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

