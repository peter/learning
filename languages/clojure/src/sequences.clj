; Clojure provides the sequence abstraction for its collection data structures
; Used for iteration
; Can be backed by a data structure or a function (infinite/lazy sequences)

(def coll [1 2 3 4])

; Sequence API

(seq coll) ; If collection is non-empty then return seq object else return nil

(first coll)
(rest coll)
(cons 7 coll) ; new sequence with 7 first: (7 1 2 3 4)

; Sequences over functions
(def a-range (range 1 4))
(first a-range)
(second a-range)
(rest a-range)

(set! *print-length* 10) ; Number of items in sequence the REPL will print

; Generators create sequences
(range) ; infinte sequence (0 1 2 3 4 ...)
(iterate #(* 2 %) 2) ; => (2 4 8 16 ...)

(take 3 (range))
(drop 3 (range))
(map #(* % %) [0 1 2 3])
(filter even? (range))
(apply str (interpose "," (range 3)))

(reduce + (range 4))
(reduce + 10 (range 4))
(into #{} "hello")
(into {} [[:x 1] [:y 2]])
(some {2 :b 3 :c} [1 nil 2 3]) ; => :b (a map can be used as a function that takes a key as argument)

(re-seq #"[aeiou]" "clojure") ; => ("o" "u" "e")
