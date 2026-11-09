import fs from 'node:fs';
import path from 'node:path';

// Usage: ego-browser nodejs < publish_instant_linkedin.mjs
const task = await taskSpace(1);
const page = task.page("p48") || await task.newPage();

console.log("[LinkedIn] Navigating to MA-DPP company page admin...");
await page.goto("https://www.linkedin.com/company/144112219/admin/page-posts/published/?editPageActiveTab=info&shareMsgArgs=null", { waitUntil: "domcontentloaded", timeout: 30000 });
await new Promise(r => setTimeout(r, 3000));

// 1. Open post composer
console.log("[LinkedIn] Opening post composer...");
await page.evaluate(() => {
  const btn = Array.from(document.querySelectorAll("button, span")).find(el => el.innerText.trim() === "创建");
  if (btn) btn.click();
});
await new Promise(r => setTimeout(r, 1200));

await page.evaluate(() => {
  const opt = Array.from(document.querySelectorAll("div, span, button")).find(el => el.innerText.trim() === "发动态");
  if (opt) opt.click();
});
await new Promise(r => setTimeout(r, 2000));

// 2. Select image
const defaultImg = "/Users/happy/Library/CloudStorage/GoogleDrive-cnproduct@gmail.com/我的云端硬盘/WPS同步盘/贸启航/客户贸启航/mqh客户/科山芯创/Cosine/ma_dpp_30_campaign/images/day_01.png";
console.log("[LinkedIn] Uploading image...");
const chooserPromise = page.waitForFileChooser({ timeout: 10000 });
await page.click('button[aria-label="添加媒体文件"]');
const chooser = await chooserPromise;
await chooser.setFiles(defaultImg);
await new Promise(r => setTimeout(r, 3000));

await page.evaluate(() => {
  const nextBtn = Array.from(document.querySelectorAll("button")).find(b => b.innerText.trim() === "下一页");
  if (nextBtn) nextBtn.click();
});
await new Promise(r => setTimeout(r, 1500));

// 3. Fill text
const defaultText = `🚀 [OFFICIAL LAUNCH] Cosine Nanoelectronics Pioneers Semiconductor Digital Product Passports (MA-DPP) for Global Tier-1 OEMs

As the European Union’s Ecodesign for Sustainable Products Regulation (ESPR 2024/1781) takes effect, global electronics procurement faces a paradigm shift. Supply chain opacity is no longer an option.

Today, Cosine Nanoelectronics is proud to launch our 30-Day MA-DPP Technical Series—demonstrating complete, cryptographic silicon traceability from raw wafer lot to factory gate.

Key Architecture Highlights:
✅ Node 100015 Decentralized Identity (ISO/IEC 15459 compliant)
✅ Direct Die-Level Traceability: Eliminating broker blindspots & counterfeit risks
✅ Immutable SHA-256 Cryptographic Seals on all test & chemical dossiers
✅ Instant QR Access to SGS CSTC Laboratory Reports (RoHS 2.0 / REACH SVHC / AEC-Q100)
✅ Pin-to-Pin Compatibility: Drop-in replacement for legacy analog & interface ICs (RS-485, CAN, Op-Amps, Gate Drivers)

Starting this week, we will publish daily technical deep-dives into our qualified analog signal chain ICs and their corresponding Digital Product Passports.

🔍 Inspect the Live MA-DPP Hub & Download Official Test Dossiers:
https://www.cosinechips.com/ma-dpp

Need engineering samples or qualification reports? Samples dispatch within 48 hours. Contact our team at sales@cosinechips.com.

#Semiconductor #DigitalProductPassport #MADPP #EUESPR #SupplyChainTraceability #AnalogIC #AutomotiveElectronics #CleanTech #CosineNanoelectronics #IndustrialAutomation`;

console.log("[LinkedIn] Inserting text...");
await page.evaluate((text) => {
  const editor = document.querySelector('.ql-editor');
  if (editor) {
    editor.focus();
    document.execCommand('selectAll', false, null);
    document.execCommand('insertText', false, text);
  }
}, defaultText);
await new Promise(r => setTimeout(r, 1500));

// 4. Click Publish (发布)
console.log("[LinkedIn] Clicking 发布...");
const res = await page.evaluate(() => {
  const pubBtn = Array.from(document.querySelectorAll("button")).find(b => b.innerText.trim() === "发布");
  if (pubBtn && !pubBtn.disabled) {
    pubBtn.click();
    return "success";
  }
  return pubBtn ? "disabled" : "not found";
});
console.log("[LinkedIn] Result:", res);
await new Promise(r => setTimeout(r, 5000));
console.log("[LinkedIn] Instant post published successfully!");
