; In Clojure, everything is an expression that returns a value
; Only the values nil and false are treated as false (falsy) in a boolean/conditional context

; The if operator takes and three arguments: test, then, else
(str "2 is " (if (even? 2) "even" "odd"))

; The else expression is optional
(if (true? false) "impossible!")

; if/do
; do has multiple expressions and returns the value of the last one

(if (even? 5)
  (do (println "even")
    true)
  (do (println "odd")
    false))

; if-let

(if-let [x (even? 3)]
  (println x)
  (println "some odd value"))

(defn show-evens [coll]
  (if-let [evens (seq (filter even? coll))]
    (println (str "The evens are:" evens))
    (println "There are no evens")))

; cond - a series of tests and expressions, :else expression is optional
(cond
  test1 expression1
  test2 expression2
  :else else-expression)

(let [x 5]
  (cond
    (< x 2) "x is less than 2"
    (< x 10) "x is less than 10")) ; => "x is less than 10"

; condp - cond with shared predicate
(defn foo [x]
  (condp = x
    5 "x is 5"
    10 "x is 10"
    "x isn't 5 or 10"))
(foo 11) ; => x isn't 5 or 10

; case - predivate always =, test values must be compile time literals, else has no test value
(defn foo [x]
  (case x
    5 "x is 5"
    10 "x is 10"
    "x isn't 5 or 10"))
(foo 11)

; doseq - iterates over a sequence (forEach)
(doseq [n (range 3)]
  (println n))

; while
(while (.accept socket)
  (handle socket))

; for (list comprehension / sequence genrator)
(for [x [0 1]
      y [0 1]]
  [x y]) ; => ([0 0] [0 1] [1 0] [1 1])

; loop/recur (similar to let but supports recur)
(loop [i 0]
  (if (< i 10)
    (recur (inc i))
    i)) ; => 10

; function recur (functions acting as loop)
(defn increase [i]
  (if (< i 10)
    (recur (inc i))
    i))
(increase 4) ; => 10

; recur must be in tail position (last statement in branch) for tail call ellimination to happen

; multi arity tail-recursive function
(defn factorial
  ([n] (factorial 1 n))
  ([accum n]
    (if (zero? n)
      accum
      (factorial (* accum n) (dec n)))))

(defn factorial
  ([n] (factorial 1 n))
  ([accum n]
    (if (zero? n)
      accum
      (recur (* accum n) (dec n)))))

; Exception handling
(try
  (/ 2 1)
  (catch ArithmeticException e
    "divide by zero"
  )
  (finally
    (println "cleanup")
  )
)

(try
  (throw (Exception. "something went wrong"))
  (catch Exception e (.getMessage e)))

; with-open
(require '[clojure.java.io :as io])
(with-open [f (io/writer "/tmp/new")]
  (.write f "some text"))
