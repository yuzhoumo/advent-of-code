package utils

import (
    "fmt"
    "strings"
)

type Solution interface {
    Init(input string)
    Title() string
    PartOne() string
    PartTwo() string
}

func Print(s Solution) {
    var sb strings.Builder

    sb.WriteString(s.Title())
    sb.WriteString("\n")

    AppendPart(&sb, "Part One: ", s.PartOne())
    AppendPart(&sb, "Part Two: ", s.PartTwo())

    sb.WriteString("--------------------\n\n")

    fmt.Print(sb.String())
}

func AppendPart(sb *strings.Builder, part string, solution string) {
    if strings.Count(solution, "\n") <= 1 {
        sb.WriteString(part)
        sb.WriteString(solution)
        sb.WriteString("\n")
        return
    }

    sb.WriteString(part)
    sb.WriteString("\n")
    sb.WriteString(solution)
}
