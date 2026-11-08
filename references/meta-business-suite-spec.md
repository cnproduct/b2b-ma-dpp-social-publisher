# Meta Business Suite (Facebook) 排期与发帖自动化规范

本文件记录在 Meta Business Suite 与 Facebook 官方公共主页中执行自动化发帖与排期的技术规范。

## 1. 核心路由与页面
- **Meta Business Suite Composer (发帖器)**:
  `https://business.facebook.com/latest/composer?asset_id=[asset_id]`
- **Meta Business Suite 日程本 (Planner)**:
  `https://business.facebook.com/latest/planner?asset_id=[asset_id]`
- **Facebook 官方主页前台管理界面**:
  `https://www.facebook.com/[page_id]`

## 2. Composer (发帖器) 自动化细节

### 2.1 照片/视频上传
- Meta 界面中，“添加照片/视频”外层存在一个全宽度的父容器（宽度通常 500px+）。如果使用通用选择器点击中心点，会点到右侧的空白区域导致文件弹窗无法唤起。
- **最佳实践**: 定位内部真正具备按钮属性的子节点：
  `document.querySelectorAll('[role="button"]')` 并检查 `innerText.includes("添加照片")`，获取其 BoundingClientRect 中心点后使用 `page.mouse.click(x, y)`。
- 通过 `page.waitForFileChooser()` 拦截并写入绝对路径。

### 2.2 文案填充
- 定位具有 `aria-label="在对话框中输入内容，即可为帖子添加文字。"` 的 `div` 元素（通常带 `.notranslate._5rpu` 类名）。
- 使用 `document.execCommand('selectAll')` + `document.execCommand('insertText', false, text)` 填入。

### 2.3 定时排期模式
1. 勾选开关：定位 `input[aria-label="设置日期和时间"]`，确保其处于 `checked` 状态。
2. 小时与分钟：定位 `input[aria-label="小时"]` 与 `input[aria-label="分钟"]`，使用键盘 Backspace 两次清空原有时间后输入目标两位数字。
3. 日期设置：点击 `input[placeholder="年-月-日"]` 展开日历，若跨月点击月份右箭头，并在单元格中定位对应日期的纯数字文本节点进行点击。
4. 提交排期：点击底部的 `预设时间` 按钮。
5. 营销弹窗规避：提交后 Meta 常会弹出“通过速推向更大规模的受众推广”弹窗，检测包含 `以后再说` 的按钮并点击关闭。

### 2.4 公共主页前台即时发布模式
- 当在主页前台 `https://www.facebook.com/[page_id]` 直接发帖时，点击 `分享新鲜事` 或 `照片/视频` 区域。
- 填入文案后点击 `下一页`，检查弹窗并点击 `发帖`。
- 若弹出“直接与用户对话（添加立即拨打按钮）”或“探索商品标记功能”，自动定位右上角 `[aria-label="关闭"]` 或点击 `以后再说` 完成发布闭环。
