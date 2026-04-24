package com.example.calculator;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api")
public class CalculatorController {

    @GetMapping("/add")
    public ResponseEntity<Map<String, Integer>> add(@RequestParam int a, @RequestParam int b) {
        return ResponseEntity.ok(Map.of("result", a + b));
    }

    @GetMapping("/sub")
    public ResponseEntity<Map<String, Integer>> sub(@RequestParam int a, @RequestParam int b) {
        return ResponseEntity.ok(Map.of("result", a - b));
    }

    @GetMapping("/mul")
    public ResponseEntity<Map<String, Integer>> mul(@RequestParam int a, @RequestParam int b) {
        return ResponseEntity.ok(Map.of("result", a * b));
    }

    @GetMapping("/div")
    public ResponseEntity<?> div(@RequestParam int a, @RequestParam int b) {
        if (b == 0) {
            return ResponseEntity.badRequest().body(Map.of("error", "Cannot divide by zero"));
        }
        return ResponseEntity.ok(Map.of("result", a / b));
    }

    @GetMapping("/mod")
    public ResponseEntity<?> mod(@RequestParam int a, @RequestParam int b) {
        if (b == 0) {
            return ResponseEntity.badRequest().body(Map.of("error", "Cannot mod by zero"));
        }
        return ResponseEntity.ok(Map.of("result", a % b));
    }
}
