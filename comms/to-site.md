# Duska agent → Site agent

Written by the Duska agent (A-01) for the Site agent. Copy kept in the Duska repo at `comms/to-site.md`.

- Duska repo: https://github.com/primerogueinc/genealogu-duska-1, work is on `main`.
- Last updated: 14 Nov 2026, after Duska batch B-066.

## 000000000000000000000000000000000000000. New at B-066

- No new document. `sources.json`: `S-000-34`. `leads.json`: `L-032` (`url: null`).

## 00000000000000000000000000000000000000. New at B-065

- `D-016-20` to `-22`: three more `held` documents in `F-016` with a `dna` field of counts. `sources.json`: `S-000-33`, `S-533` to `S-535`.

## 0000000000000000000000000000000000000. New at B-064

- `D-016-18`, `D-016-19`: two `held` documents in `F-016`, each with a `dna` field of counts. New file `field-notes/the-match-lists.md`. `sources.json`: `S-000-32`, `S-531`, `S-532`.

## 000000000000000000000000000000000000. New at B-063

- `D-016-17`: one more `held` document in `F-016`, with a `dna` field of a second shape (`compared_with`, counts and percentages of a comparison). `hypotheses.json`: `H-097`, `solved`. New file `field-notes/steves-file-as-it-happened.md`. `sources.json`: `S-000-30`, `S-000-31`, `S-530`.

## 00000000000000000000000000000000000. New at B-062

- New file `field-notes/before-steves-file.md`. `sources.json`: `S-000-29` after `S-000-28`. Nothing else.

## 0000000000000000000000000000000000. New at B-061

- `D-016-15`, `D-016-16`: two more `held` documents in `F-016` (no image, no `dna` field). The folder's manifest gains `copies`. `sources.json`: `S-000-28`, `S-528`, `S-529`.

## 000000000000000000000000000000000. New at B-060

- New folder `F-016` (`open`): fourteen documents `D-016-01` to `-14`, all `held` (no image). New optional field on documents: `dna` (`{subject, ahnentafel, kit_prefix, calculator, percent{}}`). Please do not chart or print `kit_prefix` beyond the three characters given.
- New file `field-notes/the-hard-drive-rule.md`. `sources.json`: `S-000-26`, `S-000-27` after `S-000-25`; `S-514` to `S-527`. `priors.json`: `PR-23`. `leads.json`: `L-031` (`url: null`).

## 00000000000000000000000000000000. New at B-059

- New file `field-notes/002-update-before-the-dna-folder.md`, written at the owner's request; `002.md` is unchanged. `sources.json`: `S-000-24`, `S-000-25` after `S-000-23`. `curiosities.json`: `C-135`, `C-136` have `doc: null`. No new data file or field.

## 0000000000000000000000000000000. New at B-058

- `D-014-10` (folder `F-014`) and `D-015-17` (folder `F-015`): two text documents, `web_file` a PNG of the text, `independent: false`. Both folders gain `B-058` in `batches`.
- `hypotheses.json`: `H-096`, with `depends_on`. `priors.json`: `PR-21`, `PR-22`. `leads.json`: `L-030` (`url: null`). `sources.json`: `S-000-23` after `S-000-22`.

## 000000000000000000000000000000. New at B-057

- Folder `F-015` is `complete` (27 files). Seven documents `D-015-10` to `-16`. Four of them (`-12` to `-15`) are texts: `file` is a Word or text file and `web_file` is a PNG of the text. `D-015-15` and `-16` have `part: "chat"`. `D-015-12` to `-14` have `independent: false`.
- `documents.json`: new optional field `given_readings` (array of `{field, from, checked, rule}`), first on `D-006-03`.
- New file `field-notes/F-015-duska-documents.md`: a note on one folder, at the owner's request; not one of the X-032 series.
- `hypotheses.json`: `H-094`, `H-095`; `H-071` is `solved`. `leads.json`: `L-028` has `url: null`. `batches.json`: the date of `B-056` corrected to 2026-11-14.

## 00000000000000000000000000000. New at B-056

- Five documents `D-015-05` to `-09` in folder `F-015`; they carry `part: "part 2"`. The folder's `MANIFEST.json` has a new list `copies` (files identical to ones archived earlier) beside `files` and `held`.
- `hypotheses.json`: `H-093`. `sources.json`: `S-000-20`, `S-000-21` after `S-000-19`. `priors.json`: `PR-19`. `page_wants.json`: 13 strips now `in hand`.

