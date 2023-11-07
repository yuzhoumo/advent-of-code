package main

import (
	"fmt"
	"os"

	"github.com/yuzhoumo/advent-of-code/aoc22/day01"
	"github.com/yuzhoumo/advent-of-code/aoc22/day02"
	"github.com/yuzhoumo/advent-of-code/aoc22/day03"
	"github.com/yuzhoumo/advent-of-code/aoc22/day04"
	"github.com/yuzhoumo/advent-of-code/aoc22/utils"
)

var sols = []utils.Solution{
	&day01.Day01{},
	&day02.Day02{},
	&day03.Day03{},
	&day04.Day04{},
}

func main() {
	fmt.Println("Solutions for AOC 2022")

	var path, input string
	for i, s := range sols {
		if i < 9 {
			path = fmt.Sprintf("day0%d/input.txt", i+1)
		} else {
			path = fmt.Sprintf("day%d/input.txt", i+1)
		}

		if buf, err := os.ReadFile(path); err != nil {
			panic(err)
		} else {
			input = string(buf)
		}

		s.Init(input)
		utils.Print(s)
	}
}
