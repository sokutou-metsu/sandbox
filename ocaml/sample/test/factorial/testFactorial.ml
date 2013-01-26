(* -*- coding: utf-8-unix -*- *)

open Factorial
open OUnit

let test_positive () =
  begin
    assert_equal 2 (factorial 2);
    assert_equal 6 (factorial 3);
    assert_equal 24 (factorial 4)
  end

let test_first () =
  assert_equal 1 (factorial 1)

let test_zero () =
  assert_equal 1 (factorial 0)

let test_negative () =
  assert_raises
    (Invalid_argument "negative number")
    (fun _ -> (factorial (-1)))


let suite =
  "Test Factorial" >::: [
    "test_positive" >:: test_positive;
    "test_first" >:: test_first;
    "test_zero" >:: test_zero;
    "test_negative" >:: test_negative
  ]
