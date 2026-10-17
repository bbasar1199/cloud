---
name: web-design-guidelines
description: Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".
metadata:
  author: vercel
  version: "1.0.0"
  argument-hint: <file-or-pattern>
---

<!-- Kaynak: vercel-labs/agent-skills (MIT). Kurallar vercel-labs/web-interface-guidelines (MIT) command.md'den yerel rules.md'ye alındı; ağdan çekilmez. -->

# Web Interface Guidelines

Review files for compliance with Web Interface Guidelines.

## How It Works

1. Read the rules in [rules.md](rules.md) (local copy; do not fetch from the network)
2. Read the specified files (or prompt user for files/pattern)
3. Check against all rules in rules.md
4. Output findings in the terse `file:line` format

## Usage

When a user provides a file or pattern argument:
1. Read rules.md
2. Read the specified files
3. Apply all rules from rules.md
4. Output findings using the format specified in rules.md

If no files specified, ask the user which files to review.

## Ayluna notu

Ayluna işinde `ayluna-imza/TASARIM-BILGISI.md` ve `ayluna-imza/beceriler/ayluna-tasarim/SKILL.md` önce gelir. Şu kurallar Ayluna'da geçmez:
- "Title Case for headings/buttons": Türkçe metin cümle düzeninde yazılır.
- "Second person; avoid first person": marka sesi "biz" der ("30 güne uzattık").
- Bulgular yalnız öneridir; kullanıcı seçmeden toplu uygulanmaz.
