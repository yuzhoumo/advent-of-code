package day06

import (
	"errors"
	"strconv"
	"strings"
)

func findUnique(data []rune, size int) (int, error) {
	for i := 0; i < len(data); i += 1 {
		found, seen := true, map[rune]bool{}
		for j := i; j < i + size; j += 1 {
			curr := data[j]
			if seen[curr] {
				found = false
				break
			}
			seen[curr] = true
		}

		if found {
			return i + size, nil
		}
	}

	return 0, errors.New("not found")
}

type Day06 struct {
	datastream []rune
}

func (d *Day06) Init(input string) {
	d.datastream = []rune(strings.TrimSpace(input))
}

func (d *Day06) Title() string {
	return "--- Day 6: Tuning Trouble ---"
}

func (d *Day06) PartOne() string {
	idx, _ := findUnique(d.datastream, 4)
	return strconv.Itoa(idx)
}

func (d *Day06) PartTwo() string {
	idx, _ := findUnique(d.datastream, 14)
	return strconv.Itoa(idx)
}
