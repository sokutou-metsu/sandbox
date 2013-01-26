(* -*- coding: utf-8-unix -*- *)

open TestFactorial
open OUnit

let suite =
  "Sample" >::: [
    TestFactorial.suite
  ]

let _ =
  run_test_tt_main suite
