# API Auth Examples

Example implementations of REST APIs with user registration and token (JWT)
based login.

* Flask - [source code](flask) | [demo app](http://api-auth-flask.herokuapp.com)
* Ruby on Rails - [source code](rails) | [demo app](http://api-auth-rails.herokuapp.com)

## About Json Web Tokens (JWT)

The JWT tokens have three parts - `header.claims.signature` and are base 64 encoded
as indicated by this pseudo code:

```
var headers = base64URLencode(myHeaders);
var claims = base64URLencode(myClaims);
var payload = header + "." + claims;

var signature = base64URLencode(HMACSHA256(payload, secret));

var encodedJWT = payload + "." + signature;
```

"The most important thing about JSON Web Tokens is that they are signed. This ensures the claims have not been tampered with when stored and passed between your service and another service."

"Do not contain any sensitive data in a JWT. These tokens are usually signed to protect against manipulation (not encrypted) so the data in the claims can be easily decoded and read"

The most common algorithm for signing JWT tokens is HS256 (HMAC + SHA256).
The header algorithm used is indicated in the header.

The claims is typically JSON info about the user and also contain an `ext` property
with the Unix time indicating when the token should expire.

## Glossary

* [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token) - "JSON Web Token (JWT, pronounced /dʒɒt/[1]) is a JSON-based open standard (RFC 7519) for creating access tokens that assert some number of claims. For example, a server could generate a token that has the claim "logged in as admin" and provide that to a client. The client could then use that token to prove that it is logged in as admin. The tokens are signed by the server's key, so the client and server are both able to verify that the token is legitimate. The tokens are designed to be compact, URL-safe and usable especially in web browser single sign-on (SSO) context.".
* [SHA and SHA-256](http://www.xorbin.com/tools/sha256-hash-calculator) - "The SHA (Secure Hash Algorithm) is one of a number of cryptographic hash functions. A cryptographic hash is like a signature for a text or a data file. SHA-256 algorithm generates an almost-unique, fixed size 256-bit (32-byte) hash. Hash is a one way function – it cannot be decrypted back. This makes it suitable for password validation, challenge hash authentication, anti-tamper, digital signatures."
* [HMAC](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code) - "In cryptography, a keyed-hash message authentication code (HMAC) is a specific type of message authentication code (MAC) involving a cryptographic hash function and a secret cryptographic key. It may be used to simultaneously verify both the data integrity and the authentication of a message, as with any MAC"
* [bcrypt](https://en.wikipedia.org/wiki/Bcrypt) - a password hashing function that is resistant to brute-force search attacks. Used by OpenBSD and some Linux flavors.
* [Base64](https://en.wikipedia.org/wiki/Base64) -  binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representation. The particular set of 64 characters chosen to represent the 64 place-values for the base varies between implementations. Base64 tokens in URLs need to be URL encoded since they can contain "/".

## Resources

* [jwt.io - decode, verify, generate JWT](https://jwt.io) (provieded by Auth0)
* [Introduction to JSON Web Tokens](https://jwt.io/introduction)
* [Use JWT The Right Way!](https://stormpath.com/blog/jwt-the-right-way)
* [On JWT Encryption with HS256 (HMAC with SHA-256)](https://stackoverflow.com/questions/39239051/rs256-vs-hs256-whats-the-difference)

Authentication as a Service:

* [Authentication databases and services](https://futurice.com/blog/authentication-databases-and-services)
* [Auth0](https://auth0.com) (see [Auth0 - Python](https://github.com/auth0/auth0-python))
* [Okta](https://developer.okta.com)
* [AuthRocket](https://authrocket.com)

Deployment:

* [Pushing a subtree to Heroku](https://stackoverflow.com/questions/5977234/how-can-i-push-a-part-of-my-git-repo-to-heroku)
