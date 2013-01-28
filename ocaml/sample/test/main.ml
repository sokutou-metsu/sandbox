(* -*- coding: utf-8-unix -*- *)

open TestFactorial
open TestFold
open OUnit

let suite =
  "Sample" >::: [
    TestFactorial.suite;
    TestFold.suite
  ]

let _ =
  run_test_tt_main suite
