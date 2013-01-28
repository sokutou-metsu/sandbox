(* -*- coding: utf-8-unix -*- *)

open Utility.List
open OUnit

let test_fold () =
  assert_equal [3; 2; 1] (fold (fun x y -> x :: y) [] [1; 2; 3]);
  assert_equal 6 (fold (fun x y -> x * y) 1 [1; 2; 3])

let test_fold_left () =
  assert_equal [3; 2; 1] (fold_left (fun x y -> y :: x) [] [1; 2; 3]);
  assert_equal 6 (fold_left (fun x y -> x * y) 1 [1; 2; 3])

let test_fold_right () =
  assert_equal [1; 2; 3] (fold_right (fun x y -> x :: y) [] [1; 2; 3]);
  assert_equal 6 (fold_right (fun x y -> x * y) 1 [1; 2; 3])

let suite =
  "Test Fold" >::: [
    "test_fold" >:: test_fold;
    "test_fold_left" >:: test_fold_left;
    "test_fold_right" >:: test_fold_right
  ]
