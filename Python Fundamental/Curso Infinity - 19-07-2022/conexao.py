import pymysql.cursors
import uteis.info_uteis as info


class Conexao:
    def __init__(self):
        self.conexao = pymysql.connect(host=info.host,
                                       user=info.username,
                                       password=info.password,
                                       database=info.database,
                                       cursorclass=pymysql.cursors.DictCursor)

    def executarSql(self, sql, parametros=None, tipo=None):
        with self.conexao.cursor() as cursor:
            if parametros is None and tipo is None:
                cursor.execute(sql)
                resultado = cursor.fetchall()
                return resultado
            elif parametros is not None and tipo is None:
                cursor.execute(sql, (parametros))
                resultado = cursor.fetchall()
                return resultado
            elif tipo is not None:
                cursor.execute(sql, (parametros))
                self.conexao.commit()

