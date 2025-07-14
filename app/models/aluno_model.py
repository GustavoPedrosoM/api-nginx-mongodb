def aluno_helper(aluno) -> dict:
    return {
        "id": str(aluno["_id"]),
        "nome": aluno["nome"],
        "idade": aluno["idade"],
        "matricula": aluno["matricula"]
    }
