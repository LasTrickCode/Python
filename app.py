import traceback
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import banco

app = Flask(__name__)

CORS(app, origins="*")

@app.route("/lembrete", methods=['GET'])
@cross_origin()
def listar_lembretes_por_paciente():
    try:
        paciente_id = request.args.get("pacienteId", type=int)
        if not paciente_id:
            return {"erro": "Informe o parâmetro pacienteId"}, 400

        lembretes_tuplas = banco.listar_por_paciente(paciente_id)
        lembretes = [
            {
                "id_lembrete": l[0],
                "id_consulta": l[1],
                "dt_hora": str(l[2]),
                "tp_consulta": l[3],
                "st_confirmacao": l[4],
                "id_paciente": l[5],
                "nm_paciente": l[6],
                "nm_email": l[7],
                "id_medico": l[8],
                "nm_medico": l[9],
                "nm_especialidade": l[10]
            }
            for l in lembretes_tuplas
        ]

        return jsonify(lembretes), 200

    except Exception as erro:
        traceback.print_exc()
        return {"erro": "Erro na consulta de lembretes"}, 400


@app.route("/consulta/<int:id>", methods=['PUT'])
@cross_origin()
def atualizar_status_consulta(id):
    try:
        dados = request.get_json()
        status = dados.get("statusConfirmacao", "").upper().strip()
        if status not in ("C", "D"):
            return {"erro": "Status inválido. Use apenas 'C' (Confirmada) ou 'D' (Desmarcada)."}, 400

        consulta = banco.consultar_consulta_id(id)
        if not consulta:
            return {"erro": "Consulta não encontrada"}, 404
        consulta_dict = {
            "id_consulta": consulta[0],
            "st_confirmacao": status
        }

        linhas = banco.atualizar_status_confirmacao(consulta_dict)

        if linhas == 0:
            return {"erro": "Consulta não existe para ser atualizada"}, 404

        return jsonify({
            "id_consulta": consulta[0],
            "id_paciente": consulta[1],
            "id_medico": consulta[2],
            "dt_hora": str(consulta[3]),
            "tp_consulta": consulta[4],
            "st_confirmacao": status
        }), 200

    except Exception as erro:
        traceback.print_exc()
        return {"erro": "Erro ao atualizar consulta"}, 400
    
@app.route("/pacientes", methods=['GET'])
@cross_origin()
def recupera_paciente():
    try:
        pacientes = banco.consultar_paciente()  
        lista_pacientes = [
            {
                "id_paciente": p[0],
                "nm_paciente": p[1],
                "nm_email": p[2]
            }
            for p in pacientes
        ]
        return jsonify(lista_pacientes), 200
    except Exception as erro:
        traceback.print_exc()
        return {"erro": "Erro na consulta de pacientes"}, 400

app.run(debug=True)