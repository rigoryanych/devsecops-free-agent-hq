# 🔐 DevSecOps Free Agent HQ

> Enterprise-Grade Security Automation Stack - 100% Free Tier

## 📊 Overview

A complete DevSecOps implementation using free-tier tools and services. This repository demonstrates automated security scanning, AI-powered code review, and continuous monitoring without any cost.

## ✨ Features

- 🤖 **AI-Powered Code Review** - Automated security analysis using Hugging Face
- 🔒 **Security Scanning** - Trivy vulnerability scanning on every push
- 📈 **Code Analysis** - CodeQL static analysis for security issues
- 🏥 **Health Monitoring** - Weekly automated repository health checks
- 🔔 **Smart Alerts** - Zapier integration for email notifications
- 📋 **Task Management** - ClickUp automation for security workflows
- 🤝 **Dependabot** - Automated dependency updates and security patches

## 🛠️ Tech Stack

| Tool | Purpose | Status |
|------|---------|--------|
| GitHub Actions | CI/CD & Workflows | ✅ Active |
| Trivy | Container Scanning | ✅ Active |
| CodeQL | Static Analysis | ✅ Active |
| Hugging Face | AI Code Review | ✅ Active |
| Zapier | Automation | ✅ Active |
| ClickUp | Task Management | ✅ Active |
| Dependabot | Dependency Updates | ✅ Active |

## 🚀 Workflows

### 1. Security Scanning (`security.yml`)
- Runs on every push to main
- Trivy scans for vulnerabilities
- CodeQL analyzes code for security issues
- Results posted to Security tab

### 2. AI Code Review (`ai-code-review.yml`)
- Triggers on Pull Requests
- AI-powered security analysis
- Automated PR comments with review results
- Powered by Hugging Face API

### 3. Health Check (`health-check.yml`)
- Runs weekly (Mondays 9 AM UTC)
- Checks repository health metrics
- Monitors workflow status
- Reviews security alerts

## 📦 Setup

### Prerequisites
1. GitHub repository with Actions enabled
2. Hugging Face account and API token
3. (Optional) Zapier account for notifications
4. (Optional) ClickUp account for task management

### Configuration

1. **Add Secrets**
   ```
   GitHub Settings → Secrets and variables → Actions
   Required: HF_API_TOKEN (Hugging Face API token)
   ```

2. **Enable Dependabot**
   ```
   GitHub Settings → Security & analysis
   Enable: Dependabot alerts, security updates, and version updates
   ```

3. **Configure Workflows**
   All workflow files are in `.github/workflows/`

## 📚 Documentation

- [Workflow Details](/.github/workflows/) - See individual workflow files
- [Security Scanning](https://github.com/aquasecurity/trivy) - Trivy documentation
- [Code Analysis](https://codeql.github.com/) - CodeQL documentation

## 🎯 Cost

**Total: $0/month** (All free tier services)

## 📝 License

MIT License - Feel free to use and modify

## 🤝 Contributing

Contributions welcome! Please read the contributing guidelines first.

---

_Powered by GitHub Actions, Trivy, CodeQL, Hugging Face, and other free-tier tools_


---

## Advanced Customisation - AuditorSEC Edition v2.0

### New Workflows (2026)

| Workflow | Type | Description |
|----------|------|-------------|
| `security-advanced.yml` | Upgraded | Real Snyk OSS + SAST + GitGuardian (ggshield) + CodeQL matrix + OPA policy check + Zapier alert |
| `ai-code-review.yml` | Upgraded | Real HF Inference API (Mistral-7B) + PQC/crypto deprecated pattern detection + PR comment |
| `governance-policy-check.yml` | NEW | OPA/Rego policy enforcement + secrets audit + ISO 27001/NIS2/CISA compliance mapping |
| `pqc-hardening-check.yml` | NEW | FIPS-203/204/205 deprecated crypto scan + PQC adoption scoring + Bakhmach Protocol roadmap |

### Required Secrets

```
HF_API_TOKEN         # Hugging Face Inference API
SNYK_TOKEN           # Snyk vulnerability scanning
GITGUARDIAN_API_KEY  # GitGuardian secret detection
CLICKUP_API_TOKEN    # ClickUp task automation
ZAPIER_WEBHOOK_URL   # Critical alert notifications
```

Add via: **GitHub Settings → Secrets and variables → Actions**

### PQC Hardening Roadmap (Bakhmach Protocol)

| Work Package | Algorithm | Target Platform | FIPS Standard |
|-------------|-----------|-----------------|---------------|
| WP1 | ML-KEM (CRYSTALS-Kyber) | ESP32 firmware | FIPS-203 |
| WP2 | ML-DSA (CRYSTALS-Dilithium) | Firmware signing | FIPS-204 |
| WP3 | Causal AI false-alarm reduction | IoT sensors | N/A |
| WP4 | Field test + audit report | Bakhmach deployment | All |

### Governance Layer

- **OPA/Rego** policy packs enforce: explicit permissions, pinned action versions, no hardcoded secrets
- **Compliance mapping**: ISO 27001 A.8.x, NIS2 Art.21, CISA Secure by Design
- **Secrets audit**: all 5 required secrets tracked per run
- Policy violations block PR merges; all results posted as PR comments and GitHub Step Summary

### Documentation

- [Advanced Customised Recommendations](./ADVANCED_CUSTOMISED_RECOMMENDATIONS.md) - Full v2.0 strategy
- [Implementation Roadmap](./IMPLEMENTATION_ROADMAP.md) - Enhancement task list
- [Enhancements Complete](./ENHANCEMENTS_COMPLETE.md) - Completed items

---

*AuditorSEC DevSecOps Orchestrator — 2026-03-17 | Bakhmach, UA*
