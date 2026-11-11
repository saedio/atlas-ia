
from app.tools.ibge import buscar_municipio
from app.tools.geocoding import buscar_localidade


def consultar_localizacao(nome: str, necessidade: str) -> dict:
    """
    Consulta fontes geográficas conforme a necessidade.
    """

    if not nome.strip():
        raise ValueError("O nome da localidade não pode estar vazio.")

    if necessidade == "ibge":

        resultados = buscar_municipio(nome)

        return {
            "fonte": "IBGE",
            "quantidade": len(resultados),
            "resultados": resultados
        }

    elif necessidade == "coordenadas":

        resultados = buscar_localidade(nome)

        return {
            "fonte": "Open-Meteo",
            "quantidade": len(resultados),
            "resultados": resultados
        }

    elif necessidade == "completa":

        municipios = buscar_municipio(nome)
        localidades = buscar_localidade(nome)

        return {
            "fontes": ["IBGE", "Open-Meteo"],
            "ibge": municipios,
            "geocoding": localidades
        }

    else:
        raise ValueError("Necessidade de consulta inválida.")
