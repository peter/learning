-module(functions).
-export([factorial/1, member/2, member_two/2, factorial2/1]).

factorial(0) -> 1;
factorial(N) -> N * factorial(N-1).

member(H, [H|T]) -> true;
member(H, [_|T]) -> member(H, T);
member(H, []) -> false.

member_two(H, [H1|_]) when H == H1 -> true;
member_two(H, [_|T]) -> member_two(H, T);
member_two(H, []) -> false.

factorial2(N) -> factorial2_t(N, 1).
factorial2_t(0, Acc) -> Acc;
factorial2_t(N, Acc) -> factorial2_t(N-1, N*Acc).
