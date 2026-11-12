# Duska line rebuild: protocol and current state

This file tells any analyst (human or AI) how this repository is worked, and where things stand. Read it before touching the data.

## What this is

An independent reconstruction of the paternal (father's father) line of Kevin J.S. Duska Jr., made from his own Duska archive, handed over one desktop folder at a time. It is run as a test: the finished AI tree will be compared with the tree Kevin built himself.

## Analyst brief (agent A-01)

Forensically reconstruct the genealogy of the owner of a computer in Calgary, working as a certified genealogist would, without holding the credential. Evidence is limited to the folders handed over, the analyst's training, and whatever is publicly reachable. Kevin may give other agents a different brief; the brief in force is recorded in `data/role.json`.

## Rules

1. One folder batch at a time. Kevin names each folder and says what it is. Log it in `data/folders.json`. A folder stays `open` until Kevin says it is complete.
2. Archive everything. Originals go to `records/<folder-id>_<name>/originals/` with a `MANIFEST.json` (sha256, bytes, pixels). Web-size copies go to `assets/pages/<folder-id>/`.
3. Every document gets an entry in `data/documents.json`: an entry-by-entry abstract in English, plus full transcription and translation of passages that bear on the line or are worth keeping. Mark doubtful readings with square brackets and a reading level (high, medium, low).
4. Every batch gets a blurb in `data/batches.json`.
5. Raise hypotheses, then solve them. Each hypothesis has a confidence, a basis and a named test. On each batch, rule on every open hypothesis the new evidence touches and log the change. Statuses: open, supported, solved, refuted.
6. Every fact on the tree (`data/people.json`) cites a source ID. Proof levels: stated, documented, inferred, prior.
7. Interesting or funny finds that are not about the line go to `data/curiosities.json`.
8. Requests for more material go to `data/requests.json` with status `held`. Raise them with Kevin only once a whole line has been processed from the folders given.
9. Blind test. Do not read Kevin's published tree or his one-name study site (duskagenealogy.primerogueinc.com) until the comparison phase. Anything already known is logged in `data/priors.json`.
10. Living people: exact birth dates stay out of this public repository. Years only.
11. Outside research is allowed and is logged in `data/leads.json` with a URL. A lead is not a finding.
12. After any data change run `python3 build.py` and commit `index.html` with the data.
13. This repo is one of three (Duska, Demko, Places) with a coordinator above them. This agent is the only writer here and merges its own work into `main` after every batch. Agents talk through `comms/` as set out in `comms/README.md`: read the other repos' outboxes at the start of each batch, write to your own.

## Layout

    data/        people, candidates, sources, hypotheses, batches, folders, documents,
                 curiosities, priors, leads, requests, role (all JSON)
    records/     original files as received, one directory per folder
    assets/      web-size page images used by the front end
    site/        template.html
    build.py     builds index.html (static, data inlined)
    index.html   the front end

## Current state (2026-11-11)

- Batches: B-000 baseline, B-001 Folder 1, B-002 Folder 2.
- Folder F-001, `Documents/Genealogy/Duska Misc/Senne Interesting Pages`: open, 10 files received.
- Folder 1 is a parish copy-book of circulars from the Bishop of Szatmár, June 1837 to January 1840, Nagykapos district. No Duska named. Context only.
- Folder F-002, `Documents/Genealogy/Duska and Demko Leads/Cicarovce`: complete, 1 file. Baptism of Mihály Demkó, b. 19 Aug 1882, son of György Demkó (Greek Catholic) and Mária Hreskó (Roman Catholic), Viszoka 132. Held as unplaced candidates in `data/candidates.json`.
- Tree so far: Ahn 1 and Ahn 2 stated by Kevin. Ahn 4, 8 and 9 (Maria Demko) rest on priors only.
- Hypotheses: H-001 to H-008, H-010 and H-012 to H-015 open, H-011 supported, H-009 solved. H-012 (Mihály is Maria Demko's father) against H-013 (her brother) is the live question.
- A private preview of the front end is published as the artifact "Duska Line Rebuild".
- First messages to the Demko agent, the Places agent and the coordinator are in `comms/outbox/`. The Demko repo (`primerogueinc/genealogy-demko-1`) was empty on 2026-11-11 and the Places repo did not exist yet.

## Comparison phase

When Kevin declares the archive complete: freeze the data, then read his tree and score the rebuild. Report matches, misses, disagreements, and anything the rebuild found that his tree lacks.
