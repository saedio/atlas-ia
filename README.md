# ATLAS AI

**Projeto de IA com Python e APIs publicas com dados reais do IBGE.**

Agente inteligente que pesquisa, consulta, interpreta e correlaciona dados públicos usando Python e APIs externas, direto do terminal.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

---

## Sobre o projeto

O ATLAS AI recebe perguntas em linguagem natural, identifica qual informação foi pedida, escolhe a API pública adequada, consulta os dados reais e devolve uma resposta clara, sempre indicando a fonte.

Exemplos de perguntas:

```text
> Qual é a população de São Paulo?
> Como está o clima hoje em São Paulo?
> Qual é o PIB do estado de São Paulo?
> Consulte informações sobre o município de Campinas.
> Compare a população de São Paulo com a do Rio de Janeiro.
> Pesquise informações sobre o Japão.
```

## Diferencial

**Nenhuma resposta é inventada.**

O Atlas separa explicitamente:

- **Dados consultados:** retornados por uma API, com fonte e data da consulta.
- **Dados não encontrados:** informados como indisponíveis, sem estimativas ou suposições.

Se a API falhar, não retornar o dado ou a pergunta for ambígua, o agente informa isso em vez de preencher a lacuna.

## Como funciona

1. **Interpreta** a pergunta em linguagem natural.
2. **Identifica** qual informação está sendo solicitada (entidade, localidade, indicador).
3. **Escolhe** a API pública adequada.
4. **Requisita** os dados via HTTP.
5. **Trata e organiza** a resposta recebida.
6. **Interpreta** os resultados (comparações, correlações).
7. **Responde** de forma compreensível, citando a fonte.

```text
Pergunta ──► Interpretação ──► Roteador de APIs ──► Requisição HTTP
                                                          │
Resposta + fontes ◄── Interpretação dos dados ◄── Tratamento
```

## Funcionalidades

- Consulta de população de cidades, estados e países
- Consulta de clima atual por localidade
- Consulta de indicadores econômicos (ex.: PIB estadual)
- Informações sobre municípios brasileiros
- Informações gerais sobre países
- Comparação entre duas ou mais localidades
- Citação obrigatória da fonte em toda resposta
- Distinção explícita entre dado consultado e dado não encontrado

## Fontes de dados

| Domínio | API pública (planejada) |
|---|---|
| Municípios, estados, população, PIB | IBGE (API de Dados Agregados e Localidades) |
| Clima | Open-Meteo |
| Países | REST Countries |

> A lista pode mudar conforme o desenvolvimento.

## Tecnologias

- Python 3.10+
- `requests` para chamadas HTTP
- APIs públicas externas
- Camada de interpretação de linguagem natural (a definir)

## Instalação

```bash
git clone
