module Basics where

doubleMe x = x + x

doubleSmallNumber x = if x > 100
                        then x
                        else x*2

removeNonUppercase :: [Char] -> [Char]
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]

addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z

factorial :: Integer -> Integer
factorial n = product [1..n]

circumference :: Float -> Float
circumference r = 2 * pi * r

sayHello :: String -> IO ()
sayHello x = putStrLn ("Hello, " ++ x ++ "!")

area :: Fractional a => a -> a
area n = 3.14 * (n * n)

myValue = 10

fnWithLet :: Num a => a -> a
fnWithLet x =
  let y = x * 2
      z = x^2
  in 2 * y * z

mult1 = x * y
  where x = 5
        y = 6

printInc n = print plusTwo
  where plusTwo = n + 2

maxhelper :: Int -> [Int] -> Int
maxhelper x [] = x
maxhelper x (y:ys) = maxhelper (if x>y then x else y) ys

maxfromlist :: [Int] -> Maybe Int
maxfromlist [] = Nothing
maxfromlist (x:xs) = Just (maxhelper x xs)
