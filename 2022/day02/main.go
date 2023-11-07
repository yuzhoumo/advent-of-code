package day02

import (
	"strconv"
	"strings"
)

type Day02 struct {
	rounds [][]int
}

func (d *Day02) Init(input string) {
	for _, row := range strings.Split(input, "\n") {
		rr := []rune(row)
		d.rounds = append(d.rounds, []int{int(rr[0] - 'A'), int(rr[2] - 'X')})
	}
}

func (d *Day02) Title() string {
	return "--- Day 2: Rock Paper Scissors ---"
}

func (d *Day02) PartOne() string {
	score := 0
	for _, round := range d.rounds {

		opp, you := round[0], round[1]

		won := ((opp + 1) % 3) == you
		if won {
			score += 6
		} else if opp == you {
			score += 3
		}

		score += you + 1
	}

	return strconv.Itoa(score)
}

func (d *Day02) PartTwo() string {
	score := 0
	for _, round := range d.rounds {

		opp, result := round[0], round[1]
		if result == 0 {
			you := (opp + 2) % 3
			score += you + 1
		} else if result == 1 {
			you := opp
			score += 3 + (you + 1)
		} else {
			you := (opp + 1) % 3
			score += 6 + (you + 1)
		}
	}

	return strconv.Itoa(score)
}
