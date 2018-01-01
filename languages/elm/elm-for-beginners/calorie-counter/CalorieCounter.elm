module Main exposing (..)

import String
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Html.App exposing (beginnerProgram)


type alias Model =
    { calories : Int
    , increment : Int
    , error : Maybe String
    }


initModel : Model
initModel =
    { calories = 0, increment = 1, error = Nothing }


type Msg
    = AddCalorie
    | ChangeIncrement String
    | Clear


update : Msg -> Model -> Model
update msg model =
    case msg of
        AddCalorie ->
            { model
                | calories = model.calories + model.increment
            }

        ChangeIncrement increment ->
            let
                incrementInt =
                    String.toInt increment
            in
                case incrementInt of
                    Ok incrementValue ->
                        { model | increment = incrementValue, error = Nothing }

                    Err err ->
                        { model | increment = 0, error = Just err }

        Clear ->
            initModel


view : Model -> Html Msg
view model =
    div []
        [ h3 []
            [ text ("Total calories: " ++ (toString model.calories)) ]
        , input
            [ onInput ChangeIncrement
            , value
                (if model.increment == 0 then
                    ""
                 else
                    toString model.increment
                )
            ]
            []
        , div [] [ text (Maybe.withDefault "" model.error) ]
        , button
            [ type' "button"
            , onClick AddCalorie
            ]
            [ text "Add" ]
        , button
            [ type' "button"
            , onClick Clear
            ]
            [ text "Clear" ]
        ]


main : Program Never
main =
    beginnerProgram
        ({ model = initModel
         , update = update
         , view = view
         }
        )
