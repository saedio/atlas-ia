
from app.agent.intent_classifier import classificar_intencao
from app.services.location_service import consultar_localizacao


def executar_agente(pergunta: str) -> dict:
    """
    Interpreta a pergunta e executa a ferramenta correspondente.
    """

    classificacao = classificar_intencao(pergunta)

    intencao = classificacao["intencao"]
    localidade = classificacao["localidade"]

    if intencao == "desconhecida":
        return {
            "sucesso": False,
            "mensagem": "Não consegui identificar o que você deseja consultar."
        }

    if not localidade:
        return {
            "sucesso": False,
            "mensagem": "Não consegui identificar a localidade da consulta."
        }

    resultado = consultar_localizacao(localidade, intencao)

    return {
        "sucesso": True,
        "intencao": intencao,
        "localidade": localidade,
        "dados": resultado
    }


if __name__ == "__main__":

    print("\n========== ATLAS AI ==========")
    print("       AGENTE INTELIGENTE")
    print("==============================")

    pergunta = input("\nComo posso ajudar? ")

    try:
        resposta = executar_agente(pergunta)

        print("\nResultado:")
        print(resposta)

    except ValueError as erro:
        print(f"\nErro: {erro}")
