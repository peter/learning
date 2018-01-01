module Main exposing (..)

import Html exposing (..)
import Html.Events exposing (..)
import Html.App as App
import Http
import Task
import Json.Decode exposing (..)
import Json.Decode.Pipeline exposing (decode, required, optional)


type alias Response =
    { id : Int
    , joke : String
    , categories : List String
    }


responseDecoder : Decoder Response
responseDecoder =
    decode Response
        |> required "id" int
        |> required "joke" string
        |> optional "categories" (list string) []
        |> at [ "value" ]


url : String
url =
    "http://api.icndb.com/jokes/random"


randomJoke : Cmd Msg
randomJoke =
    Task.perform Fail Joke (Http.get responseDecoder url)



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
    = Joke Response
    | Fail Http.Error
    | NewJoke


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        Joke response ->
            ( toString (response.id) ++ " " ++ response.joke, Cmd.none )

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
