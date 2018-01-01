-- Simple factorial definition

fact2 :: Int -> Int
-- fact2 n = if n == 0 then 1 else n * fact2 (n - 1)
fact2 0 = 1
fact2 n = n * fact2 (n - 1)
