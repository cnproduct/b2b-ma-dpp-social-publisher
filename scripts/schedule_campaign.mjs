#!/usr/bin/env node
/**
 * schedule_campaign.mjs
 * 
 * Master Tri-Platform Scheduler (LinkedIn + Facebook + Reddit)
 * Schedules or executes B2B MA-DPP technical campaigns across:
 * 1. LinkedIn Official Company Page (via LinkedIn Scheduler)
 * 2. Facebook Official Page (via Meta Business Suite Planner)
 * 3. Reddit Technical Subreddits (Alternating 60-day rhythm: Topics & Expert Answers)
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');

// Parse arguments
const args = process.argv.slice(2);
let targetPlatform = 'all'; // 'all', 'linkedin', 'facebook', 'reddit'
let dayFilter = null; // number or range '1-60'

for (let i = 0; i < args.length; i++) {
  if (args[i] === '--platform') targetPlatform = args[++i];
  else if (args[i] === '--day') dayFilter = parseInt(args[++i], 10);
  else if (args[i] === '--days') dayFilter = args[++i];
}

// Locate manifest and status files
let manifestPath = path.join(ROOT_DIR, 'campaign_manifest_60_days.json');
let statusPath = path.join(ROOT_DIR, 'schedule_status_60_days.json');

if (!fs.existsSync(manifestPath)) {
  manifestPath = path.join(ROOT_DIR, 'campaign_manifest_30_days.json');
  statusPath = path.join(ROOT_DIR, 'schedule_status.json');
}

const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
let status = fs.existsSync(statusPath) ? JSON.parse(fs.readFileSync(statusPath, 'utf8')) : [];

console.log(`[Master Scheduler] Platform: ${targetPlatform} | Manifest: ${manifest.length} Days`);

// Runner in ego-browser
const runnerCode = `
import fs from 'node:fs';
import path from 'node:path';

const manifest = ${JSON.stringify(manifest)};
const targetPlatform = ${JSON.stringify(targetPlatform)};
const dayFilter = ${JSON.stringify(dayFilter)};

const task = await taskSpace(1);
const pages = await task.pages();

// Match or locate pages
let liPage = pages.find(p => {
  try { return (p._url || '').includes('linkedin.com'); } catch(e) { return false; }
});
let fbPage = pages.find(p => {
  try { return (p._url || '').includes('facebook.com'); } catch(e) { return false; }
});
let redditPage = pages.find(p => {
  try { return (p._url || '').includes('reddit.com'); } catch(e) { return false; }
});

console.log("Pages initialized:", {
  hasLI: !!liPage,
  hasFB: !!fbPage,
  hasReddit: !!redditPage
});

// Helper for days filter
function isDayAllowed(dayNum) {
  if (!dayFilter) return true;
  if (typeof dayFilter === 'number') return dayNum === dayFilter;
  if (typeof dayFilter === 'string' && dayFilter.includes('-')) {
    const [start, end] = dayFilter.split('-').map(Number);
    return dayNum >= start && dayNum <= end;
  }
  return true;
}

for (const item of manifest) {
  if (!isDayAllowed(item.day)) continue;

  console.log(\`\\n=== Processing Day \${item.day} (\${item.date} \${item.time}) ===\`);

  // 1. LinkedIn Scheduler
  if ((targetPlatform === 'all' || targetPlatform === 'linkedin') && liPage) {
    try {
      console.log(\`[LinkedIn] Scheduling Day \${item.day}...\`);
      await liPage.goto("https://www.linkedin.com/company/35934326/admin/dashboard/");
      await liPage.waitForTimeout(3000);

      // Open composer
      await liPage.evaluate(() => {
        const btn = Array.from(document.querySelectorAll("button, span")).find(el => el.innerText.trim() === "创建");
        if (btn) btn.click();
      });
      await liPage.waitForTimeout(1000);
      await liPage.evaluate(() => {
        const opt = Array.from(document.querySelectorAll("div, span, button")).find(el => el.innerText.trim() === "发动态");
        if (opt) opt.click();
      });
      await liPage.waitForTimeout(2000);

      // Set schedule date & time
      await liPage.evaluate(() => {
        const clockBtn = document.querySelector('button[aria-label="设定动态发布时间"], .share-actions__scheduled-post-btn');
        if (clockBtn) clockBtn.click();
      });
      await liPage.waitForTimeout(1500);

      console.log(\`[LinkedIn] Day \${item.day} schedule modal opened.\`);
    } catch (e) {
      console.error(\`[LinkedIn Error Day \${item.day}]\`, e.message);
    }
  }

  // 2. Facebook Meta Business Suite Scheduler
  if ((targetPlatform === 'all' || targetPlatform === 'facebook') && fbPage) {
    try {
      console.log(\`[Facebook] Processing Day \${item.day} in Meta Business Suite...\`);
      await fbPage.goto("https://business.facebook.com/latest/posts/scheduled_posts?asset_id=115347823236277");
      await fbPage.waitForTimeout(4000);

      // Click Create post button
      await fbPage.evaluate(() => {
        const btn = Array.from(document.querySelectorAll("div[role='button'], button")).find(el => el.innerText.includes("创建帖子") || el.innerText.includes("Create post"));
        if (btn) btn.click();
      });
      await fbPage.waitForTimeout(5000);

      // Fill copy via page.fill (guarantees React synthetic events synchronization)
      await fbPage.fill('div.notranslate._5rpu, [contenteditable=\"true\"]', item.facebook_copy);
      await fbPage.waitForTimeout(1000);
      console.log(\`[Facebook] Day \${item.day} copy inserted.\`);
    } catch (e) {
      console.error(\`[Facebook Error Day \${item.day}]\`, e.message);
    }
  }

  // 3. Reddit Technical Community Strategy
  if ((targetPlatform === 'all' || targetPlatform === 'reddit') && item.reddit) {
    try {
      console.log(\`[Reddit] Day \${item.day} Mode: \${item.reddit.mode} | Target: \${item.reddit.target_subreddit}\`);
      if (redditPage) {
        if (item.reddit.mode === 'create_topic') {
          console.log(\`[Reddit] Anchor Topic: "\${item.reddit.title}"\`);
        } else {
          console.log(\`[Reddit] Targeted Reply on Keywords: \${item.reddit.keywords.join(', ')}\`);
        }
      }
    } catch (e) {
      console.error(\`[Reddit Error Day \${item.day}]\`, e.message);
    }
  }
}
`;

const tempRunner = path.join(ROOT_DIR, '.tmp_master_scheduler.mjs');
fs.writeFileSync(tempRunner, runnerCode, 'utf8');

try {
  execSync(`ego-browser nodejs < "${tempRunner}"`, {
    stdio: 'inherit',
    encoding: 'utf8'
  });
} catch (err) {
  console.error('[Master Scheduler Error]', err.message);
} finally {
  if (fs.existsSync(tempRunner)) fs.unlinkSync(tempRunner);
}
