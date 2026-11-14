#!/usr/bin/env python3
"""Running tally of full pages wanted.

The owner (S-000-17, 13 Nov 2026): 'at the end I will backfill all full pages so
you can start noting what you want as a running tally'.

Most of this archive is single rows cut from register pages. This script lists
every such strip, ranks it, and says what the full page would settle. It writes
data/page_wants.json (for the front end and the other agents) and PAGE-TALLY.md
(to read). Run it after each batch: python3 tally.py

Derived: the list of strips, their rank, the hypotheses that cite them.
Hand-written, kept below: NOTES (what to look for), IN_HAND (strips whose page
has since arrived), NEVER_SEEN (pages this line needs and has in no form).
"""
import json, re, collections

L = lambda n: json.load(open(f'data/{n}.json'))

# Folders whose files are rows cut from a register page.
STRIP_FOLDERS = {'F-002': 'Baptisms, Čičarovce (Viszoka)', 'F-003': 'Baptisms, Belža Greek Catholic transcript',
                 'F-004': 'Baptisms, Čičarovce (Viszoka)', 'F-005': 'Baptisms, Iňačovce Greek Catholic',
                 'F-007': 'Baptisms, Iňačovce Reformed', 'F-008': 'Baptisms, Prešov Greek Catholic',
                 'F-009': 'Baptisms, Senné Roman Catholic', 'F-010': 'Baptisms, Staré', 'F-013': 'Burials'}
EXTRA = {'D-006-19': 'Passenger list', 'D-014-01': 'Passenger list', 'D-006-24': 'Baptisms, Senné Roman Catholic',
         'D-015-03': "Voters' list, Montréal", 'D-015-04': "Voters' list, Montréal"}   # strips filed outside the strip folders
SKIP = {'D-013-99', 'D-013-100', 'D-013-101'}                           # crops of a society's index, not register strips

# What the full page is expected to settle, by document. Written by hand.
NOTES = {
    'D-013-138': "The death of Ahn 32. The page number and entry number for the citation; the rows around it for other deaths in house 3.",
    'D-013-134': "The year (1873 is the owner's). Whether the entry or its neighbours name a son: he is the proposed father of Ahn 32 (H-085).",
    'D-013-165': "The year: the last digit reads 5 or 7. She is the proposed mother of Ahn 32 (H-085); her age of 31 dates her birth from it.",
    'D-013-148': "The year (1878 is the owner's). János of house 6, aged 80: the other old man of the house, and a test of who headed it (H-085, H-079).",
    'D-013-169': "The year (1879 is the owner's). A Duska born about 1799 who married out; a sister of the men of house 6 if the page says where she was born.",
    'D-013-105': "The child is entered as son of his grandparents (H-088). The page shows whether the priest made the same slip in other entries.",
    'D-013-120': "The year (1870 is the owner's) and whether the mother is named: decides whether Ahn 17 was given a dead sister's name (H-089).",
    'D-013-161': "Three strips of the 1840s run carry small dates under the names that do not match the owner's labels. The page headings give the true years.",
    'D-013-180': "As D-013-161: the year, from the page heading.",
    'D-013-155': "As D-013-161: the year, from the page heading.",
    'D-013-102': "Filed as Anna, reads Eva; D-013-129 is the reverse. The two pages show which label belongs to which burial of [1853], and the year.",
    'D-013-129': "See D-013-102.",
    'D-013-83': "The surname is doubtful on the strip. The page, or the same man in a neighbouring entry, would settle whether he is a Duska.",
    'D-013-97': "The year (1830 is the owner's) and the father's name, cut off on the strip: which Reformed Duska couple lost her (H-042, H-064).",
    'D-013-77': "Filed among the Duska deaths with no Duska on the strip. The page may show why: a husband named in the next column (H-082).",
    'D-007-08': "The row below the one kept: Mihály Duska, born at 'Bradenville'. The full row and the rows under it (R-010). A Duska born in America and baptised at home.",
    'D-013-15': "Filed as 1905, on a page layout of the 1830s. The year from the page heading (H-078). Routed to the Demko agent; asked as R-020.",
    'D-013-26': "Filed as 1888; house 121 points to the 1870s. The year from the page heading (H-077). Routed to the Demko agent; asked as R-020.",
    'D-009-23': "The baptism of Ahn 17. The year (1872 is the owner's), the page number and entry number.",
    'D-009-06': "The baptism of Ahn 16. The date is 'as above' on the strip: the entry above gives it. The year, page and entry number.",
    'D-009-10': "The first child of Ahn 32 and Anna Krak. The year (1866 is the owner's) bounds their marriage, which is not in hand.",
    'D-009-33': "A son of Ahn 32 and Anna Krak. The year (1872 is the owner's) fixes the order of their children, who run to August 1875 (H-052).",
    'D-013-36': "An infant Anna Krak buried at Jesztreb in [1848]. If the year stands she cannot be the wife of Ahn 32, which removes one candidate (H-050, H-055).",
    'D-010-01': "The Sztára baptism of an Anna Krak, January 1848. The mother's surname is doubtful; the page and the entries around it would fix it (H-055).",
    'D-006-19': "The heading of the passenger list: ship, port and date of sailing and landing. Settles Hamburg and 1930 (H-090) and dates the arrival of Ahn 8 (H-066).",
    'D-014-01': "The same list as D-006-19, a second crop. One heading serves both.",
    'D-015-03': "The heading of the page: the year, the electoral district and the street. All three now rest on the file name and on the house number.",
    'D-015-04': "The heading of the section the two rows stand in: the street. And the year and district from the top of the page (H-092).",
}
# Strips whose full page has arrived since: strip -> the page.
IN_HAND = {'D-009-79': 'D-014-07', 'D-009-84': 'D-014-09', 'D-006-24': 'D-014-09', 'D-009-01': 'D-014-02', 'D-009-16': 'D-014-04',
           'D-009-66': 'D-014-06', 'D-009-08': 'D-014-03', 'D-009-88': 'D-014-03', 'D-009-34': 'D-014-05', 'D-009-35': 'D-014-05', 'D-009-12': 'D-014-05', 'D-007-15': 'D-015-05', 'D-007-25': 'D-015-05'}
