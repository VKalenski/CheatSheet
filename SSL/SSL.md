SSL Certificate

openssl genrsa -aes256 -out ca-key.pem 4096

> **Create SSL certificate:**
```
openssl req -new -x509 -sha256 -days 365 -key ca-key.pem -out ca.pem
```

*This is the information which must fill:*
- Enter the pass phrase for ca-key.pem: **empty**
- Country Name (2 letter code) [AU]: **empty**
- State or Province Name (full name) [Some-State]: **empty**
- Locality Name (eg. city) []: **empty**
- Organization Name (eg, company) [Internet Widgits Pty Ltd]: CL Creative
- Organizational Unit Name (eg, section) []: **empty**
- Common Name (e.g. server FQDN or YOUR Name) []: **empty**
- Email Address []: **empty**

> **View the certificate:**
```
openssl x509 -in ca.pem -text
```

> **Generate SSL:**
```
openssl genrsa -out cert-key.pem 4096
```

openssl req -new -sha256 -subj "/CN=clcreative" key cert-key.pem -out cert.csr