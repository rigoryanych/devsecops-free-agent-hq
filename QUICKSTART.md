QUICKSTART.md# Quick Start Guide

## For New Contributors

### Prerequisites
- Python 3.11+
- Git
- Docker (optional)

### Local Setup

```bash
# Clone repository
git clone https://github.com/rigoryanych/devsecops-free-agent-hq.git
cd devsecops-free-agent-hq

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running Tests Locally

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_python.py -v

# With coverage
python -m pytest tests/ --cov=. --cov-report=html
```

### Security Scanning Locally

```bash
# Bandit (Python security)
bandit -r . -f json -o bandit-report.json

# CodeQL (if installed)
codeql database create --language python --source-root . db
codeql database analyze db javascript.ql --format=sarif-latest
```

### Submitting a Pull Request

1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes and commit: `git commit -m "feat: Your feature"`
3. Push to your fork: `git push origin feature/your-feature`
4. Open PR on GitHub - automated checks will run
5. Address any feedback from automated reviews
6. Merge once all checks pass

### Troubleshooting

**Q: My PR checks are failing**  
A: Check the Actions tab for specific failure details. Common issues:
- Code quality issues: Review AI Code Review suggestions
- Security vulnerabilities: Check Trivy and CodeQL findings
- Test failures: Run tests locally first

**Q: How do I fix security findings?**  
A: See [SECURITY.md](./SECURITY.md) for security scanning details

**Q: Where's the documentation?**  
A: See [DEVOPS_SETUP_GUIDE.md](./DEVOPS_SETUP_GUIDE.md) and [CONTRIBUTING.md](./CONTRIBUTING.md)

### Resources
- [Main README](./README.md)
- [Security Policy](./SECURITY.md)
- [DevOps Guide](./DEVOPS_SETUP_GUIDE.md)
- [Contributing Guidelines](./CONTRIBUTING.md)
