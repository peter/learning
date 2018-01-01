-- Programming tip: focus on the type of a function first

-- Improvement: use a random word from a dictionary (import System.Random)

check :: String -> String -> Char -> (Bool,String)
-- word: the secret word
-- display: current display
-- c: character guessed by player
check word display c
  = (c `elem` word, [if x==c
      then c
      else y | (x,y) <- zip word display])

turn :: String -> String -> Int -> IO ()
-- word: the secret word
-- display: current display
-- n: number of guesses left
turn word display n =
  do if n==0
        then putStrLn "You lose"
        else if word==display
                then putStrLn ("You win: " ++ word ++ "!!")
                else mkguess word display n

mkguess :: String -> String -> Int -> IO ()
mkguess word display n =
  do putStrLn (display ++ " " ++ take n (repeat '*'))
     putStr " Enter your guess: "
     q <- getLine
     let (correct, display') = check word display (q!!0)
     let n' = if correct then n else n-1
     turn word display' n'

starman :: String -> Int -> IO ()
starman word n = turn word ['-' | x <- word] n
