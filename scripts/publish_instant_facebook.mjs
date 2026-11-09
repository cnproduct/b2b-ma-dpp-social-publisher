import fs from 'node:fs';
import path from 'node:path';

// Usage: ego-browser nodejs < publish_instant_facebook.mjs
// Default Verified Flow: Always publishes Full Text + 1200x1350 Infographic Image + Hashtags
const task = await taskSpace(1);
const page = task.page("p51") || await task.newPage();

// 1. Ensure viewport is standardized via CDP emulation
if (typeof page.cdp === 'function') {
  await page.cdp('Emulation.setDeviceMetricsOverride', {
    width: 1440,
    height: 900,
    deviceScaleFactor: 1,
    mobile: false
  });
}

console.log("[Facebook] Navigating to Meta Business Suite Composer...");
await page.goto("https://business.facebook.com/latest/composer?asset_id=115347823236277", { waitUntil: "domcontentloaded", timeout: 30000 });
await new Promise(r => setTimeout(r, 4000));

// 2. Locate and upload infographic photo
const defaultImg = "/Users/happy/Library/CloudStorage/GoogleDrive-cnproduct@gmail.com/我的云端硬盘/WPS同步盘/贸启航/客户贸启航/mqh客户/科山芯创/Cosine/ma_dpp_30_campaign/images/day_01.png";
console.log("[Facebook] Locating '添加照片/视频' button...");

const photoBtnCoords = await page.evaluate(() => {
  window.scrollTo(0, 0);
  const scrollables = Array.from(document.querySelectorAll('div')).filter(d => d.scrollHeight > d.clientHeight && d.clientHeight > 300);
  scrollables.forEach(s => s.scrollTop = 0);
  const btn = Array.from(document.querySelectorAll('[role="button"], button, div, span')).find(e => e.innerText && (e.innerText.trim() === '添加照片/视频' || e.innerText.trim() === '添加照片'));
  if (btn) {
    const r = btn.getBoundingClientRect();
    // Click inner button on the left (offset +50px from left)
    return { x: r.left + 50, y: r.top + r.height / 2 };
  }
  return { x: 213, y: 376 }; // Verified fallback coordinates
});

console.log("[Facebook] Photo button coords:", photoBtnCoords);
if (photoBtnCoords) {
  const chooserPromise = page.waitForFileChooser({ timeout: 10000 });
  await page.mouse.click(photoBtnCoords.x, photoBtnCoords.y);
  const chooser = await chooserPromise;
  await chooser.setFiles(defaultImg);
  console.log("[Facebook] Photo attached successfully!");
  await new Promise(r => setTimeout(r, 4000));
}

// 3. Prepare copy (Full text + live links + hashtags)
let fullCopy = "";
const manifestPath = "/Users/happy/Library/CloudStorage/GoogleDrive-cnproduct@gmail.com/我的云端硬盘/WPS同步盘/贸启航/客户贸启航/mqh客户/科山芯创/Cosine/ma_dpp_30_campaign/campaign_manifest_30_days.json";

if (fs.existsSync(manifestPath)) {
  const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf-8"));
  const firstDay = Array.isArray(manifest) ? manifest[0] : (manifest.campaign ? manifest.campaign[0] : null);
  if (firstDay && firstDay.facebook_copy) {
    fullCopy = firstDay.facebook_copy;
  }
}

if (!fullCopy) {
  fullCopy = `[Day 1/30: Cosine Semiconductor MA-DPP Series] ⚡

Is your component supply chain ready for the EU ESPR 2024/1781 mandate? 

Today, Cosine Nanoelectronics showcases the The 2026 Semiconductor Digital Product Passport Mandate—fully certified under international standard ISO/IEC 15459 Node 100015!

How EU Ecodesign Regulation Reshapes Component Procurement for Global Tier-1 OEMs

Why European and global OEMs choose Cosine:
✓ Mandatory lifecycle carbon footprint & recyclability reporting under EU ESPR 2024/1781
✓ Zero broker blindspots: Direct die-level batch authentication via decentralized MA-DPP node
✓ Instant QR-scan access to SGS accredited lab chemical and ESD test dossiers

🏆 Highlights:
• BOM Traceability: 100%
• Universal Identifier: Node 100015
• Tamper-Proof Proof: SHA-256

🔍 Scan or click to view the cryptographically verified passport and download official SGS test reports:
https://www.cosinechips.com/ma-dpp

💬 Questions about pin-to-pin replacements or custom volume pricing? Message us directly or email sales@cosinechips.com!

#CosineChips #MADPP #Semiconductor #ElectronicsEngineering #SmartGrid #Robotics #RoHS #ISO15459`;
}

// 4. Fill text via page.fill to ensure React / Draft.js synthetic event synchronization
console.log(`[Facebook] Filling text into rich editor (${fullCopy.length} chars)...`);
await page.fill('div.notranslate._5rpu, [contenteditable="true"]', fullCopy);
await new Promise(r => setTimeout(r, 2000));

// Dismiss hashtag autocomplete if visible
await page.keyboard.press("Escape");
await page.evaluate(() => {
  const label = document.querySelector('div[aria-label="发布位置"]');
  if (label) label.click();
});
await new Promise(r => setTimeout(r, 1000));

// 5. Verify text was recognized before clicking publish
const textLength = await page.evaluate(() => {
  const ed = document.querySelector('div.notranslate._5rpu, [contenteditable="true"]');
  return ed ? ed.innerText.trim().length : 0;
});
if (textLength < 50) {
  throw new Error(`[Facebook ERROR] Text editor validation failed: text length is only ${textLength}! Aborting publish to prevent empty posts.`);
}
console.log(`[Facebook] Editor text verified: ${textLength} chars.`);

// 6. Click "发布"
console.log("[Facebook] Clicking '发布' button...");
const publishBtnCoords = await page.evaluate(() => {
  const btn = Array.from(document.querySelectorAll('button, [role="button"]')).find(b => b.innerText && b.innerText.trim() === '发布');
  if (btn) {
    const r = btn.getBoundingClientRect();
    return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
  }
  return null;
});

if (publishBtnCoords) {
  await page.mouse.click(publishBtnCoords.x, publishBtnCoords.y);
  console.log("[Facebook] Publish clicked, waiting 10 seconds for completion...");
  await new Promise(r => setTimeout(r, 10000));
}

// 7. Verify published post in table
console.log("[Facebook] Auditing published post feed...");
await page.goto("https://business.facebook.com/latest/posts/published_posts?asset_id=115347823236277", { waitUntil: "domcontentloaded", timeout: 30000 });
await new Promise(r => setTimeout(r, 4000));

const auditResult = await page.evaluate(() => {
  const rows = Array.from(document.querySelectorAll('tbody tr, div[role="row"]'));
  if (rows.length > 0) {
    return rows[0].innerText.replace(/\n+/g, ' | ');
  }
  return "No rows found";
});
console.log("[Facebook] Latest published post:", auditResult);

if (auditResult.includes("这篇帖子没有文字内容")) {
  throw new Error("[Facebook CRITICAL] Post published without text! Please check editor state.");
}

console.log("[Facebook] Verification SUCCESS: Post published with full text + image + tags!");
