---
layout: default
title: Início
---
[Home](./) · [English](cases.html) · [Português](cases_pt.html) · [Español](cases_es.html) · [Fork](https://github.com/felipelago17/brazilian-political-cases-academic/fork)

# Casos Políticos Brasileiros – Rastreador Acadêmico

**Português** · [English](./) · [Español](index_es.html)

Compilação acadêmica de casos jurídicos publicamente relatados envolvendo figuras políticas brasileiras de destaque.

**Status em 31 de outubro de 2026**

## Propósito

Este repositório documenta casos publicamente relatados para pesquisa e referência acadêmica. Não está afiliado a nenhum partido político, candidato, governo ou autoridade judicial.

Cada entrada inclui:
- Pelo menos um link de fonte pública independente
- Notas sobre a disponibilidade da decisão oficial do tribunal ou do Ministério Público

## Conteúdo

- [`tracker.py`](tracker.py) – Dados estruturados dos casos (fonte única de verdade)
- [Casos – Português](cases_pt.html)
- [Cases – English](cases.html)
- [Casos – Español](cases_es.html)

## Metodologia

Fontes limitadas à imprensa mainstream, veículos jurídicos, Agência Brasil, sites oficiais de tribunais/governo/legislativo e US DOJ/Treasury. Veículos partidários ou abertamente de campanha são excluídos.

**Presunção de inocência:** Alegações e investigações não são constatações de culpa. Isto não é aconselhamento jurídico.

## Projetos de dados abertos relacionados

Este rastreador registra **casos** (acusações, investigações, condenações). Projetos brasileiros de tecnologia cívica complementares medem **indicadores** a partir de dados governamentais abertos e servem como camada quantitativa ao lado das linhas do tempo dos casos:

- [Operação Serenata de Amor](https://github.com/okfn-brasil/serenata-de-amor) (Open Knowledge Brasil, 2016–; MIT) — a *Rosie*, classificadora que atribui uma pontuação de suspeita a cada reembolso da Cota para Exercício da Atividade Parlamentar (CEAP), e o *Jarbas*, API/painel que publica os itens sinalizados para validação cidadã. O projeto está em grande parte inativo, mas o método — pontuação não supervisionada de anomalias sobre dados oficiais de reembolso, publicada junto com o recibo — é o desenho de referência para qualquer indicador de "irregularidade mensurável" aqui. Pacote complementar: [serenata-toolbox](https://github.com/okfn-brasil/serenata-toolbox).
- [Querido Diário](https://github.com/okfn-brasil/querido-diario) (Open Knowledge Brasil; ativo) — coleta e indexa diários oficiais municipais; fonte viva para avisos de licitação e nomeações.
- [FiscalizaJá — Dados Abertos](https://github.com/FiscalizaJa/dadosabertos) (2023–) — padroniza os dados de cotas da Câmara e do Senado em um único esquema.

Indicadores dessas fontes seriam reportados separadamente das entradas de casos e nunca lidos como prova de culpa.

## Colaboração open source

Este repositório está aberto a contribuições. Faça um fork, altere e abra um pull request.

[Fazer fork do repositório](https://github.com/felipelago17/brazilian-political-cases-academic/fork)

## Aviso

Este repositório tem fins exclusivamente educacionais e informativos. Sempre verifique nas fontes primárias. Licença: [CC BY 4.0](LICENSE).
