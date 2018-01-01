; Namespace declaration
(ns my-app.my-module)

; Moving into a namespace (creates if doesn't exist)
(in-ns 'my-namespace)

; Dir listing in namespace plus documentation of functions
(dir clojure.java.io)
(doc clojure.java.io/delete-file)

; REPL always starts in namespace "user"

; Require - loads namespace if not already loaded
(require 'clojure.set)
(clojure.set/union #{1 2} #{1 3 4})
(require '[clojure.set :as set])
(set/union #{1 2} #{1 3 4})

; Use - loads namespace *and* refers all symbols into current namespace (warns on clashes)
; Only recommended for the REPL
(use 'clojure.string)
(use '[clojure.string :only (join)])
(join ",", [1 2 3])

; Refer: copy symbol bindings from a namespace into current namespace

; Import: make Java class names available in current namespace
