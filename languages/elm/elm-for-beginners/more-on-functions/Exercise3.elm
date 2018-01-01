module Main exposing (..)

import Html
import Regex exposing (split, regex)


words : String -> List String
words str =
    split Regex.All (regex "\\W") str


wordCount : String -> Int
wordCount =
    words >> List.length


result : String
result =
    let
        str =
            "Here are some words to count"

        count =
            wordCount str
    in
        "Number of words in '"
            ++ str
            ++ "': "
            ++ (toString count)


main : Html.Html msg
main =
    Html.text result
