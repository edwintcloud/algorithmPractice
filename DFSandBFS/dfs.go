package main

import "fmt"

func isSafe(m *[][]int, row int, col int) bool {
	if row < 0 || row >= len(*m) {
		return false
	}
	if col < 0 || col >= len((*m)[row]) {
		return false
	}
	if (*m)[row][col] == 0 {
		return false
	}
	return true
}

func dfs(m *[][]int, row int, col int, count *int) {
	rowNbr := [8]int{-1, -1, -1, 0, 0, 1, 1, 1}
	colNbr := [8]int{-1, 0, 1, -1, 1, -1, 0, 1}

	(*m)[row][col] = 0

	for i := 0; i < 8; i++ {
		if isSafe(m, row+rowNbr[i], col+colNbr[i]) {
			(*count)++
			dfs(m, row+rowNbr[i], col+colNbr[i], count)
		}
	}
}

func largestRegion(m *[][]int) int {
	result := 0
	for i := 0; i < len(*m); i++ {
		for j := 0; j < len((*m)[i]); j++ {
			if (*m)[i][j] == 1 {
				count := 1
				dfs(m, i, j, &count)
				if count > result {
					result = count
				}
			}
		}
	}
	return result
}

func main() {

	// create test array
	m := [][]int{
		{0, 0, 0, 0, 0, 1},
		{0, 1, 1, 0, 1, 1},
		{0, 0, 1, 0, 0, 1},
		{0, 0, 0, 0, 1, 0},
	}

	fmt.Println(largestRegion(&m))
}
