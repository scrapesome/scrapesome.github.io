# 🧰 scrapesome UI

A modern, responsive web interface for the [`scrapesome`](https://github.com/scrapesome/scrapesome) web scraping tool. Built with **TailwindCSS**, **FastAPI backend**, and a dynamic frontend that supports rendering scraped content as HTML, Markdown, JSON tables, or plain text.

![screenshot](https://raw.githubusercontent.com/scrapesome/scrapesome/main/docs/assets/images/favicon.png)

---

## 🚀 Features

- 🌐 Input any URL and scrape content instantly
- 🧠 Choose output format: **HTML**, **Markdown**, **JSON**, or **Text**
- ⏱ Set request timeout and toggle headless rendering (via Playwright)
- 🔄 Supports custom request headers and redirect behavior
- 🎨 Dark mode toggle
- 🔍 Live render of:
  - HTML → sandboxed in an `iframe`
  - Markdown → rendered via `marked.js`
  - JSON → dynamic tables
  - Text → preformatted block

---