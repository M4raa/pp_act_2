package main

import "testing"

// Test 1
func TestCountVowelsSimple(t *testing.T) {
	result := CountVowels("hola")
	if result != 2 {
		t.Errorf("Esperado 2, obtenido %d", result)
	}
}

// Test 2
func TestCountVowelsWithUppercase(t *testing.T) {
	result := CountVowels("Avion")
	if result != 3 {
		t.Errorf("Esperado 3, obtenido %d", result)
	}
}

// Test que falla
func TestCountVowelsIncorrect(t *testing.T) {
	result := CountVowels("zzz")
	if result != 1 {
		t.Errorf("Esperado 1, obtenido %d", result)
	}
}
