package day03

import (
	"strconv"
	"strings"
	"unicode"
)

type Day03 struct {
	bags []string
}

func (d *Day03) Init(input string) {
	d.bags = strings.Split(input, "\n")
}

func (d *Day03) Title() string {
	return "--- Day 3: Rucksack Reorganization ---"
}

func (d *Day03) PartOne() string {
	priorities := 0
	for _, bag := range d.bags {

		compartment, half := map[rune]bool{}, len(bag)/2
		for _, item := range bag[:half] {
			compartment[item] = true
		}

		for _, item := range bag[half:] {
			if compartment[item] {
				priorities += priority(item)
				break
			}
		}
	}

	return strconv.Itoa(priorities)
}

func (d *Day03) PartTwo() string {
	priorities := 0
	for i := 0; i < len(d.bags); i += 3 {

		g1 := map[rune]bool{}
		for _, item := range d.bags[i] {
			g1[item] = true
		}

		g2 := map[rune]bool{}
		for _, item := range d.bags[i+1] {
			g2[item] = true
		}

		for _, item := range d.bags[i+2] {
			if g1[item] && g2[item] {
				priorities += priority(item)
				break
			}
		}
	}

	return strconv.Itoa(priorities)
}

func priority(item rune) int {
	if unicode.IsLower(item) {
		return 1 + int(item-'a')
	} else if unicode.IsUpper(item) {
		return 27 + int(item-'A')
	}
	return 0
}