# Pages this line needs and has in no form. Noted, not asked: the owner sends deaths and marriages as folders of their own.
NEVER_SEEN = [
    {"what": "The passenger list of 1937, page 263: Maria Duska and her son Stephan", "where": "The lists of arrivals for 1937 that the typed index points to (D-015-02)", "settles": "The ship, port and day of their arrival, who they were going to and at what address; H-065 on its own record."},
    {"what": "Marriage of György Duska (Ahn 32) and Anna Krak, about 1864 to 1866", "where": "Senné Roman Catholic marriages, or the bride's Greek Catholic parish", "settles": "Which Anna Krak she is and who her parents were (Ahn 66 and 67); H-050, H-055."},
    {"what": "Burial of Anna Krak, wife of György Duska, between August 1875 and 1879", "where": "The Greek Catholic book that served Szenna; she is not among the Senné Roman Catholic strips", "settles": "Her age, so her birth year, and with it which Anna Krak she is; H-052, H-055."},
    {"what": "Marriage of Michal Duska and Maria Demko, 30 January 1927", "where": "Probably Iňačovce Greek Catholic marriages", "settles": "The ages and parents of Ahn 8 and Ahn 9 on one record; R-017."},
    {"what": "Baptism of Štefan Duska, the original entry: volume IV, page 110, entry 43 of 1929", "where": "Senné Roman Catholic baptisms", "settles": "His birthday, 21 or 23 October; R-018."},
    {"what": "Census of 1869, Senné (Szenna), house 6 and house 5", "where": "The 1869 census sheets for Ung county", "settles": "Who lived with whom in the house two György Duskas shared: H-085, H-079; R-014."},
    {"what": "Baptism of the András Duska born about December 1921", "where": "Senné Roman Catholic baptisms", "settles": "His true parents; H-088."},
    {"what": "Marriage of András Hankovcsák and Mária Nyemcsik, about 1890", "where": "Senné Roman Catholic marriages", "settles": "Her parents; H-086."},
    {"what": "Burial of Erzsébet Schwarz, wife of György Duska the younger, 1890 to 1900", "where": "Senné Roman Catholic burials", "settles": "Clears the way for his second marriage; H-087."},
    {"what": "Burial of András Duska, 22 August 1940", "where": "Senné Roman Catholic burials after 1925, later than the volume the strips come from", "settles": "The death of Ahn 16 on a record of its own; the date rests on a note beside his baptism (D-009-06)."},
]


def build():
    docs, hyps, people = L('documents'), L('hypotheses'), L('people')
    direct = {s for p in people if p.get('ahnentafel') for s in p.get('sources', [])}
    live = [h for h in hyps if h['status'] in ('open', 'supported')]
    htext = {h['id']: json.dumps(h, ensure_ascii=False) for h in live}
    out = []
    for d in docs:
        i = d['id']
        if i in SKIP: continue
        kind = EXTRA.get(i) or STRIP_FOLDERS.get(d['folder'])
        frm = d['entries'][0]['from'] if d.get('entries') else ''
        if d['folder'] == 'F-011' and 'names only' in frm: kind = 'Census sheet, names only'
        if not kind: continue
        if d['folder'] == 'F-013': kind = 'Burials, ' + {'Belza': 'Belža Greek Catholic', 'Cicarovce': 'Čičarovce', 'Senne - ROCA': 'Senné Roman Catholic'}.get(d.get('part', ''), d.get('part', '').replace('Inacovce', 'Iňačovce'))
        label_year = '[' in d['span'] or 'filed' in d['span'] or 'owner' in d['span']
        hs = sorted(h for h, t in htext.items() if re.search(re.escape(i) + r'(?!\d)', t) or re.search(re.escape(d['source']) + r'(?!\d)', t))
        want = ['the full sheet'] if kind.startswith('Census') else (['page heading: year and page number'] + (['the year as written on the page'] if label_year else []) + ['the rows above and below'])
        if i in ('D-006-19', 'D-014-01'): want = ['the heading of the list: ship, port, dates']
        on_line = d['source'] in direct
        if i in IN_HAND: rank = 0
        elif on_line or i in NOTES or (hs and d.get('route') == 'duska'): rank = 1
        elif d.get('route') == 'duska' and label_year: rank = 2
        else: rank = 3
        e = {"id": i, "file": d['file'], "folder": d['folder'], "register": kind, "date_on_file": d['span'], "title": d['title'], "route": d.get('route'),
             "rank": rank, "status": "in hand" if i in IN_HAND else "wanted", "want": want, "direct_line": on_line, "hypotheses": hs, "look_for": NOTES.get(i)}
        if i in IN_HAND: e['in_hand'] = IN_HAND[i]
        out.append(e)
    return out


