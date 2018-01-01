; MAPS

(def users {"kyle" {:password "secretk" :number-pets 2}
            "siva" {:password "secrets" :number-pets 4}
            "rob" {:password "secretr" :number-pets 6}
            "george" {:password "secretg" :number-pets 8}})

(let [user-data (vals users)
        number-pets (map :number-pets user-data)
        total (apply + number-pets)]
  (println total)) ; => 20
