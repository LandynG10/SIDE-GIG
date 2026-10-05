# Third-party skills vendored here

| Skills | Source | Commit | License |
| --- | --- | --- | --- |
| `replica-*` (11 skills) | https://github.com/Jakeschincariol/replica-skill | 77c9436 | MIT (`LICENSE.replica-skill`) |
| `cold-email`, `prospecting`, `copywriting`, `offers`, `pricing`, `seo-audit`, `social`, `sales-enablement`, `marketing-psychology` | https://github.com/coreyhaines31/marketingskills | dda3841 | MIT (`LICENSE.marketingskills`) |

oh-my-claudecode (https://github.com/Yeachan-Heo/oh-my-claudecode, MIT) is not
vendored: it is a full plugin with hooks and a Node runtime, so it is installed
through `.claude/settings.json` (`extraKnownMarketplaces` + `enabledPlugins`).
Claude Code prompts to install it the first time the repo is trusted. The full
marketing (50 skills) and replica packs are registered there too, so
`/plugin install marketing-skills@marketingskills` gets the rest.

`local-site-sprint` is our own skill for this repo's business.
