# Contributing

Thank you for contributing!

## How to Contribute

1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Submit a pull request

## Automated Checks

Your PR will trigger:
- AI Code Review
- Security Scanning
- CodeQL Analysis

## Guidelines

- Write clear commit messages
- Test your changes
- Update documentation

Thank you!

## Workflow Verification (✅ Verified - November 24, 2025)

All automated workflows have been tested and verified to be functioning correctly:

### ✅ Workflow Status

- **AI Code Review with Hugging Face** - WORKING
  - Trigger: Pull Request events
  - Status: Passing
  - Runtime: ~7 seconds
  - Features: Automated code analysis, security recommendations

- **Security Scan - Trivy** - WORKING  
  - Trigger: Pull Request events
  - Status: Passing
  - Runtime: ~15 seconds
  - Features: Container and dependency vulnerability scanning

- **CodeQL Analysis** - WORKING
  - Trigger: Dynamic
  - Status: Passing  
  - Runtime: ~49 seconds
  - Features: Code quality analysis, security pattern detection

### What to Expect in Your PR

When you submit a pull request, the following will happen automatically:

1. All three workflows will be triggered
2. Status checks will appear in the PR
3. AI Code Review will post automated comments with recommendations
4. Security vulnerabilities (if any) will be reported
5. Code quality metrics will be analyzed

### Workflow Execution Times

- Total time for all workflows to complete: ~70 seconds
- All checks must pass before merge
- Branch protection is recommended for main

Thank you for contributing to DevSecOps Free Agent HQ!
