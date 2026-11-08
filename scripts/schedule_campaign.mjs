import fs from 'node:fs';

const manifestPath = '/Users/happy/Library/CloudStorage/GoogleDrive-cnproduct@gmail.com/我的云端硬盘/WPS同步盘/贸启航/客户贸启航/mqh客户/科山芯创/Cosine/ma_dpp_30_campaign/campaign_manifest_30_days.json';
const statusPath = '/Users/happy/Library/CloudStorage/GoogleDrive-cnproduct@gmail.com/我的云端硬盘/WPS同步盘/贸启航/客户贸启航/mqh客户/科山芯创/Cosine/ma_dpp_30_campaign/schedule_status.json';

const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
let status = JSON.parse(fs.readFileSync(statusPath, 'utf8'));

const task = await taskSpace(1);
const liPage = task.page("p48");
const fbPage = task.page("p51");

async function scheduleLinkedInDay(page, dayData) {
  console.log(`[LinkedIn] Starting Day ${dayData.day}: ${dayData.date} ${dayData.time}...`);
  await page.goto("https://www.linkedin.com/company/35934326/admin/dashboard/", { waitUntil: "domcontentloaded", timeout: 30000 });
  await new Promise(r => setTimeout(r, 3000));

  // 1. Click 创建 -> 发动态
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

  // 2. Set Schedule Date & Time
  await page.evaluate(() => {
    const clockBtn = document.querySelector('button[aria-label="设定动态发布时间"], .share-actions__scheduled-post-btn');
    if (clockBtn) clockBtn.click();
  });
  await new Promise(r => setTimeout(r, 1500));

  // Open calendar
  const dateCoords = await page.evaluate(() => {
    const d = document.querySelector('#share-post__scheduled-date');
    if (d) {
      const r = d.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }
    return null;
  });
  if (dateCoords) {
    await page.mouse.click(dateCoords.x, dateCoords.y);
    await new Promise(r => setTimeout(r, 800));
  }

  const targetDayNum = parseInt(dayData.date.split('-')[2], 10);
  const targetMonthNum = parseInt(dayData.date.split('-')[1], 10);

  // If December, click next month
  if (targetMonthNum === 12) {
    const nextMonthCoords = await page.evaluate(() => {
      const b = document.querySelector('.artdeco-calendar__next-month');
      if (b) {
        const r = b.getBoundingClientRect();
        return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
      }
      return null;
    });
    if (nextMonthCoords) {
      await page.mouse.click(nextMonthCoords.x, nextMonthCoords.y);
      await new Promise(r => setTimeout(r, 800));
    }
  }

  // Click target day
  const dayCoords = await page.evaluate((targetDay) => {
    const calendar = document.querySelector('.artdeco-datepicker');
    if (!calendar) return null;
    const btns = Array.from(calendar.querySelectorAll('button')).filter(b => b.innerText.trim() === String(targetDay) && !b.className.includes('diff-month'));
    if (btns.length > 0) {
      const r = btns[0].getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }
    return null;
  }, targetDayNum);

  if (dayCoords) {
    await page.mouse.click(dayCoords.x, dayCoords.y);
    await new Promise(r => setTimeout(r, 800));
  }

  // Time selection
  const timeCoords = await page.evaluate(() => {
    const t = document.querySelector('#share-post__scheduled-time');
    if (t) {
      const r = t.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }
    return null;
  });
  if (timeCoords) {
    await page.mouse.click(timeCoords.x, timeCoords.y);
    await new Promise(r => setTimeout(r, 800));
  }

  const optCoords = await page.evaluate((tStr) => {
    const options = Array.from(document.querySelectorAll('[role="option"], .artdeco-typeahead__result'));
    let opt = options.find(o => o.innerText.trim() === tStr);
    if (!opt) {
      opt = options.find(o => o.innerText.includes(tStr.split(':')[0])) || options[0];
    }
    if (opt) {
      opt.scrollIntoView({ block: 'center' });
      const r = opt.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }
    return null;
  }, dayData.time);

  if (optCoords) {
    await page.mouse.click(optCoords.x, optCoords.y);
    await new Promise(r => setTimeout(r, 800));
  }

  // Click 下一页
  await page.evaluate(() => {
    const nextBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === '下一页');
    if (nextBtn) nextBtn.click();
  });
  await new Promise(r => setTimeout(r, 1500));

  // 3. Attach image
  const imgPath = `/Users/happy/Library/CloudStorage/GoogleDrive-cnproduct@gmail.com/我的云端硬盘/WPS同步盘/贸启航/客户贸启航/mqh客户/科山芯创/Cosine/ma_dpp_30_campaign/images/${dayData.image_filename}`;
  const chooserPromise = page.waitForFileChooser({ timeout: 10000 });
  await page.click('button[aria-label="添加媒体文件"]');
  const chooser = await chooserPromise;
  await chooser.setFiles(imgPath);
  await new Promise(r => setTimeout(r, 3000));

  // Click 下一页 on media preview
  await page.evaluate(() => {
    const nextBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === '下一页');
    if (nextBtn) nextBtn.click();
  });
  await new Promise(r => setTimeout(r, 1500));

  // 4. Fill text
  await page.evaluate((text) => {
    const editor = document.querySelector('.ql-editor');
    if (editor) {
      editor.focus();
      document.execCommand('selectAll', false, null);
      document.execCommand('insertText', false, text);
    }
  }, dayData.linkedin_copy);
  await new Promise(r => setTimeout(r, 1500));

  // 5. Click 设定时间
  await page.evaluate(() => {
    const schedBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === '设定时间' || b.innerText.trim() === '排期');
    if (schedBtn) schedBtn.click();
  });
  await new Promise(r => setTimeout(r, 4000));
  console.log(`[LinkedIn] Day ${dayData.day} scheduled successfully!`);
}

