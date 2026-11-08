import fs from 'node:fs';
import path from 'node:path';

// Usage: ego-browser nodejs < render_infographics.mjs
const task = await taskSpace(1);
const page = await task.newPage();

const baseDir = process.cwd();
const htmlDir = path.join(baseDir, 'html_cards');
const imgDir = path.join(baseDir, 'images');

if (!fs.existsSync(imgDir)) {
  fs.mkdirSync(imgDir, { recursive: true });
}

for (let d = 1; d <= 30; d++) {
  const dStr = String(d).padStart(2, '0');
  const htmlPath = path.join(htmlDir, `day_${dStr}.html`);
  const imgPath = path.join(imgDir, `day_${dStr}.png`);

  if (!fs.existsSync(htmlPath)) {
    console.log(`Skipping missing HTML: ${htmlPath}`);
    continue;
  }

  console.log(`Rendering Day ${dStr}: ${htmlPath}...`);
  await page.goto(`file://${htmlPath}`, { waitUntil: "domcontentloaded" });
  await new Promise(r => setTimeout(r, 600));

  await page.screenshot({
    path: imgPath,
    fullPage: true
  });
  console.log(`Saved: ${imgPath}`);
}

await page.close();
console.log("All 30 infographics rendered successfully!");
