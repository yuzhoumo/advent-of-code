package day04

import (
	"fmt"
	"io"
	"strconv"
	"strings"
)

type Day04 struct {
	contains int
	overlaps int
}

func (d *Day04) Init(input string) {

	const pat = "%d-%d,%d-%d\n"
	r := strings.NewReader(input)

	for {
		var i, j, k, l int
		if _, err := fmt.Fscanf(r, pat, &i, &j, &k, &l); err == io.EOF {
			break
		}

		kil := k <= i && i <= l
		kjl := k <= j && j <= l

		ikj := i <= k && k <= j
		ilj := i <= l && l <= j

		if (kil && kjl) || (ikj && ilj) {
			d.contains += 1
		}

		if kil || ikj {
			d.overlaps += 1
		}
	}
}

func (d *Day04) Title() string {
	return "--- Day 4: Camp Cleanup ---"
}

func (d *Day04) PartOne() string {
	return strconv.Itoa(d.contains)
}

func (d *Day04) PartTwo() string {
	return strconv.Itoa(d.overlaps)
}