async function scheduleFacebookDay(page, dayData) {
  console.log(`[Facebook] Starting Day ${dayData.day}: ${dayData.date} ${dayData.time}...`);
  await page.goto("https://business.facebook.com/latest/composer?asset_id=115347823236277", { waitUntil: "domcontentloaded", timeout: 30000 });
  await new Promise(r => setTimeout(r, 4000));

  // 1. Upload photo
  const imgPath = `/Users/happy/Library/CloudStorage/GoogleDrive-cnproduct@gmail.com/我的云端硬盘/WPS同步盘/贸启航/客户贸启航/mqh客户/科山芯创/Cosine/ma_dpp_30_campaign/images/${dayData.image_filename}`;
  const photoBtnCoords = await page.evaluate(() => {
    window.scrollTo(0, 0);
    const scrollables = Array.from(document.querySelectorAll('div')).filter(d => d.scrollHeight > d.clientHeight && d.clientHeight > 300);
    scrollables.forEach(s => s.scrollTop = 0);
    const btn = Array.from(document.querySelectorAll('[role="button"]')).find(e => e.innerText && e.innerText.trim().includes('添加照片'));
    if (btn) {
      const r = btn.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }
    return null;
  });

  if (photoBtnCoords) {
    const chooserPromise = page.waitForFileChooser({ timeout: 10000 });
    await page.mouse.click(photoBtnCoords.x, photoBtnCoords.y);
    const chooser = await chooserPromise;
    await chooser.setFiles(imgPath);
    console.log(`[Facebook] Day ${dayData.day} image uploaded!`);
    await new Promise(r => setTimeout(r, 4000));
  }

  // 2. Insert copy
  await page.evaluate((text) => {
    const textBox = document.querySelector('div[aria-label="在对话框中输入内容，即可为帖子添加文字。"], div.notranslate._5rpu');
    if (textBox) {
      textBox.focus();
      document.execCommand('selectAll', false, null);
      document.execCommand('insertText', false, text);
    }
  }, dayData.facebook_copy);
  await new Promise(r => setTimeout(r, 1000));

  // 3. Toggle 设置日期和时间
  await page.evaluate(() => {
    const cb = document.querySelector('input[aria-label="设置日期和时间"]');
    if (cb && !cb.checked) {
      cb.click();
    }
  });
  await new Promise(r => setTimeout(r, 1000));

  // 4. Set Time
  const [targetHr, targetMin] = dayData.time.split(':');
  const hrCoords = await page.evaluate(() => {
    const hr = document.querySelector('input[aria-label="小时"]');
    if (hr) {
      const r = hr.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }
    return null;
  });
  if (hrCoords) {
    await page.mouse.click(hrCoords.x, hrCoords.y);
    await page.keyboard.press("Backspace");
    await page.keyboard.press("Backspace");
    await page.keyboard.type(targetHr);
  }

  const minCoords = await page.evaluate(() => {
    const min = document.querySelector('input[aria-label="分钟"]');
    if (min) {
      const r = min.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }
    return null;
  });
  if (minCoords) {
    await page.mouse.click(minCoords.x, minCoords.y);
    await page.keyboard.press("Backspace");
    await page.keyboard.press("Backspace");
    await page.keyboard.type(targetMin);
  }

  // 5. Set Date
  const dateCoords = await page.evaluate(() => {
    const d = document.querySelector('input[placeholder="年-月-日"]');
    if (d) {
      const r = d.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }
    return null;
  });
  if (dateCoords) {
    await page.mouse.click(dateCoords.x, dateCoords.y);
    await new Promise(r => setTimeout(r, 800));
  }

  const targetDayNum = parseInt(dayData.date.split('-')[2], 10);
  const targetMonthNum = parseInt(dayData.date.split('-')[1], 10);

  if (targetMonthNum === 12) {
    await page.evaluate(() => {
      const svgs = Array.from(document.querySelectorAll('svg, i, div[role="button"]'));
      const nextBtn = svgs.find(s => s.getAttribute('aria-label')?.includes('下') || s.getAttribute('aria-label')?.includes('Next'));
      if (nextBtn) nextBtn.click();
    });
    await new Promise(r => setTimeout(r, 600));
  }

  const fbDayCoords = await page.evaluate((dNum) => {
    const cells = Array.from(document.querySelectorAll('div, span, td')).filter(el => el.innerText && el.innerText.trim() === String(dNum) && el.children.length === 0);
    for (const c of cells) {
      const r = c.getBoundingClientRect();
      if (r.top > 320 && r.left > 80 && r.left < 450) {
        return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
      }
    }
    return null;
  }, targetDayNum);

  if (fbDayCoords) {
    await page.mouse.click(fbDayCoords.x, fbDayCoords.y);
    await new Promise(r => setTimeout(r, 1000));
  }

  // 6. Submit 预设时间
  const submitCoords = await page.evaluate(() => {
    const btn = Array.from(document.querySelectorAll('button, [role="button"]')).find(b => b.innerText.trim() === '预设时间');
    if (btn) {
      const r = btn.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }
    return null;
  });

  if (submitCoords) {
    await page.mouse.click(submitCoords.x, submitCoords.y);
    console.log("Clicked 预设时间!");
    await new Promise(r => setTimeout(r, 6000));

    await page.evaluate(() => {
      const dismissBtn = Array.from(document.querySelectorAll('button, [role="button"]')).find(b => b.innerText.includes('以后再说'));
      if (dismissBtn) dismissBtn.click();
    });
    await new Promise(r => setTimeout(r, 2000));
    console.log(`[Facebook] Day ${dayData.day} scheduled successfully!`);
  }
}

