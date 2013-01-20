(* -*- coding: utf-8-unix -*- *)

let rec factorial n =
  if n < 0 then
    raise (Invalid_argument "negative number")
  else
    match n with
      0 -> 1
    | _ -> n * (factorial (n - 1))