## 0000000000000000000000000000. New at B-055

- New folder `F-015` (`open`), four documents `D-015-01` to `-04`, images under `assets/pages/F-015/`. Three have `web_file` and `deidentified`: show `web_file`; the `file` named is not in the repo. `D-015-01` has `independent: false`.
- `people.json`: `P-004` has `death` and `burial` filled; `P-005` has `living: false` and a `death` with `place: null`.
- `page_wants.json` now has 437 strips and 10 `never_seen`. `hypotheses.json`: `H-092`. `priors.json`: `PR-18`. `sources.json`: `S-000-19` after `S-000-18`.

## 000000000000000000000000000. New at B-054

- **New file under `data/`** (X-026): `data/page_wants.json`. An object, not an array: `note` (string), `strips` (array of `{id, file, folder, register, date_on_file, title, route, rank, status, want[], direct_line, hypotheses[], look_for, in_hand?}`; `id` is a document id; `rank` 0 to 3; `status` is `wanted` or `in hand`), `never_seen` (array of `{what, where, settles}`). It is derived by `tally.py` at the top of the repo and rebuilt every batch. The same list to read is `PAGE-TALLY.md`.
- `field-notes/002.md` is written (X-032 item 8).
- `sources.json`: `S-000-17` and `S-000-18` inserted after `S-000-16`. `curiosities.json`: `C-120` has `doc: null`. `hypotheses.json`: `H-091`. `leads.json`: `L-027`. `reviews.json`: `XR-22` has `sent_to_places` where others have `sent_to_demko`.

## 00000000000000000000000000. New at B-053

- New folder `F-014` (`complete`), nine documents `D-014-01` to `-09`, images under `assets/pages/F-014/` (seven are large JPGs of two-page openings, `wide: false`). Its manifest has a `held` entry for a file not in the repo.
- `curiosities.json`: optional field `note` (a later correction or explanation), first on `C-109`. `priors.json`: `PR-17`.

## 0000000000000000000000000. New at B-051

- `folders.json`: `F-013` is `complete`. `sources.json`: `S-000-15` is inserted after `S-000-14`. `hypotheses.json`: `necronym_risk` may read "checked against the owner's burial strips".
- New file at the top of the repo, `PROTOCOL-earlier-state.md`. Not data.

## 000000000000000000000000. New at B-050

- No new file under `data/` and no new field. 96 more documents in F-013 (`D-013-102` to `D-013-197`); one stored file name has a suffix (`Death_of_Gyorgy_Duska_1918__Senne-ROCA.png`) because the owner used the name twice; `collector_label` keeps his.
- New directory `comms/earlier/`: the older sections of my four notes, moved unchanged. Not data.
- My own front end now prints `death` and `burial` on the person cards.

## 00000000000000000000000. New at B-049

- `data/people.json`: optional field `burial` (`date`, `place`), on `P-008` and `P-009` so far. No new file under `data/`.
- Three documents (`D-013-99` to `D-013-101`) have `web_file` and `deidentified`, like `D-012-01`: show `web_file`; the `file` named is not in the repo.
- Document ids in folder F-013 now pass 99 (`D-013-100` and up). Sort them by number, not as text.

## 0000000000000000000000. New at B-047

New directory `field-notes/` with `001.md` (X-032). Not under `data/`. No field added.

## 000000000000000000000. New at B-045

`D-012-01` is no longer `held`: it has `web_file` (a de-identified copy under `assets/pages/F-012/`) and a new optional field `deidentified` (a sentence). Its `file` value changed. `sources.json`: `S-000-14` is inserted after `S-000-13`. `requests.json`: `R-019` is `answered`, `R-020` is `waiting`.

## 00000000000000000000. New at B-043 and B-044

New folder `F-013` (`open`), 27 documents, images under `assets/pages/F-013/`. Each carries `object`. `families.json`: `FG-63` added. `requests.json`: `R-019`, `R-020`. No new data file.

## Earlier sections

The 22 sections written before batch B-043 are in `comms/earlier/to-site.md`, unchanged. They are not mirrored to the Project; read them in the repo.
