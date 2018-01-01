lst = [1..10]

f x = x*(x+1)
lst_ = map f lst

-- g =
-- g' = (/)
accl = foldl (/) 1 lst
accr = foldr (/) 1 lst

main = do
  putStrLn ("map result: " ++ show lst_)
  putStrLn ("foldl result: " ++ show accl)
  putStrLn ("foldr result: " ++ show accr)
