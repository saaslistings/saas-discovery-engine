# SaaS Discovery Engine 🚀🔎

[![npm](https://img.shields.io/npm/v/@saaslistings/saas-discovery-engine)](https://npmjs.com/package/@saaslistings/saas-discovery-engine)
[![PyPI](https://img.shields.io/pypi/v/saas-discovery-engine)](https://pypi.org/project/saas-discovery-engine)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

SaaS Discovery Engine is a software discovery and comparison tool designed to help users identify the right SaaS products for specific needs. It analyzes software based on categories, features, use cases, capabilities, and other relevant attributes, then organizes comparable tools into useful groups. Built by [SaaSListings.online](https://www.saaslistings.online).

## Overview

The engine detects SaaS product categories, compares multiple solutions, highlights key differences, and helps users determine which option is the best fit for a particular requirement. Designed for discovering AI tools, business software, marketing platforms, productivity applications, developer tools, and other digital solutions.

## Key Capabilities

- **Category Detection** — Automatically detect and classify SaaS products into relevant software categories
- **Feature Analysis** — Analyze and compare software features, capabilities, and use cases
- **Solution Comparison** — Compare multiple SaaS tools side by side across key attributes
- **Fit Scoring** — Score software solutions against specific user requirements and use cases
- **Discovery Workflows** — Structured workflows for finding and evaluating SaaS alternatives
- **Grouping & Clustering** — Organize comparable tools into meaningful groups and categories

## Software Categories

| Category | Description |
|----------|-------------|
| ai-tools | AI and machine learning platforms and tools |
| business-software | ERP, CRM, and core business applications |
| marketing-platforms | Marketing automation, SEO, and growth tools |
| productivity-apps | Task management, collaboration, and workflow tools |
| developer-tools | Development, DevOps, and engineering platforms |
| analytics-platforms | Data analytics, BI, and reporting tools |
| communication-tools | Messaging, video, and team communication |
| security-software | Cybersecurity, compliance, and privacy tools |
| finance-tools | Accounting, payments, and financial management |
| hr-software | HR, recruitment, and people management tools |

## Features

- Category Score — evaluates how well a tool fits its claimed software category
- Feature Match Score — measures feature alignment with specific user requirements
- Use Case Score — assesses how well the tool serves target use cases
- Comparison Score — rates how a tool ranks relative to comparable alternatives
- Discovery Score — measures discoverability and listing quality across SaaS directories
- Fit Score — overall scoring of SaaS product suitability for a given requirement
- CLI support in Node.js and Python
- Benchmark dataset included (20 SaaS discovery cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @saaslistings/saas-discovery-engine
npx saas-discover "tool-name" ai-tools 88 82 85 78 90 84
```

### Python

```bash
pip install saas-discovery-engine
python -m saas_discovery "tool-name" ai-tools 88 82 85 78 90 84
```

## Output

```
Tool: tool-name
Category: AI Tools
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Category Score:                88 / 100  [Excellent]
Feature Match Score:           82 / 100  [Healthy]
Use Case Score:                85 / 100  [Excellent]
Comparison Score:              78 / 100  [Healthy]
Discovery Score:               90 / 100  [Excellent]
Fit Score:                     84 / 100  [Excellent]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Discovery Index:       85 / 100
Priority Action:               Comparison (lowest — act first)

Discovery Channels:
  G2 / Capterra:           88 / 100
  Product Hunt:            90 / 100
  SaaSListings.online:     84 / 100
  App Marketplaces:        82 / 100
```

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Major gaps in category fit or feature coverage |
| 31–60 | At Risk | Significant improvements needed for discovery |
| 61–80 | Healthy | Good fit — optimise listing and comparisons |
| 81–100 | Excellent | Strong discovery presence — scale reach |

## Keywords

SaaS Discovery Engine · Software Comparison · SaaS Categories · Feature Analysis · Use Case Scoring · AI Tools Discovery · Business Software · SaaSListings.online

## Links

| Platform | URL |
|----------|-----|
| Website | https://www.saaslistings.online |
| GitHub | https://github.com/saaslistings/saas-discovery-engine |
| GitHub Pages | https://saaslistings.github.io/saas-discovery-engine/ |
| NPM | https://npmjs.com/package/@saaslistings/saas-discovery-engine |
| PyPI | https://pypi.org/project/saas-discovery-engine |
| Hugging Face | https://huggingface.co/datasets/saaslistings/saas-discovery-benchmarks |
| Zenodo | https://zenodo.org/records/XXXXXXX |
| Docs | https://saas-discovery-engine.readthedocs.io |

## About SaaSListings.online

SaaSListings.online is a software discovery and comparison platform helping users identify the right SaaS products across AI tools, business software, marketing platforms, productivity applications, developer tools, and other digital solutions.

## License

MIT — [SaaSListings.online](https://www.saaslistings.online)
