import sys
import re

# Part 1
def count_yes(answers):
    """
    Return the total number of questions that had a 'yes' answer, i.e. return
    the number of unique characters in `answers` excluding newlines.
    """

    answer_set = set()

    for c in answers.replace('\n', ''):
        answer_set.add(c)

    return len(answer_set)


# Part 2
def count_all_yes(answers):
    """
    Return the total number of questions in which all members of the group
    answered 'yes' to. i.e. return the number of chars that are common across
    all of the line-separated segments of `answers`.
    """

    cnt, answer_dict, group = 0, {}, answers.splitlines()

    for answer_set in group:
        for a in answer_set:
            if a in answer_dict:
                answer_dict[a] += 1
            else:
                answer_dict[a] = 1

            if answer_dict[a] == len(group):
                cnt += 1

    return cnt


def main():
    assert len(sys.argv) > 1, 'Missing argument: path to input file'
    assert len(sys.argv) < 3, 'Too many arguments'
    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        text = f.read().strip()
        answers = text.split('\n\n')

    # Solve part 1
    part1 = sum(count_yes(a) for a in answers)
    print('\nPart 1:', part1)

    # Solve part 2
    part2 = sum(count_all_yes(a) for a in answers)
    print('Part 2:', part2)


if __name__ == '__main__':
    main()
