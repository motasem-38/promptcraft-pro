# PromptCraft Pro

[![Verify Package & Build Artifact](https://github.com/motasem-38/promptcraft-pro/actions/workflows/ci.yml/badge.svg)](https://github.com/motasem-38/promptcraft-pro/actions/workflows/ci.yml)

PromptCraft Pro is a portable model-aware prompt-engineering skill. Install it into a supported LLM harness, then ask it to design, adapt, or evaluate prompts.

PromptCraft Pro is open source and available for anyone to use, inspect, modify, and redistribute under the [MIT License](LICENSE).

## Install

### Claude Code Native Slash Command & Skill (Quick Install)

Once version 1.0.0 is published to npm, install the skill and native `/promptcraft`
command into your project's `.claude/` directory:

```bash
npx promptcraft-pro@1.0.0
```

Before npm publication, install from a local checkout with `node /path/to/promptcraft-pro/bin/cli.js`
while in your target project. The installer copies the skill and its supporting files
and replaces existing PromptCraft Pro files. Run `/promptcraft <your request>` in Claude Code.


### ChatGPT / Codex Plugin

Version 1.0.0 packages the original skill unchanged as an Agent Plugins 1.0
plugin with a custom icon and public-directory metadata.

- [Publication guide (Arabic)](docs/PUBLISHING.ar.md).
- [Host acceptance checks and current test status](docs/SMOKE-TESTS.md).

The distributable ZIP can be built in the ignored `dist/` directory with
`npm run build:zip`, or outside this source directory with
`python scripts/build_plugin.py ../promptcraft-pro-1.0.0.zip`.
A development installation does not publish the plugin in the public directory.
The public ZIP requires developer verification, portal scans, review, and a
separate publish action. No MCP server, OAuth setup, or API key is required.

### Any agent supported by skills.sh

```bash
npx skills@latest add https://github.com/motasem-38/promptcraft-pro --skill promptcraft-pro
```

To install for a specific agent, add its agent name:

```bash
npx skills@latest add https://github.com/motasem-38/promptcraft-pro --skill promptcraft-pro -a claude-code
```

### Claude Code

```bash
npx skills@latest add https://github.com/motasem-38/promptcraft-pro --skill promptcraft-pro -a claude-code
```

### Codex

```bash
npx skills@latest add https://github.com/motasem-38/promptcraft-pro --skill promptcraft-pro -a codex
```

### GitHub Copilot

```bash
npx skills@latest add https://github.com/motasem-38/promptcraft-pro --skill promptcraft-pro -a copilot
```

### Gemini CLI

```bash
gemini skills install https://github.com/motasem-38/promptcraft-pro.git --path skills/promptcraft-pro
```

The exact command and supported agent name can vary by the harness version. Use the repository link if your tool has an "install skill from GitHub" action.

## What it does

The `promptcraft-pro` skill helps an LLM:

- clarify the goal, inputs, constraints, and risk level
- produce a ready-to-copy prompt
- adapt prompts to a named model or platform
- add verification checks, test cases, and human review steps
- avoid invented context and unsupported guarantees

The skill does not call model APIs, collect user information, or require credentials.

This folder contains the public-facing informational pages for PromptCraft Pro, published by **Motasem Abumoghli**, individual developer.

## Files

- `index.html` — product overview and official model-documentation links
- `support.html` — support information
- `privacy.html` — narrow privacy statement for PromptCraft Pro itself
- `terms.html` — terms of service
- `skills/promptcraft-pro/SKILL.md` — installable skill definition
- `LICENSE` — MIT open-source license
- `assets/style.css` — shared responsive styling

## Sources

The site includes official documentation sources for OpenAI, Anthropic, Google Gemini, and xAI. These sources support the model references only; they are not claims about third-party data practices or endorsements.

The installable skill is included in this repository so users can install it directly from GitHub. It does not call model APIs, collect user information, or require credentials.

## GitHub Pages

The public site is served from the `main` branch at:

https://motasem-38.github.io/promptcraft-pro/

Verify each page directly:
   - `/index.html`
   - `/support.html`
   - `/privacy.html`
   - `/terms.html`

## Before changing the distribution

- Support uses the repository's enabled public issue tracker; do not post private information there.
- Review the terms and privacy language for the publisher’s jurisdiction and intended distribution channel.
- Check the live pages on mobile and desktop after GitHub Pages finishes deploying.

## Privacy scope

The privacy page intentionally describes only PromptCraft Pro’s own practices. It does not make claims about ChatGPT, OpenAI, Anthropic, Google, xAI, GitHub Pages, browsers, networks, or any other third party.
