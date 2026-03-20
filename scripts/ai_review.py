#!/usr/bin/env python3
"""AI Code Review script for AuditorSEC DevSecOps pipeline.
Called by ai-code-review.yml workflow (replaces YAML heredoc)."""
import os
import requests
import json
import sys

def main():
    hf_token = os.environ.get("HF_API_TOKEN", "")
    headers = {"Authorization": f"Bearer {hf_token}"}

    # Read changed files
    try:
        with open("changed_files.txt") as f:
            changed = [l.strip() for l in f if l.strip() and not l.startswith("No diff")]
    except Exception:
        changed = []

    # Collect code snippets from changed files (first 500 chars each)
    snippets = []
    for fname in changed[:5]:  # limit to 5 files
        try:
            with open(fname, "r", errors="ignore") as cf:
                content = cf.read(500)
                snippets.append(f"File: {fname}\n{content}")
        except Exception:
            pass

    code_context = "\n\n---\n\n".join(snippets) if snippets else "No code changes to review."

    prompt = (
        "You are an expert DevSecOps security auditor for AuditorSEC. "
        "Analyse the following code changes for:\n"
        "1. Security vulnerabilities (OWASP Top 10, injection, auth issues)\n"
        "2. Cryptographic weaknesses (MD5, SHA1, RSA<2048, DES, RC4)\n"
        "3. PQC readiness gaps (absence of ML-KEM/ML-DSA)\n"
        "4. Secrets/credentials exposure\n"
        "5. Input validation issues\n"
        "Provide findings as [CRITICAL], [HIGH], [MEDIUM], [LOW], [INFO]. "
        "If no issues found, say PASS.\n"
        f"Code changes:\n{code_context[:1200]}"
    )

    api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 512,
            "temperature": 0.2,
            "return_full_text": False
        }
    }

    try:
        if hf_token:
            resp = requests.post(api_url, headers=headers, json=payload, timeout=60)
            if resp.status_code == 200:
                result = resp.json()
                review_text = result[0].get("generated_text", "No output") if isinstance(result, list) else str(result)
            else:
                review_text = f"HF API returned status {resp.status_code}: {resp.text[:200]}"
        else:
            review_text = (
                "[WARN] HF_API_TOKEN not set - AI review skipped. "
                "Add HF_API_TOKEN secret to enable."
            )
    except Exception as e:
        review_text = f"[ERROR] AI review failed: {str(e)}"

    # Write review to file for next step
    with open("ai_review_result.txt", "w") as out:
        out.write(review_text)

    print("=== AI Review Output ===")
    print(review_text[:1000])


if __name__ == "__main__":
    main()
