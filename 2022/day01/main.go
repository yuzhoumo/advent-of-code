package day01

import (
    "strconv"
    "strings"
    "sort"
)

type Day01 struct {
    calories []int
}

func (d *Day01) Init(input string) {
    for _, group := range strings.Split(input, "\n\n") {

        calories := 0
        for _, v := range strings.Split(group, "\n") {
            res, _ := strconv.Atoi(v)
            calories += res
        }

        d.calories = append(d.calories, calories)
    }

    sort.Ints(d.calories)
}

func (d *Day01) Title() string {
    return "--- Day 1: Calorie Counting ---"
}

func (d *Day01) PartOne() string {
    return strconv.Itoa(d.calories[len(d.calories) - 1])
}

func (d *Day01) PartTwo() string {
    tot := 0
    for _, c := range d.calories[len(d.calories) - 3:] {
        tot += c
    }

    return strconv.Itoa(tot)
}
