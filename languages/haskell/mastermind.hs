-- From: https://gist.github.com/BillyBadBoy/6109d4042064b2380c198c0361c48e5e

import System.Random
import Data.List
---------------------------------------------------------------------
mastermind :: IO ()
mastermind = do
  putStrLn "Think of a 4 digit code using 1,2,3,4,5,6"
  turn [0..6^4 - 1] 6
---------------------------------------------------------------------
type Code  = Int
type Score = Int
---------------------------------------------------------------------
code2Ints :: Code -> [Int]
code2Ints c = map ((`mod` 6) . (c `div`)) [ 1, 6, 36, 216 ]
---------------------------------------------------------------------
-- score guess with code: 5 = black, 1 = white
score :: Code -> Code -> Score
score guess code = maximum $ map scoreWithCode guessPermutations
  where
    guessPermutations = permutations       (zip (code2Ints guess) [0..])
    scoreWithCode = sum . zipWith scorePeg (zip (code2Ints code)  [0..])
    scorePeg (x,i)(y,j) = if x == y then if i == j then 5 else 1 else 0
----------------------------------------------------------------------
isConsistentWith :: Code -> (Code, Score) -> Bool
isConsistentWith c (c', s) = score c c' == s
----------------------------------------------------------------------
updateViable :: [Code] -> (Code, Score) -> [Code]
updateViable cs (c',s) = filter (`isConsistentWith` (c',s)) cs
----------------------------------------------------------------------
randViable :: [Code] -> IO Code
randViable cs = do
  i <- randomRIO (0, length cs - 1)
  return $ cs !! i
----------------------------------------------------------------------
code2Str :: Code -> String
code2Str c = map ("123456" !!) $ code2Ints c
----------------------------------------------------------------------
getScore :: Code -> IO Score
getScore c = do
  putStrLn $ "\nI guess: " ++ code2Str c
  putStrLn "enter number of blacks:"
  b <- getLine
  putStrLn "enter number of whites:"
  w <- getLine
  return $ (5 * read b) + read w
----------------------------------------------------------------------
turn :: [Code] -> Int -> IO ()
turn viable n =
  if n == 0
    then putStrLn "Oh no! I've lost!"
    else do
      putStrLn $ "I have " ++ show n ++ " guesses remaining."
      guess <- randViable viable
      score <- getScore guess
      handleScore viable n guess score
----------------------------------------------------------------------
handleScore :: [Code] -> Int -> Code -> Score -> IO ()
handleScore viable n guess score =
  if score == 20
    then putStrLn "Yes, I win again !!!\n"
    else do
      let viable' = updateViable viable (guess, score)
      if null viable'
        then putStrLn "Error - you have scored incorrectly!"
        else turn viable' (n - 1)
----------------------------------------------------------------------
