import oracledb

def get_conexao():
    return oracledb.connect(user="rm563045", password="241203", dsn="oracle.fiap.com.br/orcl")

def insere_medico(medico):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "insert into t_medico(id_medico, nm_medico, nm_especialidade) values(sq_t_medico.nextval, :nm_medico, :nm_especialidade) returning id_medico into :id"

            new_var = cur.var(oracledb.NUMBER)
            medico['id'] = new_var

            cur.execute(sql, medico)
            medico['id'] = new_var.getvalue()[0]
        con.commit()

def insere_paciente(paciente):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "insert into t_paciente(id_paciente, nm_paciente, nm_email) values(sq_t_paciente.nextval, :nm_paciente, :nm_email) returning id_paciente into :id"

            new_var = cur.var(oracledb.NUMBER)
            paciente['id'] = new_var

            cur.execute(sql, paciente)
            paciente['id'] = new_var.getvalue()[0]
        con.commit()

def insere_consulta(consulta):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                insert into t_consulta (id_consulta, id_paciente, id_medico, dt_hora,
                    tp_consulta, st_confirmacao)
                values (sq_t_consulta.nextval, :id_paciente, :id_medico, TO_DATE(:dt_hora, 'YYYY-MM-DD HH24:MI'), :tp_consulta, :st_confirmacao)
                returning id_consulta into :id
                """

            new_var = cur.var(oracledb.NUMBER)
            consulta['id'] = new_var

            cur.execute(sql, consulta)
            consulta['id'] = new_var.getvalue()[0]
        con.commit()

def insere_lembrete(lembrete):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                insert into t_lembrete (id_lembrete, id_consulta)
                values (sq_t_lembrete.nextval, :id_consulta)
                returning id_lembrete into :id
                """

            new_var = cur.var(oracledb.NUMBER)
            lembrete['id'] = new_var

            cur.execute(sql, lembrete)
            lembrete['id'] = new_var.getvalue()[0]
        con.commit()

def atualizar_medico(medico: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                UPDATE t_medico
                SET nm_medico = :nm_medico,
                    nm_especialidade = :nm_especialidade
                WHERE id_medico = :id
            """
            cur.execute(sql, medico)
        con.commit()

def atualizar_paciente(paciente: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                UPDATE t_paciente
                SET nm_paciente = :nm_paciente,
                    nm_email = :nm_email
                WHERE id_paciente = :id
            """
            cur.execute(sql, paciente)
        con.commit()

def atualizar_consulta(consulta: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                UPDATE t_consulta
                SET id_paciente = :id_paciente,
                    id_medico = :id_medico,
                    dt_hora = TO_DATE(:dt_hora, 'YYYY-MM-DD HH24:MI'),
                    tp_consulta = :tp_consulta,
                    st_confirmacao = :st_confirmacao
                WHERE id_consulta = :id
            """
            cur.execute(sql, consulta)
        con.commit()

def atualizar_lembrete(lembrete: dict):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                UPDATE t_lembrete
                SET id_consulta = :id_consulta
                WHERE id_lembrete = :id
            """
            cur.execute(sql, lembrete)
        con.commit()

def deletar_medico(id_medico: int):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "DELETE FROM t_medico WHERE id_medico = :id"
            cur.execute(sql, {"id": id_medico})
        con.commit()

def deletar_paciente(id_paciente: int):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "DELETE FROM t_paciente WHERE id_paciente = :id"
            cur.execute(sql, {"id": id_paciente})
        con.commit()

def deletar_consulta(id_consulta: int):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "DELETE FROM t_consulta WHERE id_consulta = :id"
            cur.execute(sql, {"id": id_consulta})
        con.commit()

def deletar_lembrete(id_lembrete: int):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = "DELETE FROM t_lembrete WHERE id_lembrete = :id"
            cur.execute(sql, {"id": id_lembrete})
        con.commit()

def consultar_medico():
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                SELECT 
                    id_medico,
                    nm_medico,
                    nm_especialidade
                FROM t_medico
                ORDER BY id_medico
            """
            cur.execute(sql)
            return cur.fetchall()

def consultar_paciente():
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                SELECT 
                    id_paciente,
                    nm_paciente,
                    nm_email
                FROM t_paciente
                ORDER BY id_paciente
            """
            cur.execute(sql)
            dados = cur.fetchall()
            return dados
        
def consultar_consulta():
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                SELECT 
                    id_consulta,
                    id_paciente,
                    id_medico,
                    dt_hora,
                    tp_consulta,
                    st_confirmacao
                FROM t_consulta
                ORDER BY id_consulta
            """
            cur.execute(sql)
            return cur.fetchall()
        
def consultar_lembrete():
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                SELECT 
                    id_lembrete,
                    id_consulta,
                    dt_criacao
                FROM t_lembrete
                ORDER BY id_lembrete
            """
            cur.execute(sql)
            return cur.fetchall()

def consultar_medico_id(id_medico: int):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                SELECT 
                    id_medico,
                    nm_medico,
                    nm_especialidade
                FROM t_medico
                WHERE id_medico = :id
            """
            cur.execute(sql, {"id": id_medico})
            return cur.fetchone()

def consultar_paciente_id(id_paciente: int):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                SELECT 
                    id_paciente,
                    nm_paciente,
                    nm_email
                FROM t_paciente
                WHERE id_paciente = :id
            """
            cur.execute(sql, {"id": id_paciente})
            return cur.fetchone()
        
def consultar_consulta_id(id_consulta: int):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                SELECT 
                    id_consulta,
                    id_paciente,
                    id_medico,
                    dt_hora,
                    tp_consulta,
                    st_confirmacao
                FROM t_consulta
                WHERE id_consulta = :id
            """
            cur.execute(sql, {"id": id_consulta})
            return cur.fetchone()

def consultar_lembrete_id(id_lembrete: int):
    with get_conexao() as con:
        with con.cursor() as cur:
            sql = """
                SELECT 
                    id_lembrete,
                    id_consulta,
                    dt_criacao
                FROM t_lembrete
                WHERE id_lembrete = :id
            """
            cur.execute(sql, {"id": id_lembrete})
            return cur.fetchone()