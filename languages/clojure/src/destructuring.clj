; Destructuring cheat sheet:
; https://gist.github.com/john2x/e1dca953548bfdfb9844

; Sequential destructuring (vectors and lists)
(def point [5 7])
(let [[x y] point]
         (println "x:" x "y:" y))

(def indexes [1 2 3])
(let [[x & more] indexes]
  (println "x:" x "more:" more))
(let [[x & more :as full-list] indexes]
  (println "x:" x "more:" more "full-list:" full-list))

; Associative destructuring (maps)
(def point {:x 5 :y 7})
(let [{x :x y :y} point]
         (println "x:" x "y:" y))
(let [{:keys [x y]} point]
         (println "x:" x "y:" y))
(let [{:keys [x y] :as the-point} point]
         (println "x:" x "y:" y "point:" the-point))
(def point {:y 7})
(let [{:keys [x y] :or {x 0 y 0}} point]
         (println "x:" x "y:" y))

; Destructuring nested maps
(def book {:name "SICP" :details {:pages 657 :isbn-10 "0262011530"}})
(let [{name :name {:keys [pages isbn-10]} :details} book]
         (println "name:" name "pages:" pages "isbn-10:" isbn-10))

; Destructuring arrays nested in maps
(def golfer {:name "Jim" :scores [3 5 4 5]})
(let [{name :name [hole1 hole2] :scores} golfer]
         (println "name:" name "hole1:" hole1 "hole2:" hole2))

; Skipping parts in a compound structure with underscore (idiom)
(def stuff [7 8 9 10 11])
(let [[_ & others] stuff] (println others))

; Keyword/named arguments with defaults (options pattern)
(defn game [planet & {:keys [human-players computer-playsers]}]
  (println "Total players:" (+ human-players computer-playsers)))
(game "Mars" :human-players 1 :computer-players 2)

(def point {:x 1 :y 2 :z 3})
(defn draw-point [& {:keys [x y z] :or {x 0 y 0 z 0}}] [x y z])
