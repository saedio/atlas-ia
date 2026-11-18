
from app.tools.ibge import buscar_municipio, normalizar_texto
from app.tools.geocoding import buscar_localidade


def filtrar_correspondencia_exata(
    resultados: list,
    nome: str,
    campo_nome: str
) -> list:
    """
    Prioriza resultados cujo nome corresponde exatamente
    à localidade pesquisada.
    """

    nome_pesquisado = normalizar_texto(nome)

    correspondencias = [
        resultado
        for resultado in resultados
        if normalizar_texto(
            resultado.get(campo_nome, "")
        ) == nome_pesquisado
    ]

    return correspondencias if correspondencias else resultados


def filtrar_por_estado(
    localidades: list,
    estado: str
) -> list:
    """
    Filtra localidades conforme o estado informado.
    """

    estado_normalizado = normalizar_texto(estado)

    correspondencias = [
        localidade
        for localidade in localidades
        if normalizar_texto(
            localidade.get("admin1", "")
        ) == estado_normalizado
    ]

    return correspondencias if correspondencias else localidades


def consultar_localizacao(nome: str, necessidade: str) -> dict:
    """
    Consulta fontes geográficas conforme a necessidade.
    """

    if not nome or not nome.strip():
        raise ValueError(
            "O nome da localidade não pode estar vazio."
        )

    if necessidade == "ibge":

        resultados = buscar_municipio(nome)

        resultados = filtrar_correspondencia_exata(
            resultados,
            nome,
            "nome"
        )

        return {
            "fonte": "IBGE",
            "quantidade": len(resultados),
            "resultados": resultados
        }

    elif necessidade == "coordenadas":

        resultados = buscar_localidade(nome)

        resultados = filtrar_correspondencia_exata(
            resultados,
            nome,
            "name"
        )

        return {
            "fonte": "Open-Meteo",
            "quantidade": len(resultados),
            "resultados": resultados
        }

    elif necessidade == "completa":

        municipios = buscar_municipio(nome)
        localidades = buscar_localidade(nome)

        municipios = filtrar_correspondencia_exata(
            municipios,
            nome,
            "nome"
        )

        localidades = filtrar_correspondencia_exata(
            localidades,
            nome,
            "name"
        )

        # Identifica o estado por meio dos dados do IBGE.
        if len(municipios) == 1:

            estado = (
                municipios[0]
                .get("microrregiao", {})
                .get("mesorregiao", {})
                .get("UF", {})
                .get("nome")
            )

            if estado:
                localidades = filtrar_por_estado(
                    localidades,
                    estado
                )

        return {
            "fontes": ["IBGE", "Open-Meteo"],
            "ibge": municipios,
            "geocoding": localidades
        }

    else:
        raise ValueError(
            "Necessidade de consulta inválida."
        )
