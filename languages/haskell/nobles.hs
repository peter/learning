-- make people noble

mknoble :: String -> String
mknoble name = "Sir " ++ name

mknoble2 :: Bool -> String -> String
mknoble2 female name = (if female then "Dame " else "Sir ")
                         ++ name
