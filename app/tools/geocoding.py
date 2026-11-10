
import httpx

BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"


def buscar_localidade(nome: str) -> list[dict]:
    """Pesquisa uma cidade e retorna suas coordenadas."""

    parametros = {
        "name": nome,
        "count": 5,
        "language": "pt",
        "countryCode": "BR"
    }

    try:
        resposta = httpx.get(
            BASE_URL,
            params=parametros,
            timeout=15.0
        )

        resposta.raise_for_status()

        dados = resposta.json()

        return dados.get("results", [])

    except httpx.TimeoutException:
        print("Erro: tempo limite da consulta excedido.")

    except httpx.HTTPStatusError as erro:
        print(f"Erro HTTP: {erro.response.status_code}")

    except httpx.RequestError as erro:
        print(f"Erro de conexão: {erro}")

    return []


if __name__ == "__main__":

    print("\n========== ATLAS AI ==========")
    print("     BUSCA DE LOCALIDADES")
    print("==============================")

    cidade = input("\nDigite o nome da cidade: ").strip()

    if not cidade:
        print("Digite um nome válido.")
    else:
        resultados = buscar_localidade(cidade)

        if resultados:
            print(f"\nLocalidades encontradas: {len(resultados)}\n")

            for localidade in resultados:
                print(f"Cidade: {localidade['name']}")
                print(f"Estado: {localidade.get('admin1', 'Não informado')}")
                print(f"País: {localidade.get('country', 'Não informado')}")
                print(f"Latitude: {localidade['latitude']}")
                print(f"Longitude: {localidade['longitude']}")
                print("-" * 40)

        else:
            print("\nNenhuma localidade encontrada.")
