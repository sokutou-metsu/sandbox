(* -*- coding: utf-8-unix -*- *)

open Utility.List
open OUnit

let string_of_int_list int_list =
  "[" ^ (String.concat "; " (List.map string_of_int int_list)) ^ "]"

let test_fold () =
  assert_equal
    ~printer:string_of_int_list
    [3; 2; 1] (fold (fun x y -> x :: y) [] [1; 2; 3]);
  assert_equal
    ~printer:string_of_int
    6 (fold (fun x y -> x * y) 1 [1; 2; 3]);
  assert_equal
    ~printer:string_of_int
    (-98) (fold (fun x y -> x - y) 100 [1; 2; 3])

let test_fold_left () =
  assert_equal
    ~printer:string_of_int_list
    [3; 2; 1] (fold_left (fun y x -> x :: y) [] [1; 2; 3]);
  assert_equal
    ~printer:string_of_int
    6 (fold_left (fun x y -> x * y) 1 [1; 2; 3]);
  assert_equal
    ~printer:string_of_int
    94 (fold_left (fun x y -> x - y) 100 [1; 2; 3])

let test_fold_right () =
  assert_equal
    ~printer:string_of_int_list
    [1; 2; 3] (fold_right (fun x y -> x :: y) [] [1; 2; 3]);
  assert_equal
    ~printer:string_of_int
    6 (fold_right (fun x y -> x * y) 1 [1; 2; 3]);
  assert_equal
    ~printer:string_of_int
    (-98) (fold_right (fun x y -> x - y) 100 [1; 2; 3])

let suite =
  "Test Fold" >::: [
    "test_fold" >:: test_fold;
    "test_fold_left" >:: test_fold_left;
    "test_fold_right" >:: test_fold_right
  ]
