# Parsing

Parsing is analyzing natural language text (or programming language text) according to a formal grammar. In case of natural languages parsing involves identifying:

* Characters
* Words
* Sentences
* Paragraphs

Text to parse:

```
Bring a large pot of water up to a boil. Unlike Italian pasta, you do not need to salt the water. Once it’s boiling, hold the noodles over the water and sprinkle them in strand by strand. Once all the noodles are in, stir gently so that they are all immersed in the water. Bring the water back up to a gentle boil, then lower the heat so that the water is just simmering. (This differs from the ’rolling boil’ that’s recommended for pasta.) If the water threatens to boil over, add about 1/2 cup of cold water (but if you lower the heat to the gentle simmer, and have a big enough pot, this shouldn’t be necessary). Cook for about 7 to 8 minutes, or following the package directions (for thinner noodles 5 to 6 minutes may be enough. Test by eating a strand - it should be cooked through, not al dente, but not mushy either).
```

Typically a functional program is organized around a tree-like data structure with an algebraic data type that represents the core data. A parser reads text input and generates the tree. Functions peform transformations or traversals on the tree. Pretty-printer functions output the tree (original or transformed).

Approaches to parsing:

* Regular expressions
* Parser combinators
* Parser generators: bison, antlr, happy

Parser combinators are higher order functions that allow you to combine smaller parsers into bigger ones.

`Parsec` is a monadic parsing combinator library for Haskell.

Example of the IO Monad:

```haskell
hello :: String -> IO String
hello x =
  do
    putStrLn ("Hello, " ++ x)
    putStrLn "Whats is your name?"
    return <- getLine
    return name
```

Key features of a monad: the do keyword, the sequence of commands, the left arrow operator and the return keyword, the monadic return value (IO String).

```haskell
data Tag = MkTag String

parseTag :: Parser Tag
parseTag =
  do  char '<'
      x <- identifier
      char '>'
      return (MkTag x)
```

The parseTag function returns a parser.

If the match succeeds, the matching string is removed from the input string; otherwise, the original string is returned

Often we want to try one parser; if that fails, then try another one instead. The choice combinator <|> provides this functionality.
