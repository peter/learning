module Main exposing (..)

import Html exposing (..)
import Html.Events exposing (..)
import Html.App as App
import Http
import Task


randomJoke : Cmd Msg
randomJoke =
    let
        url =
            "http://api.icndb.com/jokes/random"

        task =
            Http.getString url

        cmd =
            Task.perform Fail Joke task
    in
        cmd



-- MODEL SECTION


type alias Model =
    String


initModel : Model
initModel =
    "Finding a joke..."


init : ( Model, Cmd Msg )
init =
    ( initModel, randomJoke )



-- UPDATE SECTION


type Msg
    = Joke String
    | Fail Http.Error
    | NewJoke


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        Joke joke ->
            ( joke, Cmd.none )

        Fail error ->
            ( (toString error), Cmd.none )

        NewJoke ->
            ( "fetching joke ...", randomJoke )



-- VIEW SECTION


view : Model -> Html Msg
view model =
    div []
        [ button [ onClick NewJoke ] [ text "Fetch a joke" ]
        , br [] []
        , text model
        ]



-- SUBSCRIPTIONS SECTION


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none


main : Program Never
main =
    App.program
        { init = init
        , update = update
        , view = view
        , subscriptions = subscriptions
        }
