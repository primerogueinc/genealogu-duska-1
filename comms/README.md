# Rules for all genealogy agents: read first

Proposed by the Duska agent on 2026-11-11 from what the three chats were already doing. The coordinator may amend it. Kevin's own instructions always come first.

## Who is who

| Agent       | Repository                        | Owns                                                        | ID prefix            |
|-------------|-----------------------------------|-------------------------------------------------------------|----------------------|
| Duska       | primerogueinc/genealogu-duska-1   | Ahn 8 and the Duska male line                               | none (cite as DUS:)  |
| Demko       | primerogueinc/genealogy-demko-1   | Ahn 9 (Maria Demko) and everything above her                | DM-                  |
| Places      | not created yet                   | Villages, parishes, jurisdictions, name variants            | PL-                  |
| Coordinator | none; keeps the ledger            | Cross-line rulings, the crosswalk, the final comparison     | X-                   |

Direct ancestors are `P-0NN` in every repo, where NN is the Ahnentafel number.

## How agents talk

Chats cannot message each other. The Project docs are the channel, and the repos are the record.

1. One writer per doc and per repo. Never edit another agent's doc or repo.
2. Agent-to-agent notes are Project docs named `claude/<from>-agent-to-<to>-agent.md`. The sender rewrites its own note when it has something new and dates each section.
3. The coordinator alone writes `claude/coordinator-ledger-duska-demko.md`. A ruling there outranks a line agent's entry wherever two lines touch.
4. At the start of every batch, read the ledger and every note addressed to you. Log what you took from them as a batch in your own repo.
5. Keep a copy of your outgoing notes in your repo (`comms/` or `interagent/`).
6. Each agent merges its own work into its own `main` after every batch, so the others can read it.

## How every agent works

1. One folder batch at a time. Kevin names each desktop folder and says what it is. Keep a folder register. A folder stays open until Kevin says it is complete.
2. Archive every file received, with its original name and a SHA-256 checksum.
3. Every document gets an English abstract. Passages that bear on the line get a full transcription and translation. Doubtful readings are marked.
4. Every batch gets a blurb. Raise hypotheses with a confidence and a named test, then rule on them as evidence arrives.
5. Every fact on a tree cites a source ID. Proof levels: stated, documented, inferred, prior. A fact relayed from another chat is scored as given, not as rebuilt.
6. Cite another agent's finding by its ID. Do not copy it into your tree as your own.
7. A record that concerns two lines is archived in both repos under the same file name. Compare checksums and readings.
8. Interesting or funny finds that are not about the line are kept in a curiosities list.
9. Requests to Kevin for more material are queued and raised only once a whole line has been processed from the folders given.
10. Kevin's published tree and his one-name study site stay unread until the coordinator opens the comparison phase.
11. All repos are public. Exact birth dates of living people stay out of them.
12. Each repo carries a front end built from its data.

## Earlier sections

From 13 Nov 2026 each `to-<name>.md` holds the sections written from batch B-043 on. Older sections are in `comms/earlier/to-<name>.md`, moved unchanged. The Demko agent did the same at DM-B-019.
