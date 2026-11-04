---
layout: default
title: Inicio
---
[Home](./) · [English](cases.html) · [Português](cases_pt.html) · [Español](cases_es.html) · [Fork](https://github.com/felipelago17/brazilian-political-cases-academic/fork)

# Casos Políticos Brasileños – Rastreador Académico

**Español** · [English](./) · [Português](index_pt.html)

Compilación académica de casos jurídicos públicamente reportados que involucran a figuras políticas brasileñas destacadas.

**Estado al 31 de octubre de 2026**

## Propósito

Este repositorio documenta casos públicamente reportados para investigación y referencia académica. No está afiliado a ningún partido político, candidato, gobierno o autoridad judicial.

Cada entrada incluye:
- Al menos un enlace a una fuente pública independiente
- Notas sobre la disponibilidad de la decisión oficial del tribunal o del Ministerio Público

## Contenido

- [`tracker.py`](tracker.py) – Datos estructurados de los casos (fuente única de verdad)
- [Casos – Español](cases_es.html)
- [Cases – English](cases.html)
- [Casos – Português](cases_pt.html)

## Metodología

Fuentes limitadas a prensa mainstream, medios jurídicos, Agência Brasil, sitios oficiales de tribunales/gobierno/legislativo y US DOJ/Treasury. Se excluyen medios partidarios o abiertamente de campaña.

**Presunción de inocencia:** Las alegaciones e investigaciones no son hallazgos de culpabilidad. Esto no es asesoramiento jurídico.

## Proyectos de datos abiertos relacionados

Este rastreador registra **casos** (acusaciones, investigaciones, condenas). Proyectos brasileños de tecnología cívica complementarios miden **indicadores** a partir de datos gubernamentales abiertos y sirven como capa cuantitativa junto a las cronologías de los casos:

- [Operação Serenata de Amor](https://github.com/okfn-brasil/serenata-de-amor) (Open Knowledge Brasil, 2016–; MIT) — *Rosie*, un clasificador que asigna una puntuación de sospecha a cada reembolso de la cuota parlamentaria (CEAP), y *Jarbas*, la API/panel que publica los ítems señalados para validación ciudadana. El proyecto está en gran parte inactivo, pero el método — puntuación no supervisada de anomalías sobre datos oficiales de reembolso, publicada junto con el recibo — es el diseño de referencia para cualquier indicador de "irregularidad medible" aquí. Paquete complementario: [serenata-toolbox](https://github.com/okfn-brasil/serenata-toolbox).
- [Querido Diário](https://github.com/okfn-brasil/querido-diario) (Open Knowledge Brasil; activo) — recopila e indexa diarios oficiales municipales; fuente viva para avisos de licitación y nombramientos.
- [FiscalizaJá — Dados Abertos](https://github.com/FiscalizaJa/dadosabertos) (2023–) — normaliza los datos de cuotas de la Cámara y el Senado en un único esquema.

Los indicadores de estas fuentes se reportarían por separado de las entradas de casos y nunca se leerían como prueba de culpabilidad.

## Colaboración open source

Este repositorio está abierto a contribuciones. Haz un fork, realiza tus cambios y abre un pull request.

[Hacer fork del repositorio](https://github.com/felipelago17/brazilian-political-cases-academic/fork)

## Aviso

Este repositorio es solo para fines educativos e informativos. Verifica siempre con las fuentes primarias. Licencia: [CC BY 4.0](LICENSE).