def num(i): return [int(x) if x.isdigit() else x for x in re.split(r'[-]', i)]


def write(out):
    json.dump({"note": "Derived by tally.py from documents.json and hypotheses.json; look_for, in_hand and never_seen are hand-written in that script. Rank 1: a direct-line entry, or one an open hypothesis rests on. Rank 2: another Duska strip whose year is only in the owner's file name. Rank 3: the rest. Rank 0: the page is in hand.",
               "strips": out, "never_seen": NEVER_SEEN}, open('data/page_wants.json', 'w'), ensure_ascii=False, indent=1)
    c = collections.Counter(e['rank'] for e in out)
    md = ["# Full pages wanted: a running tally", "",
          "The owner said on 13 November 2026 that he will send the full register pages at the end, and to keep a running tally of what is wanted (statement `S-000-17`). This is the tally. It is rebuilt by `tally.py` after every batch; the same list is in `data/page_wants.json`.", "",
          "Nearly every record in this archive is one row cut from a page. A row keeps the names. It loses the page number, often the year, and the entries above and below it. The year on most strips is the one in the owner's file name, and at least eight of those have already proved wrong.", "",
          f"- **{c[1]}** strips are rank 1: a direct-line entry, or one an open hypothesis rests on.",
          f"- **{c[2]}** are rank 2: other Duska strips whose year is only in the file name.",
          f"- **{c[3]}** are rank 3: the rest, most of them routed to the Demko and Places agents, who will rank their own.",
          f"- **{c[0]}** are already covered by a full page that has arrived.",
          f"- **{len(NEVER_SEEN)}** pages are needed and have not been seen in any form (last table).", "",
          "## Rank 1: what each page would settle", "", "| Strip | The owner's file | Date on the strip | Rests on it | Look for |", "|---|---|---|---|---|"]
    r1 = sorted((e for e in out if e['rank'] == 1), key=lambda e: (e['look_for'] is None, not e['direct_line'], num(e['id'])))
    for e in r1:
        lf = e['look_for'] or '; '.join(e['want'])
        md.append(f"| `{e['id']}` | {e['file']} | {e['date_on_file']} | {'direct line; ' if e['direct_line'] else ''}{', '.join(e['hypotheses']) or '-'} | {lf} |")
    md += ["", "## Rank 2: Duska strips with the year from the file name only", "", "For each: the page heading with its year and page number, and the rows above and below.", ""]
    by = collections.defaultdict(list)
    for e in out:
        if e['rank'] == 2: by[e['register']].append(e)
    for k in sorted(by):
        md.append(f"**{k}** ({len(by[k])}): " + ', '.join(f"`{e['id']}` {e['date_on_file']}" for e in sorted(by[k], key=lambda e: num(e['id']))))
        md.append("")
    md += ["## Rank 3: the rest", "", "| Register | Strips | Routed to |", "|---|---|---|"]
    by = collections.defaultdict(list)
    for e in out:
        if e['rank'] == 3: by[e['register']].append(e)
    for k in sorted(by):
        rc = collections.Counter(e['route'] for e in by[k])
        md.append(f"| {k} | {len(by[k])} | {', '.join(f'{r} {n}' for r, n in sorted(rc.items()))} |")
    md += ["", "## Already in hand", "", "| Strip | Its full page |", "|---|---|"]
    for e in sorted((e for e in out if e['rank'] == 0), key=lambda e: num(e['id'])): md.append(f"| `{e['id']}` {e['title']} | `{e['in_hand']}` |")
    md += ["", "## Never seen in any form", "", "Noted here, not asked for: marriages and further deaths come as folders of their own.", "", "| Page | Where it should be | What it settles |", "|---|---|---|"]
    for n in NEVER_SEEN: md.append(f"| {n['what']} | {n['where']} | {n['settles']} |")
    open('PAGE-TALLY.md', 'w').write('\n'.join(md) + '\n')
    return c


if __name__ == '__main__':
    o = build(); c = write(o)
    print(len(o), 'strips;', dict(sorted(c.items())), '; never seen', len(NEVER_SEEN))
