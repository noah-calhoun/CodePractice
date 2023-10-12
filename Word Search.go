/*
A program by Noah Calhoun to learn GO.

This word search follows the following rules:
	Words can be up, down, diagonal, but not backwards
	Letters from one word can be used in another word
*/

package main

import "fmt"

var matrix = [][]rune{
	{'B', 'A', 'T', 'M', 'A'},
	{'O', 'P', 'O', 'L', 'E'},
	{'A', 'T', 'X', 'A', 'R'},
	{'T', 'S', 'A', 'P', 'R'},
	{'Y', 'P', 'O', 'T', 'S'},
}

var words = []string{"BAT", "APPLE", "SOAP"}

func wordSearch(matrix [][]rune, words []string) {
	// Create black output matrix
	var res [][]rune
	res = make([][]rune, len(matrix))
	for i := range res {
		res[i] = make([]rune, len(matrix[i]))
		for j := range res[i] {
			res[i][j] = 0
		}
	}

	// Begin searching by row
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			// Implement the logic to check for words horizontally here using matrix[i][j]
		}
	}

	// Begin searching by column
	for j := 0; j < len(matrix[0]); j++ {
		for i := 0; i < len(matrix); i++ {
			// Implement the logic to check for words vertically here using matrix[i][j]
		}
	}

	fmt.Println(matrix)

}

func main() {

	// Call the word search function here
	fmt.Println(matrix)
	wordSearch(matrix, words)

}