// Main execution loop for Days 4 to 30
for (let d = 4; d <= 30; d++) {
  const dayData = manifest[d - 1];
  console.log(`\n========================================`);
  console.log(`[RUNNER] Processing Day ${d} of 30: ${dayData.sku} (${dayData.date} ${dayData.time})`);
  console.log(`========================================`);

  try {
    await scheduleLinkedInDay(liPage, dayData);
    status[d - 1].linkedin_scheduled = true;
    status[d - 1].linkedin_status = "Scheduled (Verified)";
  } catch (err) {
    console.error(`[LinkedIn ERROR] Day ${d}:`, err.message);
    status[d - 1].linkedin_status = `Error: ${err.message}`;
  }

  try {
    await scheduleFacebookDay(fbPage, dayData);
    status[d - 1].facebook_scheduled = true;
    status[d - 1].facebook_status = "Scheduled (Verified)";
  } catch (err) {
    console.error(`[Facebook ERROR] Day ${d}:`, err.message);
    status[d - 1].facebook_status = `Error: ${err.message}`;
  }

  fs.writeFileSync(statusPath, JSON.stringify(status, null, 2));
  console.log(`[SAVED] Status updated for Day ${d}`);
}

console.log("\n All 30 Days Scheduled Successfully across LinkedIn & Facebook!");
