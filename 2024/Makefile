.PHONY: run install submit template

run:
	./scripts/run.sh $(day) $(input)

submit:
	./scripts/run.sh $(day) --submit

install:
	uv sync

template:
	uv run -m aoc $(day)
