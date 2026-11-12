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
9. Blind test. Do not read Kevin's published tree or his one-name study site until the comparison phase, and do not read the accuracy page, the score feed or the Scorer's repo at all. Do not run open-web searches that combine the surnames with the villages (ruling X-011). Anything already known is logged in `data/priors.json`, and every search in `data/searches.json`.
10. Living people: exact birth dates stay out of this public repository. Years only.
11. Outside research is allowed and is logged in `data/leads.json` with a URL. A lead is not a finding.
12. After any data change run `python3 build.py` and commit `index.html` with the data.
13. This repo is one of three (Duska, Demko, Places) with a coordinator above them. This agent is the only writer here and merges its own work into `main` after every batch. Agents talk through `comms/` as set out in `comms/README.md`: read the other repos' outboxes at the start of each batch, write to your own.

14. Everything this agent receives comes from Kevin's Duska folder. A person in it who is not a Duska is still processed: index every named person in `data/candidates.json` with a `route` (the agent who should place them), send Demko and Hreskó people to the Demko agent, and send every household (village, house number, year, rite) to the Places agent.
15. The coordinator's ledger rules where lines touch. In force from ledger v2: labels and filing are priors and move nothing on their own (X-004); decide without waiting for Kevin and log it in `data/decisions.json` (X-005); a link is `solved` only on a record in hand with its archive reference, otherwise capped at 70 (X-009); a rule of law or custom recalled from training is marked as recalled (X-010); cite another agent by ID plus commit or date (X-008).
16. One batch, one commit on `main`, with the batch ID in the commit message. `.github/workflows/stamp.yml` hashes each commit and anchors it. Do not edit that file.
17. `main` is public on duska.si within about an hour. Write blurbs and notes for a stranger. Tag each hypothesis with its `X-Q-NN` question where the ledger files it under one.

## Layout

    data/        people, candidates, families, decisions, searches, sources, hypotheses, batches, folders, documents,
                 curiosities, priors, leads, requests, role (all JSON)
    records/     original files as received, one directory per folder
    assets/      web-size page images used by the front end
    site/        template.html
    build.py     builds index.html (static, data inlined)
    index.html   the front end

## Current state (2026-11-12, after B-007)

- Batches: B-000 baseline, B-001 Folder 1, B-002 Folder 2.
- Folder F-001, `Documents/Genealogy/Duska Misc/Senne Interesting Pages`: closed for now by Kevin on 12 Nov, 10 files received.
- Folder 1 is a parish copy-book of circulars from the Bishop of Szatmár, June 1837 to January 1840, Nagykapos district. No Duska named. Context only.
- Folder F-002, `Documents/Genealogy/Duska and Demko Leads/Cicarovce`: complete, 1 file. Baptism of Mihály Demkó, b. 19 Aug 1882, son of György Demkó (Greek Catholic) and Mária Hreskó (Roman Catholic), Viszoka 132. Held as unplaced candidates in `data/candidates.json`.
- B-003 (no files): took in coordinator ledger v1 and the Demko agent's first note.
- B-004, Folder F-003, `Duska Baptisms/Belza (Kosice) - Greek Catholic`: complete, 2 files. Baptisms of György Demko (b. 29 Mar 1895, Gönyű 24, son of György Demko and Katalin Jobbágy) and Mária Hriczko (b. 29 Aug [1894], Szina 182, daughter of József Hriczko and Erzsébet Kocsis). No Duska. Six more unplaced candidates. Also took in the Places agent's first findings (H-007 now supported; H-005 and H-010 raised). New hypotheses H-016 to H-019.
- B-005 (no files, 12 Nov): read ledger v2, the duska.si plan and the Site agent's notes. Added `stamp.yml`, `data/decisions.json`, `data/searches.json`, question tags and document checksums. Undid label-driven moves (H-012 back to 30, H-013 to 20) and applied the 70 cap (H-007, H-010) and the coordinator's 65 on H-016. Indexed nine more named people (K-010 to K-018) with routes. New note `comms/to-site.md`. Kevin allowed one research pass on the surnames provided nothing he has written is opened (S-000-4, DEC-14, SR-05); it was started on 12 Nov and its results are to be logged as leads in the next batch.
- B-006 (no files): the research pass reported. Leads L-006 to L-016. A village website places a Dúška family in Iňačovce in the 18th century (H-004 down to 45). No emigration record found. The report disclosed an unrequested search of Kevin's Gmail for three terms, which found nothing; reported to him and the coordinator.
- B-007, Folder F-004, `Duska Baptisms/Cicarovce`: complete, 20 files (one a duplicate of the F-002 file). No Duska. Fourteen Demko baptisms at Viszoka 1831 to 1883, three Tirpák children of a Demko mother, three Kocsis entries. Nine family groups in `data/families.json`; 79 more people in `data/candidates.json` (K-019 to K-097). The book is the Čičarovce Greek Catholic register: officiants are styled Greek Catholic pastor of Csicser (H-015 refuted). Mária Hreskó was already a mother in 1857, so she is all but ruled out as mother of Ahn 9 (H-013 down to 8). New hypotheses H-020 to H-025. The file labelled Anna Demko 1872 reads Szulák.
- Notes to the other agents: `comms/to-demko.md`, `comms/to-places.md`, `comms/to-coordinator.md`, each mirrored to the Project as `claude/duska-agent-to-<name>-agent.md`. The Places repo is `primerogueinc/duska-and-demko-villages`.
- Tree so far, all by Kevin's statement and none by record: Ahn 1 Kevin Jr., Ahn 2 Kevin John Duska, Ahn 4 Stefan Duska, Ahn 8 Mihaly Duska, Ahn 9 Maria Demko. Ahn 4 and 8 were stated in the Demko chat and relayed by coordinator ruling X-001.
- Hypotheses after B-007: H-003 and H-015 refuted, H-009 solved, H-007, H-011 and H-017 supported, the rest open. Who is Maria Demko's father (X-Q-03): H-012 Mihály b. 1882, 25; H-023 János Demkó husband of Szlekár, 15; H-024 János b. 1875, 10; H-013 György husband of Hreskó, 8. The rest of the odds sit on a Demko family outside this folder.
- The stamping workflow ran green on the B-005 push and the `proofs` branch exists.
- Shared rules for all agents are in `comms/README.md` and in the Project as `claude/ALL-AGENTS-READ-FIRST.md`. Notes to the Demko agent go in `comms/to-demko.md` and the Project doc `claude/duska-agent-to-demko-agent.md`.
- A private preview of the front end is published as the artifact "Duska Line Rebuild".
- First messages to the Demko agent, the Places agent and the coordinator are in `comms/outbox/`. The Demko repo (`primerogueinc/genealogy-demko-1`) was empty on 2026-11-11 and the Places repo did not exist yet.

## Comparison phase

When Kevin declares the archive complete: freeze the data, then read his tree and score the rebuild. Report matches, misses, disagreements, and anything the rebuild found that his tree lacks.
