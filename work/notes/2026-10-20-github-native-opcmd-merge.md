# Successor merge design reference

[Source GitHub-native OPCMD design](https://github.com/BigCatMellow/MAPS_Lean/blob/605ce610e0be3334d1da7af2a7c6f5912b6cc05f/work/notes/2026-10-20-github-native-opcmd-merge.md)
is preserved at the pinned original. The workflow and script are candidate
implementation; the [standing record](../coordination/standing-merge-authorization.md)
is inactive. Missing/unknown HOLD and absent active authority must refuse.
Review exact-head identity, trusted main ref, permissions, CI, review binding,
audit and emergency stop before any activation. Do not use bare merges to
bootstrap around the safeguard; no source exception carries over.
