(* -*- coding: utf-8-unix -*- *)

open TestFactorial
open OUnit

let suite =
  "main" >::: [
    TestFactorial.suite
  ]

let _ =
  begin
    ignore (run_test_tt_main suite);
    ()
  end
