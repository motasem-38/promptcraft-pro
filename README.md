# PromptCraft Pro

PromptCraft Pro is a portable model-aware prompt-engineering skill. Install it into a supported LLM harness, then ask it to design, adapt, or evaluate prompts.

PromptCraft Pro is open source and available for anyone to use, inspect, modify, and redistribute under the [MIT License](LICENSE).

## Install

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

- Replace the support placeholder with a real support URL or contact method supplied by the publisher.
- Review the terms and privacy language for the publisher’s jurisdiction and intended distribution channel.
- Check the live pages on mobile and desktop after GitHub Pages finishes deploying.

## Privacy scope

The privacy page intentionally describes only PromptCraft Pro’s own practices. It does not make claims about ChatGPT, OpenAI, Anthropic, Google, xAI, GitHub Pages, browsers, networks, or any other third party.
