# LinkedIn Company Page 自动化规范与 DOM 逆向映射

本文件记录在 LinkedIn 公司主页 (Admin View) 中通过 `ego-browser` 执行无头/自动化操作的关键 DOM 选择器、事件触发机制与容错方案。

## 1. 核心路由与入口
- **公司主页管理后台**: `https://www.linkedin.com/company/[company_id]/admin/dashboard/`
- **动态管理入口**: 点击左上侧按钮包含 `创建` -> 展开菜单点击 `发动态`。
- **动态列表管理**: 点击左侧导航栏 `主页动态`，可查看 `已发布`、`已设定发布时间` 等分标签。

## 2. 交互节点与选择器表

| 操作步骤 | 目标元素说明 | 推荐定位方式 | 交互细节与避坑指南 |
|---|---|---|---|
| **开启排期** | 时钟图标按钮 | `button[aria-label="设定动态发布时间"]` 或 `.share-actions__scheduled-post-btn` | 点击后将打开发布时间设置对话框。 |
| **展开日历** | 日期输入框 | `#share-post__scheduled-date` | 点击后展开 Artdeco Calendar 浮层。 |
| **选择日期** | 日历中的具体日期单元 | `.artdeco-datepicker button` | 需过滤掉 `.artdeco-calendar-day-btn--diff-month`；必须使用 `page.mouse.click(x, y)` 物理坐标点击以触发 Ember 数据绑定。 |
| **切换下个月** | 日历右箭头 | `.artdeco-calendar__next-month` | 当排期时间跨入次月（如12月）时点击。 |
| **选择时间槽** | 时间输入框与下拉选项 | `#share-post__scheduled-time` | LinkedIn 支持 15 分钟槽位，点击后在 `[role="option"]` 中匹配目标时间（如 `09:15`, `14:30`）。 |
| **确认时间** | 下一步按钮 | `button:has-text("下一页")` | 确认时间后返回主发帖弹窗。 |
| **上传媒体** | 添加照片/媒体 | `button[aria-label="添加媒体文件"]` | 使用 `page.waitForFileChooser()` 拦截弹窗，传入本地绝对路径。 |
| **确认媒体** | 媒体预览确认按钮 | 媒体编辑界面的 `button:has-text("下一页")` | 点击后回到文案编写界面。 |
| **填写文案** | Quill 富文本输入区 | `.ql-editor` | 必须先执行 `editor.focus()`，再使用 `document.execCommand('insertText', false, text)` 填入，保留换行与 Emoji。 |
| **执行排期** | 排期提交按钮 | `button:has-text("设定时间")` 或 `button:has-text("排期")` | 提交后等待 3~5 秒，检测 `已设定动态发布时间` 提示条。 |
| **即时发布** | 直接发布按钮 | `button:has-text("发布")` | 在未开启定时状态下直接点击，帖子即刻上线。 |
