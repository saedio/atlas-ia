
import httpx
import unicodedata

BASE_URL = "https://servicodados.ibge.gov.br/api/v1/localidades"


def normalizar_texto(texto: str) -> str:
    """Remove acentos e padroniza o texto."""

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto.strip().casefold()


def consultar_municipios() -> list:
    """Consulta os municípios na API do IBGE."""

    endpoint = f"{BASE_URL}/municipios"

    try:
        resposta = httpx.get(
            endpoint,
            params={"orderBy": "nome"},
            timeout=15.0
        )

        resposta.raise_for_status()

        return resposta.json()

    except httpx.TimeoutException:
        print("Erro: tempo limite excedido.")

    except httpx.HTTPStatusError as erro:
        print(f"Erro HTTP: {erro.response.status_code}")

    except httpx.RequestError as erro:
        print(f"Erro de conexão: {erro}")

    return []


def buscar_municipio(nome: str) -> list:
    """Pesquisa municípios pelo nome."""

    if not nome.strip():
        return []

    municipios = consultar_municipios()

    pesquisa = normalizar_texto(nome)

    resultados = []

    for municipio in municipios:

        nome_municipio = normalizar_texto(
            municipio["nome"]
        )

        if pesquisa in nome_municipio:
            resultados.append(municipio)

    return resultados


if __name__ == "__main__":

    print("\n========== ATLAS AI ==========")
    print("       CONSULTA IBGE")
    print("==============================")

    pesquisa = input("\nDigite o município: ")

    resultados = buscar_municipio(pesquisa)

    if resultados:

        print(f"\nResultados encontrados: {len(resultados)}\n")

        for municipio in resultados:

            print(f"Município: {municipio['nome']}")
            print(f"Código IBGE: {municipio['id']}")
            print("-" * 35)

    else:

        print("\nNenhum município encontrado.")
