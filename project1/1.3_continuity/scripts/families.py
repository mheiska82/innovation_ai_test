"""Mechanism families in Finnish claim excerpts (Project 1.3 continuity test).

Reads project1/1.2_paradigms/coding/claims_v0.4.csv, keeps core claims from
Finnish-language documents, and marks which growth-route families each
verbatim excerpt names, using Finnish word stems. Writes
data/claim_families.csv (one row per claim) and data/family_shares.csv.
"""
import csv, re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CLAIMS = ROOT / 'project1/1.2_paradigms/coding/claims_v0.4.csv'
OUT = Path(__file__).resolve().parents[1] / 'data'

FAMILIES = {
    # knowledge, research, technology (the 1990s route)
    'K_knowledge': r'tutkimu|tutkimus|t&k|t & k|tki|tuotekehit|osaami|tietoyhteiskun|teknolog|tiede|tieteen|koulutu|innovaatiotoimin|innovaatiopanost|innovaatiorahoit|innovaatiojärjestelm',
    # networks, clusters, ecosystems
    'N_networks': r'verkost|verkottu|klust|ekosystee|keskittym|osaamiskeskus',
    # risk capital and growth finance
    'F_finance': r'pääomasijoit|riskisijoit|riskirahoit|pääomamarkkin|oman pääoman|kasvurahoit|sijoittaj|sijoitustoimin',
    # new and growth firms, start-ups (the start-up-era route)
    'G_growthfirms': r'kasvuyrit|kasvuhakui|aloittav|alkavien yritys|start.?up|nopean kasvun|yritysten perustami|uusien yritysten|yrityshautomo|kiihdyttämö|innovatiivisten pk-yritys|innovatiivista kasvuyrit|uutta liiketoimintaa|uuden liiketoiminnan',
    # entrepreneurship in general (enterprise culture, often with work and taxation)
    'E_entrepreneurship': r'yrittäj',
    # markets: commercialisation, internationalisation, demand
    'M_markets': r'kaupallist|tuotteist|kansainvälisty|kysyntä|markkinoil|markkinointi',
}
ERAS = [('1987–1999', 1987, 1999), ('2003–2011', 2003, 2011), ('2015–2023', 2015, 2023)]


def era(year):
    for name, a, b in ERAS:
        if a <= year <= b:
            return name
    return None


def main():
    rows = [r for r in csv.DictReader(open(CLAIMS, encoding='utf-8'))
            if r['weight'] == 'core' and r['document_id'] != 'EV2009P']  # EV2009P is in English
    out = []
    for r in rows:
        text = r['excerpt_verbatim'].lower()
        fam = {k: bool(re.search(p, text)) for k, p in FAMILIES.items()}
        hits = {k: sorted(set(m.group(0) for m in re.finditer(p, text))) for k, p in FAMILIES.items()}
        y = int(r['year'])
        out.append({'claim_id': r['claim_id'], 'document_id': r['document_id'], 'year': y, 'era': era(y),
                    'claim_type': r['claim_type'], **{k: int(v) for k, v in fam.items()},
                    'matched': '; '.join(f"{k}: {', '.join(v)}" for k, v in hits.items() if v),
                    'excerpt_verbatim': r['excerpt_verbatim']})
    OUT.mkdir(exist_ok=True)
    with open(OUT / 'claim_families.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
    # shares by era; and the bridge test: growth/finance claims with or without knowledge
    agg = defaultdict(lambda: defaultdict(int))
    for o in out:
        e = o['era']; a = agg[e]; a['core'] += 1
        for k in FAMILIES: a[k] += o[k]
        gf = o['G_growthfirms'] or o['F_finance']
        if gf:
            a['GF_any'] += 1
            a['GF_with_K'] += o['K_knowledge']
            a['GF_with_N'] += o['N_networks']
            a['GF_without_K_or_N'] += int(not o['K_knowledge'] and not o['N_networks'])
    with open(OUT / 'family_shares.csv', 'w', newline='', encoding='utf-8') as f:
        cols = ['era', 'core'] + [k for k in FAMILIES] + ['GF_any', 'GF_with_K', 'GF_with_N', 'GF_without_K_or_N']
        w = csv.writer(f); w.writerow(cols + [c + '_pct' for c in FAMILIES])
        for name, _, _ in ERAS:
            a = agg[name]
            w.writerow([name] + [a[c] for c in cols[1:]] + [round(100 * a[k] / a['core']) for k in FAMILIES])
    print(open(OUT / 'family_shares.csv').read())


if __name__ == '__main__':
    sys.exit(main())
