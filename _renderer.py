"""Custom quartodoc renderer that fixes the output of returns and raises sections."""

from __future__ import annotations

from typing import Literal, Union

from plum import dispatch
from quartodoc import MdRenderer, layout
from quartodoc._griffe_compat import docstrings as ds
from quartodoc.pandoc.blocks import DefinitionList
from tabulate import tabulate


class Renderer(MdRenderer):
    style = "fix-output-of-returns-and-raises-without-names"

    # returns ----

    @dispatch
    def render(self, el: Union[ds.DocstringSectionReturns, ds.DocstringSectionRaises]):
        rows = list(map(self.render, el.value))
        header = [
            "Type",
            "Description",
        ]  # removed "Name" from header (only relevant when table-style is 'table')
        return self._render_table(rows, header, "returns")

    def _render_table(
        self,
        rows,
        headers,
        style: Literal["parameters", "attributes", "returns"],
    ):
        if self.table_style == "description-list":
            str_rows = str(DefinitionList([row.to_definition_list() for row in rows]))
            # remove empty fields and their separators
            return str_rows.replace(
                "<code>[:]{.parameter-annotation-sep} ", "<code>"
            ).replace("[]{.parameter-name} [:]{.parameter-annotation-sep} ", "")

        row_tuples = [row.to_tuple(style) for row in rows]
        # remove empty fields
        row_tuples_compact = [
            tuple(field for field in tup if field not in (None, ""))
            for tup in row_tuples
        ]
        return tabulate(row_tuples_compact, headers=headers, tablefmt="github")

    # Summarize ===============================================================

    @dispatch
    def summarize(self, el: layout.Section):
        desc = f"\n\n{el.desc}" if el.desc is not None else ""
        if el.title is not None:
            header = f"## {el.title}{desc}"
        elif el.subtitle is not None:
            header = f"### {el.subtitle}{desc}"
        else:
            header = ""

        if el.contents:
            thead = "| | |\n| --- | --- |"

            rendered = []
            for child in el.contents:
                rendered.append(self.summarize(child))

            str_func_table = "\n".join([thead, *rendered])
            # add colwidths
            return f"{header}\n\n{str_func_table}\n\n" + ': {tbl-colwidths="[40,60]"}'

        return header