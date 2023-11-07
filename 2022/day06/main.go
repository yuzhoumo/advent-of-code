package day06

import (
	"errors"
	"math/bits"
	"strconv"
	"strings"
)

func findUnique(data []rune, size int) (int, error) {
	var accum uint = 0
	masks := make([]uint, len(data))

	for i, c := range data {
		masks[i] = uint(1 << (c - 'a'))
		accum ^= masks[i]
		if i >= size {
			accum ^= uint(masks[i - size])
			if bits.OnesCount(accum) == size {
				return i + 1, nil
			}
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
