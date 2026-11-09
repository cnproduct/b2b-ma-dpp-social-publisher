# Meta Business Suite (Facebook) 排期与发帖自动化规范 (Verified Standard)

本文件记录在 Meta Business Suite 与 Facebook 官方公共主页中执行自动化发帖与排期的技术规范与防错避坑指南。

## 1. 核心路由与页面
- **Meta Business Suite Composer (官方发帖与排期主控器 - 推荐默认)**:
  `https://business.facebook.com/latest/composer?asset_id=[asset_id]`
- **Meta Business Suite 已发布帖子审计 (Published Posts)**:
  `https://business.facebook.com/latest/posts/published_posts?asset_id=[asset_id]`
- **Meta Business Suite 已定时帖子大盘 (Scheduled Posts)**:
  `https://business.facebook.com/latest/posts/scheduled_posts?asset_id=[asset_id]`
- **Meta Business Suite 日程本 (Planner / Calendar)**:
  `https://business.facebook.com/latest/content_calendar?asset_id=[asset_id]`
- **Facebook 官方主页前台动态流 (Public Live Feed)**:
  `https://www.facebook.com/[page_id]`

---

## 2. Composer (发帖器) 核心避坑与防错机制

### 2.1 视口规范 (Viewport Standardization)
- 在无头或小窗口模式下，Composer 视口常会被压缩到 `551x362` 等小尺寸，导致右侧实时预览区隐藏、按钮坐标错位。
- **强制规范**：在进入 Composer 之前，必须通过 CDP 或浏览器窗口将视口设置为标准 `1440x900`：
  ```javascript
  await page.cdp('Emulation.setDeviceMetricsOverride', {
    width: 1440,
    height: 900,
    deviceScaleFactor: 1,
    mobile: false
  });
  ```

### 2.2 照片/视频上传精准坐标
- Meta 界面中，“添加照片/视频”外层存在一个全宽度的卡片容器（宽度 500px+）。如果直接使用通用选择器点击外层元素中心，会点到右侧的空白区域导致文件弹窗无法唤起超时。
- **最佳实践**：点击左侧实际按钮区域（或相对于左侧偏移 50px）：
  ```javascript
  const photoBtnCoords = await page.evaluate(() => {
    window.scrollTo(0, 0);
    const scrollables = Array.from(document.querySelectorAll('div')).filter(d => d.scrollHeight > d.clientHeight && d.clientHeight > 300);
    scrollables.forEach(s => s.scrollTop = 0);
    const btn = Array.from(document.querySelectorAll('[role="button"], button, div, span')).find(e => e.innerText && (e.innerText.trim() === '添加照片/视频' || e.innerText.trim() === '添加照片'));
    if (btn) {
      const r = btn.getBoundingClientRect();
      return { x: r.left + 50, y: r.top + r.height / 2 };
    }
    return { x: 213, y: 376 }; // 1440x900 下的验证坐标
  });
  ```

### 2.3 严禁 `document.execCommand('insertText')`（空帖根因）
- **核心踩坑**：Meta Business Suite 的富文本编辑器基于 React + Draft.js / Lexical 架构。如果直接在 DOM 节点上执行 `document.execCommand('insertText')`，虽然 DOM 树上看似有字，但 **React 合成事件管道 (SyntheticEvent Pipeline) 与内部组件 state 根本没有触发更新**！
- **后果**：表单提交时，React 序列化其内部的空字符串 `""`，直接导致生成只带图片、没有文字的帖子，在 Meta 大盘显示为 **“这篇帖子没有文字内容”**！
- **强制标准**：必须使用自动化测试框架的原生输入事件通道：
  ```javascript
  // 使用 Playwright/ego-browser 的原生 page.fill
  await page.fill('div.notranslate._5rpu, [contenteditable="true"]', fullCopy);
  await new Promise(r => setTimeout(r, 1500));

  // 补发 Escape 并点击空白区域，关闭标签联想菜单
  await page.keyboard.press("Escape");
  await page.evaluate(() => {
    const label = document.querySelector('div[aria-label="发布位置"]');
    if (label) label.click();
  });
  ```
- **发布前校验**：提交前必须在 DOM 级校验文字长度（`textLength > 50`），否则强制抛出异常阻断发布，杜绝任何空帖外流！

### 2.4 完整图文与标签规范 (Full Text + Image + Tags)
- Facebook 发布的帖子必须与 LinkedIn 严格看齐，包含四层完整结构：
  1. **主标题与行业勾子**：例如 `[Day X/30: Cosine Semiconductor MA-DPP Series] ⚡`
  2. **合规背景与技术亮点**：EU ESPR 2024/1781 准入、Node 100015 (ISO/IEC 15459) 去中心化数字标识、SHA-256 哈希认证。
  3. **落地页网址与样品申领通道**：`https://www.cosinechips.com/ma-dpp`
  4. **完整的社媒标签矩阵**：`#CosineChips #MADPP #Semiconductor #ElectronicsEngineering #SmartGrid #Robotics #RoHS #ISO15459`
  5. **1200x1350 高清专业信息图附件**。

### 2.5 定时排期防直发硬屏障 (Schedule Verification Guard)
- 在排期模式下，勾选“设置日期和时间”后，底部的提交按钮必须从蓝色的“发布”变成“预设时间”。
- **防直发硬校验**：在点击提交之前，必须检测按钮文本：
  ```javascript
  const btnType = await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button, [role="button"]'));
    if (btns.some(b => b.innerText && b.innerText.trim() === '预设时间')) return '预设时间';
    if (btns.some(b => b.innerText && b.innerText.trim() === '发布')) return '发布';
    return 'unknown';
  });

  if (btnType !== '预设时间') {
    throw new Error(`[Facebook ERROR] Expected button to be '预设时间' for scheduling, but found '${btnType}'. Aborting to prevent accidental immediate publishing!`);
  }
  ```
  如果发现按钮仍为“发布”，立即中断执行并报错，彻底杜绝排期脚本误直发！
