(* -*- coding: utf-8-unix -*- *)

module BuildInList = List

module List : sig

  val fold : ('l -> 'b -> 'b) -> 'b -> 'l list -> 'b
  val fold_left : ('a -> 'l -> 'a) -> 'a -> 'l list -> 'a
  val fold_right : ('l -> 'b -> 'b) -> 'b -> 'l list -> 'b

end = struct

  let fold f e lis =
    let rec iter rest result =
      match rest with
        [] -> result
      | x :: xs -> iter xs (f x result) in
    iter lis e

  let fold_left f e l =
    BuildInList.fold_left f e l

  let rec fold_right f e l =
    BuildInList.fold_right f l e

end
