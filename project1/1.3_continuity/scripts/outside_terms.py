"""Start-up-era terms in the English outside evaluations (Project 1.3).

EV2009P and EV2009F (the 2009 international evaluation), OE2017 (OECD
innovation policy review) and OE2022 (OECD Economic Survey, chapter 2
"Rebooting the innovation ecosystems", PDF pages 71-120 only). English stems,
mentions per 10,000 words. Writes data/outside_terms.csv and
data/outside_terms_examples.csv.
"""
import csv, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'project1/1.3_continuity/data'
DOCS = [('EV2009P', 2009, None), ('EV2009F', 2009, None), ('OE2017', 2017, None), ('OE2022', 2022, (71, 120))]
TERMS = {
    'innovation_system': r'innovation systems?\b',
    'ecosystem': r'ecosystem',
    'start_up': r'start-?ups?\b|startups?\b',
    'growth_firm': r'high-growth|growth firms?|growth compan|growth-oriented|growth entrepreneur|hgefs?\b',
    'venture_capital': r'venture capital|risk capital',
    'incubator_accelerator': r'incubat|accelerator',
    'commercialisation': r'commerciali[sz]',
}


def pages(text, rng):
    parts = re.split(r'\[\[page (\d+)\]\]', text)
    keep = [parts[i + 1] for i in range(1, len(parts), 2) if not rng or rng[0] <= int(parts[i]) <= rng[1]]
    return ' '.join(keep)


def main():
    rows, ex = [], []
    for doc, year, rng in DOCS:
        text = pages((ROOT / 'data/text' / f'{doc}.txt').read_text(encoding='utf-8'), rng)
        flat = re.sub(r'\s+', ' ', re.sub(r'-\n(?=[a-z])', '', text))
        low = flat.lower()
        words = len(re.findall(r'\w+', flat))
        row = {'document_id': doc, 'year': year, 'pages': f'{rng[0]}-{rng[1]}' if rng else 'all', 'words': words}
        for k, p in TERMS.items():
            ms = list(re.finditer(p, low))
            row[k] = len(ms)
            row[k + '_per10k'] = round(10000 * len(ms) / words, 2)
            for m in ms[:3]:
                ex.append({'document_id': doc, 'term': k, 'passage': flat[max(0, m.start() - 90):m.end() + 90]})
        rows.append(row)
    for name, data in (('outside_terms.csv', rows), ('outside_terms_examples.csv', ex)):
        with open(OUT / name, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=list(data[0].keys())); w.writeheader(); w.writerows(data)
    for r in rows:
        print(r['document_id'], r['words'], *[f"{k}={r[k]}({r[k + '_per10k']})" for k in TERMS])


if __name__ == '__main__':
    main()
