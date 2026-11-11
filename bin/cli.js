#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const skillSrc = path.join(__dirname, '..', 'skills', 'promptcraft-pro', 'SKILL.md');
const cmdSrc = path.join(__dirname, '..', '.claude', 'commands', 'promptcraft.md');

if (args.includes('--help') || args.includes('-h')) {
  console.log('Usage: npx promptcraft-pro [--check]');
  console.log('Installs PromptCraft Pro skill and /promptcraft slash command into ./.claude/');
  process.exit(0);
}

if (args.includes('--check')) {
  if (!fs.existsSync(skillSrc)) {
    console.error('Error: SKILL.md missing at', skillSrc);
    process.exit(1);
  }
  if (!fs.existsSync(cmdSrc)) {
    console.error('Error: promptcraft.md command missing at', cmdSrc);
    process.exit(1);
  }
  console.log('PromptCraft Pro package integrity verified.');
  process.exit(0);
}

const targetDir = process.cwd();
const destSkillDir = path.join(targetDir, '.claude', 'skills', 'promptcraft-pro');
const destCmdDir = path.join(targetDir, '.claude', 'commands');

fs.mkdirSync(destSkillDir, { recursive: true });
fs.mkdirSync(destCmdDir, { recursive: true });

fs.cpSync(path.dirname(skillSrc), destSkillDir, { recursive: true });
fs.copyFileSync(cmdSrc, path.join(destCmdDir, 'promptcraft.md'));

console.log('Installed PromptCraft Pro skill and /promptcraft command into ./.claude/');
