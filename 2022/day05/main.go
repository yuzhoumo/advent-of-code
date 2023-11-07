package day05

import (
	"bufio"
	"fmt"
	"strings"
	"slices"
)

type stack []rune

func (s stack) PushN(runes []rune) stack {
	return append(s, runes...)
}

func (s stack) PopN(n int) (stack, []rune) {
	end := len(s) - n
	return s[:end], s[end:]
}

func (s stack) Peek() rune {
	return s[len(s) - 1]
}

func getTop(crates []stack) string {
	res := []rune{}
	for _, s := range crates {
		res = append(res, s.Peek())
	}
	return string(res)
}

func copyStacks(stacks []stack) []stack {
	stacksCopy := make([]stack, len(stacks))
	for i := 0; i < len(stacks); i += 1 {
		stacksCopy[i] = make(stack, len(stacks[i]))
		copy(stacksCopy[i], stacks[i])
	}
	return stacksCopy
}

func parseRows(diagram string) [][]rune {
	scanner := bufio.NewScanner(strings.NewReader(diagram))
	rows := [][]rune{}
	for scanner.Scan() {
		row, line := []rune{}, scanner.Text()
		for i := 1; i < len(line); i += 4 {
			row = append(row, rune(line[i]))
		}
		if len(row) != 0 {
			rows = append(rows, row)
		}
	}
	return rows
}

func parseStacks(diagram string) []stack {
	rows := parseRows(diagram)
	numCols := len(rows[0])
	crates := make([]stack, numCols)
	for i := len(rows) - 1; i > -1; i -= 1 {
		for j, v := range rows[i] {
			if v != ' ' {
				crates[j] = append(crates[j], v)
			}
		}
	}
	return crates
}

type move struct {
	cnt, src, dst int
}

func parseMoves(procedure string) []move {
	r := strings.NewReader(procedure)
	moves := []move{}
	for {
		var cnt, src, dst int
		n, err := fmt.Fscanf(r, "move %d from %d to %d\n", &cnt, &src, &dst)
		if n == 0 || err != nil {
			break
		}
		moves = append(moves, move{cnt, src - 1, dst - 1})
	}
	return moves
}

type Day05 struct {
	stacks []stack
	moves []move
}

func (d *Day05) Init(input string) {
	d.stacks = parseStacks(input[:strings.Index(input, "1")])
	d.moves = parseMoves(input[strings.Index(input, "move"):])
}

func (d *Day05) Title() string {
	return "--- Day 5: Supply Stacks ---"
}

func (d *Day05) PartOne() string {
	crates := copyStacks(d.stacks)
	for _, m := range d.moves {
		var vals []rune
		crates[m.src], vals = crates[m.src].PopN(m.cnt)
		slices.Reverse(vals)
		crates[m.dst] = crates[m.dst].PushN(vals)
	}
	return getTop(crates)
}

func (d *Day05) PartTwo() string {
	crates := copyStacks(d.stacks)
	for _, m := range d.moves {
		var vals []rune
		crates[m.src], vals = crates[m.src].PopN(m.cnt)
		crates[m.dst] = crates[m.dst].PushN(vals)
	}
	return getTop(crates)
}
