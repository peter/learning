module Login exposing (..)

import Html exposing (..)
import Html.Events exposing (..)
import Html.Attributes exposing (..)
import Html.App as App


-- MODEL SECTION


type alias Model =
    { username : String
    , password : String
    }


initModel : Model
initModel =
    { username = ""
    , password = ""
    }



-- UPDATE SECTION


type Msg
    = UsernameInput String
    | PasswordInput String


update : Msg -> Model -> Model
update msg model =
    case msg of
        UsernameInput username ->
            { model | username = username }

        PasswordInput password ->
            { model | password = password }



-- VIEW SECTION


view : Model -> Html Msg
view model =
    div []
        [ h1 [] [ text "Login Page" ]
        , Html.form []
            [ input
                [ type' "text"
                , onInput UsernameInput
                , placeholder "username"
                ]
                []
            , input
                [ type' "password"
                , onInput PasswordInput
                ]
                []
            , input [ type' "submit" ]
                [ text "Login" ]
            ]
        , hr [] []
        , h4 [] [ text "Login model: " ]
        , p [] [ text <| toString model ]
        ]


main : Program Never
main =
    App.beginnerProgram
        ({ model = initModel
         , view = view
         , update = update
         }
        )
