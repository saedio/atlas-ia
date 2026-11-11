
from app.services import location_service


def test_consulta_ibge(monkeypatch):
    """Verifica se a consulta utiliza somente o IBGE."""

    def fake_ibge(nome):
        return [{"nome": "São Paulo", "id": 3550308}]

    def fake_geocoding(nome):
        raise AssertionError("Open-Meteo não deveria ser chamado")

    monkeypatch.setattr(
        location_service, "buscar_municipio", fake_ibge
    )
    monkeypatch.setattr(
        location_service, "buscar_localidade", fake_geocoding
    )

    resultado = location_service.consultar_localizacao(
        "São Paulo", "ibge"
    )

    assert resultado["fonte"] == "IBGE"
    assert resultado["quantidade"] == 1


def test_consulta_coordenadas(monkeypatch):
    """Verifica se a consulta utiliza somente o Open-Meteo."""

    def fake_ibge(nome):
        raise AssertionError("IBGE não deveria ser chamado")

    def fake_geocoding(nome):
        return [{"name": "São Paulo", "latitude": -23.54}]

    monkeypatch.setattr(
        location_service, "buscar_municipio", fake_ibge
    )
    monkeypatch.setattr(
        location_service, "buscar_localidade", fake_geocoding
    )

    resultado = location_service.consultar_localizacao(
        "São Paulo", "coordenadas"
    )

    assert resultado["fonte"] == "Open-Meteo"
    assert resultado["quantidade"] == 1


def test_consulta_completa(monkeypatch):
    """Verifica se as duas fontes são consultadas."""

    monkeypatch.setattr(
        location_service,
        "buscar_municipio",
        lambda nome: [{"nome": "São Paulo", "id": 3550308}]
    )

    monkeypatch.setattr(
        location_service,
        "buscar_localidade",
        lambda nome: [{"name": "São Paulo", "latitude": -23.54}]
    )

    resultado = location_service.consultar_localizacao(
        "São Paulo", "completa"
    )

    assert len(resultado["ibge"]) == 1
    assert len(resultado["geocoding"]) == 1


def test_nome_vazio():
    """Verifica se nomes vazios são rejeitados."""

    try:
        location_service.consultar_localizacao("", "ibge")
        assert False, "Deveria gerar ValueError"
    except ValueError:
        assert True


def test_necessidade_invalida():
    """Verifica se necessidades desconhecidas são rejeitadas."""

    try:
        location_service.consultar_localizacao(
            "São Paulo", "invalida"
        )
        assert False, "Deveria gerar ValueError"
    except ValueError:
        assert True
