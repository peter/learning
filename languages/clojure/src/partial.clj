; partial
; https://clojuredocs.org/clojure.core/partial

(def my-array [[1.1 1.2 1.3] [2.1 2.2 2.3] [3.1]])
(map (partial take 2) my-array) ; => ((1.1 1.2) (2.1 2.2) (3.1))

(def hundred-times (partial * 100))
(hundred-times 4 5 6) ; => 12000

((partial = 0) 0) ; => true

; compose
; https://clojuredocs.org/clojure.core/comp
(def concat-and-reverse (comp (partial apply str) reverse str))
(concat-and-reverse "hello" "clojuredocs") ;=> "scoderujolcolleh"

((comp str +) 8 8 8) ; => "24"

(filter (comp not zero?) [0 1 0 2 0 3 0 4])
