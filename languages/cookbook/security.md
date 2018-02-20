# Security

## Creating a Random UUID Digest

JavaScript/Node.js:

```javascript
const crypto = require('crypto')

function digest(data) {
  data = (data || Math.random()).toString()
  return crypto.createHash('md5').update(data).digest("hex")
}

// Alternative implementation with sha1 and time and without argument:
function digest() {
  const time = (new Date()).valueOf().toString()
  const random = Math.random().toString()
  return crypto.createHash('sha1').update(time + random).digest("hex")
}
```

Clojure:

```clojure
(ns versioned.util.digest
  (:import java.security.MessageDigest
           java.math.BigInteger))

(defn md5 [s]
  (let [algorithm (MessageDigest/getInstance "MD5")
        size (* 2 (.getDigestLength algorithm))
        raw (.digest algorithm (.getBytes s))
        sig (.toString (BigInteger. 1 raw) 16)
        padding (apply str (repeat (- size (count sig)) "0"))]
    (str padding sig)))

(defn generate []
  (md5 (str (new java.util.Date) (rand-int 1000000))))
```
