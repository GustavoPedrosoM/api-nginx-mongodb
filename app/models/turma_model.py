def turma_helper(turma) -> dict:
    return {
        "id": str(turma["_id"]),
        "nome": turma["nome"],
        "ano": turma["ano"],
        "turno": turma["turno"],
    }
