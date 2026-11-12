# How the genealogy agents talk to each other

Chats cannot message each other directly. The repositories are the channel. They are public, so every agent can read every repo, and each repo has exactly one writer.

## Who is who

| Code  | Agent       | Repository                          | Owns                                              |
|-------|-------------|-------------------------------------|---------------------------------------------------|
| DUS   | Duska       | primerogueinc/genealogu-duska-1     | The Duska paternal line (father's father)          |
| DEM   | Demko       | primerogueinc/genealogy-demko-1     | The Demko family                                   |
| PLA   | Places      | (not created yet)                   | Villages, parishes, jurisdictions, name variants   |
| COORD | Coordinator | (to be decided)                     | Cross-repo links, conflicts, the comparison phase  |

## Rules

1. One writer per repo. An agent commits and merges only in its own repo. Nobody edits another agent's files.
2. Each agent merges its own work into its own `main` after every batch. Other agents read `main` only.
3. To say something to another agent, add a file to `comms/outbox/` in your own repo. Name it `YYYY-MM-DD_FROM-to-TO_NNN.md`. Never edit a message after it is merged. Reply with a new message in your own outbox that names the one it answers.
4. At the start of every batch, pull the other repos and read any outbox message addressed to you or to ALL. Record what you read in `comms/READ.md`.
5. Keep `comms/STATUS.md` current: what you hold, what you have concluded, what you still need.
6. Refer to anything in another repo by prefixing its ID with the repo code, for example `DUS:H-012` or `DEM:P-003`. Never copy another agent's conclusion into your tree as fact. Cite it as that agent's finding.
7. A record that concerns two repos is archived in both, with the same file name and checksum. The agent whose line the person belongs to owns the person. The other agent links to it.
8. Disagreements go to the coordinator. Write the disagreement to `COORD` in your outbox and leave both versions standing until it is ruled on.
9. The coordinator alone maintains the cross-repo link table (same person or same place appearing under different IDs) and runs the final comparison against Kevin's own tree.
