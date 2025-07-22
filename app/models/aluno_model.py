def aluno_helper(aluno, turma=None) -> dict:
    aluno_dict = {
        "id": str(aluno["_id"]),
        "nome": aluno["nome"],
        "idade": aluno["idade"],
        "matricula": aluno["matricula"],
        "turma_id": str(aluno["turma_id"]) if "turma_id" in aluno else None,
    }

    if turma:
        aluno_dict["turma"] = {
            "id": str(turma["_id"]),
            "nome": turma["nome"],
        }

    return aluno_dict