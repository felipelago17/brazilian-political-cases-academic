"""
Brazilian Political Cases – Academic Tracker
Status as of 31 October 2026

Independent compilation of publicly reported legal cases involving major Brazilian political figures.
Every entry includes independent public source link(s) and notes on official-decision availability.
Not legal advice. Presumption of innocence applies to all allegations and investigations.
"""

TRACKER = {
    "meta": {
        "title": "Brazilian Political Cases – Academic Tracker",
        "status_date": "31 October 2026",
        "disclaimer": "Allegations and investigations are not findings of guilt. Not legal advice.",
        "methodology": "Sources limited to mainstream press, legal outlets, Agência Brasil, official court/government sites, and US DOJ/Treasury. Partisan outlets excluded."
    },
    "lula_family": [
        {
            "case": "Guarujá triplex",
            "persons": "Lula",
            "origin": "Lava Jato (Curitiba)",
            "allegation": "Bribery and money laundering via OAS beach apartment; STJ fixed reparation at R$2.42m",
            "history": "Convicted (2017); upheld by TRF-4 (2018); annulled by STF (2021)",
            "status": "Closed – archived Jan 2022",
            "mechanism": "1) STF (Fachin, Mar 2021): Curitiba 13th Federal Court lacked jurisdiction. 2) STF 2nd Panel: Moro found biased. 3) Case restarted in Brasília; archived on prescription (halved for age over 70).",
            "sources": "https://gazetasp.com.br/politica/lula-x-flavio-bolsonaro-e-seus-processos-na-justica-dois-candidatos-a-presidencia-zero-julgamento-de-merito ; https://www.opovo.com.br/agencia/bbc/2026/10/22/lulinha-luchsinger-e-lava-jato-o-que-realmente-pesa-contra-lula.html",
            "official_availability": "Public court record – not reproduced",
            "portal": "https://portal.stf.jus.br/processos/",
            "why_not_linked": "Judgments are public but Brazilian court portals generate session-based links. Retrieve by case number or party name via 'consulta processual'."
        },
        {
            "case": "Atibaia country house",
            "persons": "Lula",
            "origin": "Lava Jato (Curitiba)",
            "allegation": "Bribery and money laundering; ~R$1m in refurbishments paid by construction firms",
            "history": "Convicted (2019); annulled by STF (2021)",
            "status": "Closed",
            "mechanism": "Same jurisdiction ruling and extension of Moro bias finding; charges rejected in Brasília; TRF-1 refused reopening (Jul 2025); time limit expired.",
            "sources": "https://gazetasp.com.br/politica/lula-x-flavio-bolsonaro-e-seus-processos-na-justica-dois-candidatos-a-presidencia-zero-julgamento-de-merito ; https://www.opovo.com.br/agencia/bbc/2026/10/22/lulinha-luchsinger-e-lava-jato-o-que-realmente-pesa-contra-lula.html",
            "official_availability": "Public court record – not reproduced",
            "portal": "https://portal.stf.jus.br/processos/",
            "why_not_linked": "Judgments are public but Brazilian court portals generate session-based links. Retrieve by case number or party name via 'consulta processual'."
        },
        {
            "case": "Instituto Lula land",
            "persons": "Lula",
            "origin": "Lava Jato (Curitiba)",
            "allegation": "Odebrecht bribe via land for the Institute (~R$12m)",
            "history": "Never reached judgment",
            "status": "Closed – 17 Feb 2023",
            "mechanism": "Annulled with Curitiba cases; closed by STF Justice Lewandowski because Odebrecht leniency-deal evidence was declared unusable.",
            "sources": "https://gazetasp.com.br/politica/lula-x-flavio-bolsonaro-e-seus-processos-na-justica-dois-candidatos-a-presidencia-zero-julgamento-de-merito",
            "official_availability": "Public court record – not reproduced",
            "portal": "https://portal.stf.jus.br/processos/",
            "why_not_linked": "Lewandowski decision of 17 Feb 2023. Retrieve via consulta processual."
        },
        {
            "case": "Instituto Lula donations",
            "persons": "Lula",
            "origin": "Lava Jato (Curitiba)",
            "allegation": "Odebrecht donations as disguised bribes (~R$4m)",
            "history": "Never reached judgment",
            "status": "Closed – 17 Feb 2023",
            "mechanism": "Same as above: Odebrecht leniency evidence declared unusable.",
            "sources": "https://gazetasp.com.br/politica/lula-x-flavio-bolsonaro-e-seus-processos-na-justica-dois-candidatos-a-presidencia-zero-julgamento-de-merito",
            "official_availability": "Public court record – not reproduced",
            "portal": "https://portal.stf.jus.br/processos/",
            "why_not_linked": "Same decision as above. Retrieve via consulta processual."
        },
        {
            "case": "Obstruction of justice (Cerveró / Delcídio)",
            "persons": "Lula + 6",
            "origin": "Lava Jato (Brasília)",
            "allegation": "Scheme to buy silence of ex-Petrobras director Nestor Cerveró",
            "history": "Acquitted on merits – 12 Jul 2018",
            "status": "Closed",
            "mechanism": "Judge Ricardo Leite: insufficient evidence; case rested only on cooperating witnesses. Prosecutors themselves requested acquittal.",
            "sources": "https://www.migalhas.com.br/quentes/283634/justica-absolve-envolvidos-no-caso-cervero ; https://oantagonista.com.br/brasil/urgente-juiz-absolve-lula-e-demais-por-obstrucao-no-caso-delcidio/",
            "official_availability": "Public court record – not reproduced",
            "portal": "https://portal.trf1.jus.br/",
            "why_not_linked": "Sentence of 12 Jul 2018, 10th Federal Criminal Court of the Federal District. Retrieve via consulta processual."
        }
        # Additional cases (Mapa da Mina, INSS inquiries, Sindnapi, etc.) follow the same structure.
        # Full expanded list can be added in subsequent commits.
    ],
    "bolsonaro_family": [
        {
            "case": "Coup plot (AP 2668)",
            "persons": "Jair Bolsonaro + 7 co-defendants",
            "court": "STF First Panel",
            "allegation": "Attempted coup, violent abolition of the democratic rule of law, armed criminal organisation",
            "history": "Convicted 11 Sep 2025 (4–1) to 27 years 3 months. Humanitarian house arrest granted 24 Mar 2026.",
            "status": "Serving sentence in humanitarian house arrest. Criminal-review petitions pending.",
            "mechanism": "Merits conviction; review (revisão criminal) pending",
            "sources": "https://www.gazetadopovo.com.br/republica/pgr-se-manifesta-contra-revisao-criminal-de-bolsonaro/ ; https://conjur.com.br/2026-out-02/defesa-cita-novos-fatos-e-pede-revisao-da-condenacao-de-bolsonaro/",
            "official_availability": "Public court record – not reproduced",
            "portal": "https://portal.stf.jus.br/processos/",
            "why_not_linked": "AP 2668 judgment is public. Retrieve by case number via consulta processual."
        },
        {
            "case": "Coercion in the course of proceedings (AP 2782)",
            "persons": "Eduardo Bolsonaro",
            "court": "STF First Panel",
            "allegation": "Used office as federal deputy to seek US sanctions against Brazilian authorities",
            "history": "Unanimous conviction (Jun 2026): 4 years 2 months. Final 3 Oct 2026. Arrest warrant issued 8 Oct 2026.",
            "status": "Convicted – warrant outstanding; living in the US since Feb 2025",
            "mechanism": "Merits conviction",
            "sources": "https://www.poder360.com.br/poder-justica/eduardo-bolsonaro-ja-consta-em-banco-de-mandados-de-prisao-abertos/ ; https://agenciabrasil.ebc.com.br/justica/noticia/2026-10/moraes-determina-emissao-de-mandado-de-prisao-contra-eduardo-bolsonaro",
            "official_availability": "Public court record – not reproduced",
            "portal": "https://portal.stf.jus.br/processos/",
            "why_not_linked": "AP 2782 judgment published. Retrieve via consulta processual."
        }
        # Additional Bolsonaro family cases follow the same structure.
    ],
    "alexandre_de_moraes": [
        # Structured entries for Banco Master, wife's contracts, US sanctions, impeachment requests, etc.
    ],
    "legal_mechanisms": [
        {
            "mechanism": "Lack of jurisdiction (incompetência)",
            "meaning": "Court that judged the case had no authority over it; acts annulled and case restarts elsewhere",
            "cases": "Triplex, Atibaia, Instituto Lula cases",
            "sources": "https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689.htm (CPP)"
        },
        {
            "mechanism": "Judicial bias (suspeição)",
            "meaning": "Judge found partial; his decisions and evidence they produced are void",
            "cases": "Triplex (extended to Atibaia); derivative effect on Guinea, Mapa da Mina",
            "sources": "https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689.htm (CPP Art. 254)"
        }
        # Remaining mechanisms follow the same structure.
    ]
}

def summary():
    print("Brazilian Political Cases – Academic Tracker")
    print(f"Status: {TRACKER['meta']['status_date']}")
    print(f"Sections: {list(TRACKER.keys())}")

if __name__ == "__main__":
    summary()
