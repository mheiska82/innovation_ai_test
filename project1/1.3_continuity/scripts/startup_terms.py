"""Start-up-era terms in the ten coded programmes, AN2008 and four Council documents (Project 1.3).

Counts Finnish stems per document in data/text/<ID>.txt (whole text), as raw
mentions and per 10,000 words, and keeps up to three example passages per
term. Writes project1/1.3_continuity/data/startup_terms.csv and
startup_terms_examples.csv.
"""
import csv, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DOCS = [('GP64', 1987), ('GP65', 1991), ('GP66', 1995), ('GP67', 1999), ('GP68', 2003), ('GP70', 2007),
        ('AN2008', 2008), ('GP72', 2011), ('GP74', 2015), ('GP75', 2019), ('GP77', 2023),
        # Research and Innovation Council documents counted in Project 2 (RC2010 is a corpus gap)
        ('RC2014', 2014), ('RC2017', 2017), ('RC2024', 2024), ('RC2026', 2026)]
TERMS = {
    'innovation_system': r'innovaatiojärjestelm',
    'ecosystem': r'ekosysteem',  # ecological senses removed by EXCLUDE below
    'growth_firm': r'kasvuyrit|kasvuhakui',
    'start_up': r'start.?up|startup',
    'venture_capital': r'(?<!osake)pääomasijoit|riskirahoit|riskisijoit|riskipääom',
    'incubator_accelerator': r'yrityshautomo|(?<!ajatus)hautomotoimin|kiihdyttämö',
    'commercialisation': r'kaupallist',
}
# A match is dropped when the 80 characters around it show an ecological sense.
EXCLUDE = {'ecosystem': r'ekosysteemipal|luonno|monimuotoi|ekosysteemin toi|vesistö|metsäekosysteem|meriekosysteem'}
OUT = ROOT / 'project1/1.3_continuity/data'


def main():
    rows, ex = [], []
    for doc, year in DOCS:
        text = (ROOT / 'data/text' / f'{doc}.txt').read_text(encoding='utf-8')
        text = re.sub(r'-\n(?=[a-zäö])', '', text)   # rejoin hyphenated line breaks
        flat = re.sub(r'\s+', ' ', text)
        low = flat.lower()
        words = len(re.findall(r'\w+', flat))
        row = {'document_id': doc, 'year': year, 'words': words}
        for k, p in TERMS.items():
            ms = [m for m in re.finditer(p, low)
                  if not (k in EXCLUDE and re.search(EXCLUDE[k], low[max(0, m.start() - 80):m.end() + 80]))]
            row[k] = len(ms)
            row[k + '_per10k'] = round(10000 * len(ms) / words, 2)
            for m in ms[:3]:
                a, b = max(0, m.start() - 90), min(len(flat), m.end() + 90)
                ex.append({'document_id': doc, 'year': year, 'term': k, 'passage': flat[a:b]})
        rows.append(row)
    with open(OUT / 'startup_terms.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    with open(OUT / 'startup_terms_examples.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(ex[0].keys())); w.writeheader(); w.writerows(ex)
    for r in rows:
        print(r['document_id'], r['year'], r['words'], *[r[k] for k in TERMS])


if __name__ == '__main__':
    main()
