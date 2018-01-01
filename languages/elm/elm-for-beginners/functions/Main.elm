module Main exposing (..)

import Html exposing (div)
import String


add : Int -> Int -> Int
add a b =
    a + b


result : Bool
result =
    add 1 2 |> add 5 |> \x -> x % 2 == 0


counter : Int
counter =
    0


increment : Int -> Int -> Int
increment cnt amt =
    let
        localCount =
            cnt + 1
    in
        localCount


uppercaseLongName : String -> String
uppercaseLongName name =
    let
        resultName =
            if (String.length name) > 10 then
                String.toUpper name
            else
                name
    in
        resultName ++ " - name length: " ++ (String.length resultName |> toString)


main : Html.Html msg
main =
    div []
        [ Html.text (toString result)
        , Html.text
            (uppercaseLongName "Peter Marklund")
        ]
