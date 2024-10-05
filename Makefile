
package_dir := tg_gateway
examples_dir := examples
code_dir := $(package_dir) $(examples_dir)

.PHONY: reformat
reformat:
	@black $(code_dir)
	@ruff check $(code_dir) --fix

.PHONY: lint
lint: reformat
	@mypy --strict $(package_dir)
