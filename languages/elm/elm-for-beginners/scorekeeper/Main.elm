module Main exposing (..)

import String
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Html.App as App


type alias Model =
    { players : List Player
    , name : String
    , playerId : Maybe Int
    , plays : List Play
    }


type alias Player =
    { id : Int
    , name : String
    , points : Int
    }


type alias Play =
    { id : Int
    , playerId : Int
    , name : String
    , points : Int
    }


initModel : Model
initModel =
    { players = []
    , name = ""
    , playerId = Nothing
    , plays = []
    }


type Msg
    = Edit Player
    | Score Player Int
    | Input String
    | Save
    | Cancel
    | DeletePlay Play


updatePlayer : Int -> Model -> Model
updatePlayer playerId model =
    let
        newPlayers =
            List.map
                (\player ->
                    if player.id == playerId then
                        { player
                            | name = model.name
                        }
                    else
                        player
                )
                model.players

        newPlays =
            List.map
                (\play ->
                    if play.playerId == playerId then
                        { play
                            | name = model.name
                        }
                    else
                        play
                )
                model.plays
    in
        { model
            | players = newPlayers
            , plays = newPlays
            , playerId = Nothing
        }


createPlayer : Model -> Model
createPlayer model =
    let
        newId =
            (List.length model.players) + 1

        newPlayer =
            Player newId model.name 0

        newPlayers =
            newPlayer :: model.players
    in
        { model
            | players = newPlayers
        }


savePlayer : Model -> Model
savePlayer model =
    case model.playerId of
        Just playerId ->
            updatePlayer playerId model

        Nothing ->
            createPlayer model


score : Player -> Int -> Model -> Model
score player points model =
    let
        newPoints =
            player.points + points

        newPlayers =
            List.map
                (\player' ->
                    if player'.id == player.id then
                        { player'
                            | points = newPoints
                        }
                    else
                        player'
                )
                model.players

        newPlayId =
            (List.length model.plays) + 1

        newPlays =
            Play newPlayId player.id player.name points
                :: model.plays
    in
        { model
            | players = newPlayers
            , plays = newPlays
        }


deletePlay : Play -> Model -> Model
deletePlay play model =
    let
        newPlays =
            List.filter
                (\p -> p.id /= play.id)
                model.plays

        newPlayers =
            List.map
                (\player ->
                    if player.id == play.playerId then
                        { player
                            | points = (player.points - play.points)
                        }
                    else
                        player
                )
                model.players
    in
        { model
            | plays = newPlays
            , players = newPlayers
        }


edit : Player -> Model -> Model
edit player model =
    { model
        | name = player.name
        , playerId = Just player.id
    }


update : Msg -> Model -> Model
update msg model =
    case msg of
        Input name ->
            Debug.log "Input updated model"
                { model | name = name }

        Save ->
            if (String.isEmpty model.name) then
                model
            else
                savePlayer model

        Cancel ->
            { model
                | name = ""
                , playerId = Nothing
            }

        Edit player ->
            edit player model

        Score player points ->
            score player points model

        DeletePlay play ->
            deletePlay play model


view : Model -> Html Msg
view model =
    div [ class "scoreboard" ]
        [ h1 []
            [ text "Score Keeper" ]
        , playerSection model
        , playerForm model
        , playSection model
        , p [] [ text (toString model) ]
        ]


playerSection : Model -> Html Msg
playerSection model =
    div []
        [ playerListHeader
        , playerList model
        , pointTotal model
        ]


playerListHeader : Html Msg
playerListHeader =
    header []
        [ div [] [ text "Name" ]
        , div [] [ text "Points" ]
        ]


editStyle : List ( String, String )
editStyle =
    [ ( "backgroundColor", "cyan" ) ]


playerStyle : Model -> Player -> List ( String, String )
playerStyle model player =
    case model.playerId of
        Just playerId ->
            if playerId == player.id then
                editStyle
            else
                []

        Nothing ->
            []


inputStyle : Model -> List ( String, String )
inputStyle model =
    case model.playerId of
        Just playerId ->
            editStyle

        Nothing ->
            []


player : Model -> Player -> Html Msg
player model player =
    li []
        [ i
            [ class "edit"
            , onClick (Edit player)
            ]
            []
        , div
            [ style (playerStyle model player) ]
            [ text player.name ]
        , button
            [ type' "button"
            , onClick (Score player 2)
            ]
            [ text "2pt" ]
        , button
            [ type' "button"
            , onClick (Score player 3)
            ]
            [ text "3pt" ]
        , div []
            [ text (toString player.points) ]
        ]


playerList : Model -> Html Msg
playerList model =
    -- ul []
    --     (List.map player model.players)
    model.players
        |> List.sortBy .name
        |> List.map (player model)
        |> ul []


pointTotal : Model -> Html Msg
pointTotal model =
    let
        total =
            List.map .points model.plays
                |> List.sum
    in
        footer []
            [ div [] [ text "Total:" ]
            , div [] [ text (toString total) ]
            ]


playerForm : Model -> Html Msg
playerForm model =
    Html.form [ onSubmit Save ]
        [ input
            [ type' "text"
            , placeholder "Add/Edit player"
            , onInput Input
            , value model.name
            , style (inputStyle model)
            ]
            []
        , button [ type' "submit" ] [ text "Save" ]
        , button [ type' "button", onClick Cancel ] [ text "Cancel" ]
        ]


playSection : Model -> Html Msg
playSection model =
    div []
        [ playListHeader
        , playList model
        ]


playListHeader : Html Msg
playListHeader =
    header []
        [ div [] [ text "Plays" ]
        , div [] [ text "Points" ]
        ]


playList : Model -> Html Msg
playList model =
    model.plays
        |> List.map play
        |> ul []


play : Play -> Html Msg
play play =
    li []
        [ i
            [ class "remove"
            , onClick (DeletePlay play)
            ]
            []
        , div [] [ text play.name ]
        , div [] [ text (toString play.points) ]
        ]


main : Program Never
main =
    App.beginnerProgram
        { model = initModel
        , view = view
        , update = update
        }
