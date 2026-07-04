# Sprint 1 - URL Validator

## Problem
What problem does this module solve?

## Design Decisions
- Why return `(True, url)` and `(False, None)`?
- Why normalize before validation?
- Why add `https://`?
- Why remove `www.`?
- Why reject email addresses?
- Why accept IP addresses?

## Mistakes I Made
email  checking,url suitable for project was not fully made

## What I Learned
Functions 

# Sprint 2

## What I learned
- DNS converts domain names to IP addresses.
- socket.gethostbyname() performs DNS lookup.
- urlparse() extracts the hostname.
- Always fail early.
- Use try/except for network operations.

## Mistakes I made
- Forgot to check if hostname was None.
- Forgot to return (True, ip_address).