# Passlib Documentation & Common Use Cases

## Overview

[Passlib](https://passlib.readthedocs.io/) is a password hashing library for Python, designed to make it easy to store hashed passwords securely. It supports a wide range of secure hashing algorithms and is commonly used in authentication systems.

---

## Installation

```bash
pip install passlib
```

---

## Basic Usage

### Hashing a Password
Hashing is the process of converting a password into a fixed-length string using a cryptographic algorithm. This is essential for securely storing passwords in a database.
```python
from passlib.context import CryptContext

# Create a CryptContext with the desired hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash a password
password = "my_secure_password"
hashed_password = pwd_context.hash(password)

print("Hashed Password:", hashed_password)
```

### Verifying a Password

```python
# Verify a password
provided_password = "my_secure_password"
is_valid = pwd_context.verify(provided_password, hashed_password)

if is_valid:
    print("Password is correct!")
else:
    print("Invalid password!")
```

### Using Multiple Hashing Schemes
You can configure `Passlib` to use multiple hashing schemes, allowing you to upgrade your password hashing strategy over time without breaking existing passwords.

```python
pwd_context = CryptContext(
    schemes=["bcrypt", "sha256_crypt", "md5_crypt"],
    default="bcrypt",
    deprecated="auto"
)

# Hash using the default scheme (bcrypt)
hashed_password = pwd_context.hash("my_secure_password")

# Verify against multiple schemes
is_valid = pwd_context.verify("my_secure_password", hashed_password)
print("Password is valid:", is_valid)
```
---

### Rehashing Passwords
As security standards evolve, you may need to rehash passwords with stronger algorithms. `Passlib` provides a way to check if a password needs rehashing.

```python
# Check if a password needs rehashing
if pwd_context.needs_rehash(hashed_password):
    new_hashed_password = pwd_context.hash(provided_password)
    print("Password rehashed:", new_hashed_password)
```
### Customizing Hashing Parameters
You can customize parameters like the bcrypt work factor to control the computational cost of hashing.

```python
pwd_context = CryptContext(
    schemes=["bcrypt"],
    bcrypt__rounds=12  # Increase the number of rounds for more security
)

hashed_password = pwd_context.hash("my_secure_password")
print("Hashed Password with custom rounds:", hashed_password)
```

---
### Storing and Retrieving Password Hashes
When storing a hashed password in a database, you can save it as a string. When retrieving it, you can directly use it for verification.

```python
# Store hashed password in the database
stored_hashed_password = pwd_context.hash("my_secure_password")

# Retrieve and verify
provided_password = "my_secure_password"
is_valid = pwd_context.verify(provided_password, stored_hashed_password)
print("Password is valid:", is_valid)
```

### Using Argon2 (Advanced Hashing Algorithm)
Passlib supports Argon2, a modern and secure password hashing algorithm.

```python
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Hash a password using Argon2
hashed_password = pwd_context.hash("my_secure_password")
print("Argon2 Hashed Password:", hashed_password)

# Verify the password
is_valid = pwd_context.verify("my_secure_password", hashed_password)
print("Password is valid:", is_valid)
```



## References

- [Passlib Documentation](https://passlib.readthedocs.io/)
- [Passlib GitHub](https://github.com/serpentine/passlib)
