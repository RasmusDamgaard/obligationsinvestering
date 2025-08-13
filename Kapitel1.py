import marimo

__generated_with = "0.14.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Kapitel 1: Fundamentet for rentedannelsen""")
    return


@app.cell
def _():
    import marimo as mo
    import polars as pl
    return mo, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.1
    Beskriv hvilke faktorer, der har indflydelse på renteniveauet.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""svar""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.2
    Beskriv sammenhængen mellem realrenten og produktivitetstilvæksten i økonomien.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""svar""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.3
    Illustrer grafisk rentestrukturen ud fra følgende nominelle effektive rentesatser på penge- og obligationsmarkedet.
    """
    )
    return


@app.cell
def _(pl):
    data = {"Produkter": ["Anfordringsindskud", "Indskud på 3 måneders opsigelse", "Indskud på 12 måneders opsigelse",
                         "Obligationsrente, 1 år", "Obligationsrente, 3 år", "Obligationsrente, 5 år", "Obligationsrente, 10 år",
                         "Obligationsrente, 30 år"],
           "Rentesats": [0.00, 0.5, 1.5, 3.00, 4.50, 5.50, 6.25, 6.75]}
    df = pl.DataFrame(data)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
