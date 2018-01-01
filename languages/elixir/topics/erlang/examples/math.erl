-module(math).
-export([areas/1]).
-import(lists, [map/2]).

areas(L) ->
  lists:sum(
             map(
                  fun(I) -> area(I) end,
                  L)).

area({square, X}) ->
  X*X;
area({rectangle, X, Y}) ->
  X*Y.
