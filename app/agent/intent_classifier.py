
import re


def classificar_intencao(pergunta: str) -> dict:
    """
    Identifica a intenção do usuário e extrai a localidade.
    """

    pergunta_original = pergunta.strip()

    if not pergunta_original:
        raise ValueError("A pergunta não pode estar vazia.")

    pergunta = pergunta_original.casefold()

    palavras_ibge = [
        "ibge",
        "código do município",
        "codigo do municipio",
        "código ibge",
        "codigo ibge",
        "código municipal"
    ]

    palavras_coordenadas = [
        "coordenadas",
        "latitude",
        "longitude",
        "localização geográfica",
        "localizacao geografica"
    ]

    palavras_completas = [
        "informações completas",
        "informacoes completas",
        "dados completos",
        "todas as informações",
        "todas as informacoes"
    ]

    if any(palavra in pergunta for palavra in palavras_completas):
        intencao = "completa"

    elif any(palavra in pergunta for palavra in palavras_coordenadas):
        intencao = "coordenadas"

    elif any(palavra in pergunta for palavra in palavras_ibge):
        intencao = "ibge"

    else:
        intencao = "desconhecida"

    partes = re.split(
        r"\b(?:de|do|da|em|para|sobre)\s+",
        pergunta_original,
        flags=re.IGNORECASE
    )

    localidade = partes[-1].strip(" ?!.,") if len(partes) > 1 else None

    return {
        "intencao": intencao,
        "localidade": localidade,
        "pergunta_original": pergunta_original
    }
