# JobAI — Landing Page

JobAI Chrome extension 嘅公開 landing 頁。

**Live:** https://kenx1992-sudo.github.io/jobai-landing/

## 內容

| 檔案 | 用途 |
|---|---|
| `index.html` | 整個 landing 頁,單一檔案,冇外部依賴(CSS 同貓 SVG 全部 inline) |
| `brand/cat-mascot.svg` | 工作貓 mascot 嘅 vector source |
| `brand/gen_cat_svg.py` | 生成上面個 SVG(幾何座標嘅 source of truth) |
| `brand/render_cat.py` | 用 Pillow 出 PNG 預覽,supersample 抗鋸齒 |

貓嘅幾何淨係定義喺 `gen_cat_svg.py` / `render_cat.py`。兩個 script 用同一組座標,
確保 SVG 同 PNG 唔會走樣。改隻貓就改 script,唔好直接手改 SVG。

```bash
cd brand
python gen_cat_svg.py    # → cat-mascot.svg
python render_cat.py     # → cat_preview.png
```

需要 Pillow(`render_cat.py` 先要,`gen_cat_svg.py` 唔使)。

## 相關 repo

- Extension source(private):`kenx1992-sudo/jobai-extension`
- 私隱政策(public):`kenx1992-sudo/jobai-extension-privacy` → https://kenx1992-sudo.github.io/jobai-extension-privacy/
- JobAI web app:https://job-ai-leap.base44.app

## 註

頁面文案取自 Chrome Web Store 上架文案(`商店文案.md`),唔應該同 store listing 講唔同嘢 ——
改文案記得兩邊一齊改。

Extension 未上架前,CTA 掣指向 JobAI web app;上架之後應該改返指向 Chrome Web Store。
