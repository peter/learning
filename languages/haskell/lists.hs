
-- my_filter (>4) [1,2,3,4,5] => [5]
my_filter :: (b -> Bool) -> [b] -> [b]
my_filter pred [] = []
my_filter pred (x:xs)
  | pred x = x : my_filter pred xs
  | otherwise = my_filter pred xs
