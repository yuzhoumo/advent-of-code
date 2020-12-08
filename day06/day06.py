import sys
import re

# Part 1
def count_yes(answers):
    answer_set = set()
    for c in answers.replace('\n', ''):
        answer_set.add(c)

    return len(answer_set)


# Part 2
def count_all_yes(answers):
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

    print('\nInput:\n{0}'.format(text))
    print('\nPart 1:', sum(count_yes(a) for a in answers))
    print('\nPart 2:', sum(count_all_yes(a) for a in answers))


if __name__ == '__main__':
    main()
