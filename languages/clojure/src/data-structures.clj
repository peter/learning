; DATA STRUCTURES

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; ATOMIC DATA TYPES
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; Arbitrary precision integers
123456786
; Doubles
1.23
; BigDecimals
1.234M
; Ratios
22/7

; Strings
"foobar"
; Characters
\a

; Symbols
foo
bar

; Keywords
:foo
:bar

; Booleans
true
false

; Null
nil

; Regular expressions
#"foo*bar"

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; FOUR BASIC COMPOSITE DATA STRUCTURE LITERALS
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; NOTE: all data structures can contain any number of objects of any type and can be nested:

; List (linked list)
(4 :alpha 3.0)

; Vector (random access)
[2 "hello" 99]

; Set (unique items)
#{alice jim bob}

; Map (key-value dictionary)
{:a 1 :b 2}

; NOTE: keys are typically keywords (with colon prefix) but can be any object
