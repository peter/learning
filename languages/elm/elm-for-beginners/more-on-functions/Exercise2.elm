module Main exposing (..)

import Html
import String


firstChar : String -> String
firstChar s =
    String.slice 0 1 s


(~=) : String -> String -> Bool
(~=) a b =
    firstChar a == firstChar b


main : Html.Html msg
main =
    (~=) "Peter" "Petra"
        |> toString
        |> Html.text
