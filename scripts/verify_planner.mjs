import fs from 'node:fs';

// Usage: ego-browser nodejs < verify_planner.mjs
const task = await taskSpace(1);
const liPage = task.page("p48") || await task.newPage();
const fbPage = task.page("p51") || await task.newPage();

console.log("[Audit] Verifying LinkedIn scheduled queue...");
await liPage.goto("https://www.linkedin.com/company/35934326/admin/dashboard/", { waitUntil: "domcontentloaded", timeout: 30000 });
await new Promise(r => setTimeout(r, 3000));

await liPage.evaluate(() => {
  const btn = Array.from(document.querySelectorAll("button, span")).find(el => el.innerText.trim() === "创建");
  if (btn) btn.click();
});
await new Promise(r => setTimeout(r, 1000));

await liPage.evaluate(() => {
  const opt = Array.from(document.querySelectorAll("div, span, button")).find(el => el.innerText.trim() === "发动态");
  if (opt) opt.click();
});
await new Promise(r => setTimeout(r, 1500));

await liPage.evaluate(() => {
  const clockBtn = document.querySelector('button[aria-label="设定动态发布时间"], .share-actions__scheduled-post-btn');
  if (clockBtn) clockBtn.click();
});
await new Promise(r => setTimeout(r, 1200));

await liPage.evaluate(() => {
  const viewAllLink = Array.from(document.querySelectorAll("a, button, span")).find(el => el.innerText.includes("查看全部已设定发布时间的动态"));
  if (viewAllLink) viewAllLink.click();
});
await new Promise(r => setTimeout(r, 2000));
await liPage.screenshot({ path: "linkedin_scheduled_audit.png" });
console.log("[Audit] LinkedIn scheduled audit screenshot saved: linkedin_scheduled_audit.png");

// 2. Facebook Planner Audit
console.log("[Audit] Verifying Meta Business Suite Planner...");
await fbPage.goto("https://business.facebook.com/latest/planner?asset_id=115347823236277", { waitUntil: "domcontentloaded", timeout: 30000 });
await new Promise(r => setTimeout(r, 5000));
await fbPage.screenshot({ path: "facebook_planner_audit.png" });
console.log("[Audit] Facebook Planner audit screenshot saved: facebook_planner_audit.png");

console.log("[Audit] Full verification audit complete!");
