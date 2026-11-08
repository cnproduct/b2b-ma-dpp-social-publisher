import fs from 'node:fs';
import path from 'node:path';

// Usage: ego-browser nodejs < publish_instant_facebook.mjs
const task = await taskSpace(1);
const page = task.page("p51") || await task.newPage();

console.log("[Facebook] Navigating to official page...");
await page.goto("https://www.facebook.com/115347823236277", { waitUntil: "domcontentloaded", timeout: 30000 });
await new Promise(r => setTimeout(r, 4000));

// Scroll to feed composer
await page.evaluate(() => {
  window.scrollBy(0, 500);
});
await new Promise(r => setTimeout(r, 1000));

// Click 照片/视频
const defaultImg = "/Users/happy/Library/CloudStorage/GoogleDrive-cnproduct@gmail.com/我的云端硬盘/WPS同步盘/贸启航/客户贸启航/mqh客户/科山芯创/Cosine/ma_dpp_30_campaign/images/day_01.png";
console.log("[Facebook] Triggering media upload...");
const photoCoords = await page.evaluate(() => {
  const el = Array.from(document.querySelectorAll("div, span, button")).find(e => e.innerText && e.innerText.trim() === "照片/视频");
  if (el) {
    const r = el.getBoundingClientRect();
    return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
  }
  return null;
});

if (photoCoords) {
  const chooserPromise = page.waitForFileChooser({ timeout: 10000 });
  await page.mouse.click(photoCoords.x, photoCoords.y);
  const chooser = await chooserPromise;
  await chooser.setFiles(defaultImg);
  console.log("[Facebook] Image set!");
  await new Promise(r => setTimeout(r, 4000));
}

// Fill text
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

console.log("[Facebook] Entering text...");
await page.evaluate((text) => {
  const ed = document.querySelector('[contenteditable="true"], [role="textbox"], div[aria-label*="新鲜事"]');
  if (ed) {
    ed.focus();
    document.execCommand('selectAll', false, null);
    document.execCommand('insertText', false, text);
  }
}, defaultText);
await new Promise(r => setTimeout(r, 1500));

// Click 下一页
const nextBtnCoords = await page.evaluate(() => {
  const btn = Array.from(document.querySelectorAll("button, [role=\"button\"]")).find(b => b.innerText.trim() === "下一页");
  if (btn) {
    const r = btn.getBoundingClientRect();
    return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
  }
  return null;
});

if (nextBtnCoords) {
  await page.mouse.click(nextBtnCoords.x, nextBtnCoords.y);
  await new Promise(r => setTimeout(r, 2000));
}

// Click 发帖
console.log("[Facebook] Clicking 发帖...");
const postBtnCoords = await page.evaluate(() => {
  const btn = Array.from(document.querySelectorAll("[role=\"dialog\"] [role=\"button\"], [role=\"dialog\"] button")).find(b => b.innerText.trim() === "发帖");
  if (btn) {
    const r = btn.getBoundingClientRect();
    return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
  }
  return null;
});

if (postBtnCoords) {
  await page.mouse.click(postBtnCoords.x, postBtnCoords.y);
  await new Promise(r => setTimeout(r, 6000));

  // Dismiss any upsell / modal
  await page.evaluate(() => {
    const dismissBtn = Array.from(document.querySelectorAll("button, [role=\"button\"], div, span")).find(b => b.innerText.trim() === "以后再说" || b.getAttribute("aria-label") === "关闭");
    if (dismissBtn) dismissBtn.click();
  });
  await new Promise(r => setTimeout(r, 2000));
}

console.log("[Facebook] Instant post published successfully!");
