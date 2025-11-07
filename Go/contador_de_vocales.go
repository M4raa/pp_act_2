package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// Función que cuenta las vocales
func CountVowels(text string) int {
	text = strings.ToLower(text)
	vowels := "aeiou"
	count := 0

	for _, char := range text {
		if strings.ContainsRune(vowels, char) {
			count++
		}
	}
	return count
}

// Función principal
func main() {
	fmt.Println("Contador de Vocales en Go")
	fmt.Print("Introduce una frase: ")

	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')

	numVowels := CountVowels(text)
	fmt.Printf("La frase contiene %d vocal(es).\n", numVowels)
}
