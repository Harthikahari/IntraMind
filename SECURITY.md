# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

The IntraMind team takes security bugs seriously. We appreciate your efforts to responsibly disclose your findings.

### Where to Report

**DO NOT** report security vulnerabilities through public GitHub issues.

Instead, please report them to our security team:

- **Email**: security@intramind.ai
- **PGP Key**: [Download our PGP key](https://intramind.ai/security/pgp-key.asc)
- **Subject Line**: `[SECURITY] Brief description of vulnerability`

### What to Include

To help us better understand and resolve the issue, please include:

1. **Type of vulnerability** (e.g., SQL injection, XSS, authentication bypass)
2. **Full paths** of source file(s) related to the vulnerability
3. **Location** of the affected source code (tag/branch/commit or direct URL)
4. **Step-by-step instructions** to reproduce the issue
5. **Proof-of-concept or exploit code** (if possible)
6. **Impact** of the vulnerability and how it could be exploited
7. **Your contact information** for follow-up questions

### Example Report

```
Subject: [SECURITY] SQL Injection in User Authentication

Description:
The login endpoint is vulnerable to SQL injection through the username parameter.

Location:
- File: src/intramind/api/auth.py
- Function: authenticate_user()
- Lines: 45-52

Steps to Reproduce:
1. Navigate to /api/v1/auth/login
2. Submit the following payload in the username field: admin' OR '1'='1
3. Observe that authentication succeeds without valid credentials

Impact:
An attacker could bypass authentication and gain unauthorized access to any user account,
including administrator accounts.

Proof of Concept:
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin'\'' OR '\''1'\''='\''1", "password": "anything"}'

Suggested Fix:
Use parameterized queries instead of string concatenation for SQL statements.
```

## Response Timeline

We aim to respond to security reports according to the following timeline:

1. **Initial Response**: Within 48 hours of report submission
2. **Triage**: Within 5 business days
3. **Fix Development**: Depends on severity
4. **Release**: As soon as safely possible

### Severity Levels

We categorize vulnerabilities using CVSS v3.1:

| Severity | CVSS Score | Response Time | Example |
|----------|------------|---------------|---------|
| **Critical** | 9.0-10.0 | 24-48 hours | Remote code execution, authentication bypass |
| **High** | 7.0-8.9 | 1 week | SQL injection, XSS, privilege escalation |
| **Medium** | 4.0-6.9 | 2 weeks | Information disclosure, CSRF |
| **Low** | 0.1-3.9 | 1 month | Minor information leaks, low-impact DoS |

## Security Updates

Security updates are released through:

1. **GitHub Security Advisories**
2. **Email notifications** to registered users
3. **Release notes** with security fix details (after disclosure)
4. **Security mailing list**: security-announce@intramind.ai

### Subscribing to Security Updates

To receive security notifications:

```bash
# Subscribe to our security mailing list
echo "your-email@example.com" | mail -s "SUBSCRIBE" security-announce@intramind.ai
```

## Disclosure Policy

### Coordinated Disclosure

We follow a **coordinated disclosure** process:

1. **Report received** - We acknowledge receipt within 48 hours
2. **Validation** - We validate and reproduce the vulnerability
3. **Fix development** - We develop and test a fix
4. **Advance notice** - We notify you before public disclosure
5. **Public disclosure** - We publish advisory after fix is released

### Embargo Period

- We request a **90-day embargo** from initial report to public disclosure
- We may disclose earlier if the vulnerability is:
  - Already public
  - Being actively exploited
  - Affects end-user safety

### Public Disclosure

After a fix is released, we will:

- Publish a security advisory on GitHub
- Credit the reporter (unless anonymity is requested)
- Include CVE identifier (if applicable)
- Provide detailed mitigation steps

## Security Best Practices

### For Users

1. **Keep Updated**: Always use the latest version
2. **Secure Configuration**: Follow our [Security Configuration Guide](docs/guides/security-config.md)
3. **Environment Variables**: Never commit `.env` files
4. **API Keys**: Rotate keys regularly, use different keys for dev/prod
5. **HTTPS Only**: Always use TLS in production
6. **Rate Limiting**: Enable rate limiting to prevent abuse
7. **Monitoring**: Set up security monitoring and alerts

### For Developers

1. **Input Validation**: Validate and sanitize all user inputs
2. **Authentication**: Use strong authentication mechanisms
3. **Authorization**: Implement proper access controls
4. **Encryption**: Encrypt sensitive data at rest and in transit
5. **Dependencies**: Keep dependencies updated
6. **Secrets Management**: Never hardcode secrets
7. **Code Review**: Review all code for security issues
8. **Testing**: Include security tests in your test suite

### Configuration Security

```bash
# Good Practices
✓ Use strong, randomly generated secrets
✓ Enable HTTPS/TLS in production
✓ Set appropriate CORS policies
✓ Enable rate limiting
✓ Use environment variables for secrets
✓ Implement proper logging (without sensitive data)

# Bad Practices
✗ Using default or weak secrets
✗ Exposing internal APIs publicly
✗ Disabling security features in production
✗ Logging sensitive information
✗ Using development settings in production
```

## Security Features

IntraMind includes the following security features:

### Authentication & Authorization

- **JWT-based authentication**
- **API key authentication**
- **Role-based access control (RBAC)**
- **Multi-factor authentication (MFA)** support
- **OAuth 2.0** integration

### Data Protection

- **Encryption at rest** (AES-256)
- **Encryption in transit** (TLS 1.3)
- **Secure password hashing** (bcrypt)
- **Sensitive data masking** in logs
- **PII data protection**

### API Security

- **Rate limiting** per IP/user/endpoint
- **Request size limits**
- **CORS configuration**
- **Input validation**
- **SQL injection protection**
- **XSS protection**
- **CSRF protection**

### Monitoring & Logging

- **Security event logging**
- **Failed authentication tracking**
- **Anomaly detection**
- **Audit trails**
- **Real-time alerting**

## Vulnerability Response

### If You Discover a Vulnerability in Production

1. **Immediately rotate** any compromised credentials
2. **Document** what happened and what data may have been affected
3. **Report** to security@intramind.ai
4. **Preserve** logs and evidence
5. **Do not** publicly disclose until coordinated with our team

### If Your Installation is Compromised

1. **Isolate** the affected system
2. **Preserve** forensic evidence
3. **Review** access logs
4. **Rotate** all credentials and API keys
5. **Apply** latest security patches
6. **Report** the incident to security@intramind.ai

## Security Checklist

Before deploying IntraMind to production:

- [ ] All secrets are stored in environment variables
- [ ] `.env` file is in `.gitignore`
- [ ] HTTPS/TLS is enabled and properly configured
- [ ] Database credentials are strong and unique
- [ ] API keys are rotated and secured
- [ ] Rate limiting is enabled
- [ ] CORS is properly configured
- [ ] Logging is enabled (without sensitive data)
- [ ] Monitoring and alerting are set up
- [ ] Security headers are configured
- [ ] Dependencies are up to date
- [ ] Security tests are passing
- [ ] Backups are encrypted and tested
- [ ] Disaster recovery plan is in place

## Hall of Fame

We recognize security researchers who help keep IntraMind secure:

| Researcher | Vulnerability | Date | Severity |
|------------|---------------|------|----------|
| TBD | TBD | TBD | TBD |

*Want to be listed here? Report a valid security vulnerability!*

## Contact

- **Security Team**: security@intramind.ai
- **PGP Fingerprint**: `XXXX XXXX XXXX XXXX XXXX  XXXX XXXX XXXX XXXX XXXX`
- **Bug Bounty Program**: Coming soon

## Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [Our Security Documentation](docs/guides/security.md)

---

**Last Updated**: January 2025

Thank you for helping keep IntraMind and our users safe! 🔒
