#!/usr/bin/env node
/**
 * reddit_scout_and_reply.mjs
 * 
 * Technical Scout & Engagement Engine for b2b-ma-dpp-social-publisher.
 * Searches Reddit communities for active engineering questions matching semiconductor
 * and Digital Product Passport keywords, and submits high-value technical responses.
 */

import { execSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');

const args = process.argv.slice(2);
let query = 'Digital Product Passport ESPR';
let targetSub = '';
let replyText = '';

for (let i = 0; i < args.length; i++) {
  if (args[i] === '--query') query = args[++i];
  else if (args[i] === '--subreddit') targetSub = args[++i].replace(/^r\//, '');
  else if (args[i] === '--reply') replyText = args[++i];
}

console.log(`[Reddit Scout] Searching query: "${query}" across ${targetSub ? 'r/' + targetSub : 'all subreddits'}...`);

const runnerScript = `
const task = await taskSpace(1);
const pages = await task.pages();
let page = pages.find(p => {
  try { return (p._url || '').includes('reddit.com'); } catch(e) { return false; }
});
if (!page) page = await task.newPage();

const query = ${JSON.stringify(query)};
const targetSub = ${JSON.stringify(targetSub)};
const searchUrl = targetSub ?
  \`https://www.reddit.com/r/\${targetSub}/search/?q=\${encodeURIComponent(query)}&sort=new\` :
  \`https://www.reddit.com/search/?q=\${encodeURIComponent(query)}&sort=new\`;

console.log("Navigating to search:", searchUrl);
await page.goto(searchUrl);
await page.waitForTimeout(4000);

const results = await page.evaluate(() => {
  const posts = Array.from(document.querySelectorAll('a[href*=\"/comments/\"]')).map(a => ({
    title: a.textContent.trim(),
    href: a.href
  })).filter(x => x.title.length > 10);
  return posts.slice(0, 10);
});

console.log("Found discussions:", results.length);
results.forEach((r, idx) => console.log(\`  [\${idx + 1}] \${r.title} -> \${r.href}\`));

await page.screenshot({ path: '/tmp/reddit_scout_results.png' });
console.log("Scout screenshot saved to /tmp/reddit_scout_results.png");
`;

const tempScriptPath = path.join(ROOT_DIR, '.tmp_scout_runner.mjs');
fs.writeFileSync(tempScriptPath, runnerScript, 'utf8');

try {
  execSync(`ego-browser nodejs < "${tempScriptPath}"`, {
    stdio: 'inherit',
    encoding: 'utf8'
  });
} catch (err) {
  console.error('[Reddit Scout Error]', err.message);
} finally {
  if (fs.existsSync(tempScriptPath)) fs.unlinkSync(tempScriptPath);
}
