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
    import matplotlib.pyplot as plt
    return mo, pl, plt


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
    mo.md(
        r"""
    * Inflation
    * Forventet fremtidig inflation
    * Vækst økonomien og fremtidig vækst
    * 
    """
    )
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
    mo.md(r"""Høj produtivitetstilvækst $\rightarrow$ høj rente""")
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
    return (df,)


@app.cell
def _(df, plt):
    # Preserve order by taking lists directly from the DataFrame
    x = df["Produkter"].to_list()
    y = df["Rentesats"].to_list()

    plt.figure(figsize=(12, 5))
    plt.plot(x, y, marker="o")  # no explicit colors/styles per your request
    plt.xlabel("Produkter")
    plt.ylabel("Rentesats")
    plt.title("Rentesatser pr. produkt (linjediagram, original rækkefølge)")
    plt.xticks(rotation=25, ha="right")
    plt.grid(True, axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.4
    Kan man sammenligne effektive rentesater for penge- og obligationsmarkedet?
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Svar:
    Det skal man være varsom med, da den effektive rentesats er en slags aritmetisk gennemsnitsforrentning der ikke tager højde for forskelle i løbetider.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.5
    Den effektive rente tager hensyn til rentes-rente effekten. Hvis den pålydende rente er 5% og der sker rentetilskrivning 4 gange om året, bliver den effektive rente da højere eller lavere end 5%?
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Svar:
    Den bliver højere. 
    Den kan ses af: 
    $$\beta$$ 
    """
    )
    return


@app.cell
def _():
    R = (1+0.05/4)**(4)
    print("Hvilket er lig med: ",R)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.6
    Bestem den direkte rente på en obligation med en pålydende kuponrente på 7%, der handles til kurs 105.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Svar:
    $$r_d = \frac{r}{D}$$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.7
    Afgør hvorvidt den effektive rente for obligationen i opgave 1.6 er højere eller lavere end obligationens direkte rente.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Svar: 
    asdas
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.8
    Bestem den nominelle rente, der kan forventes at være gældende om 1 år, hvis følgende fire scenarier er mulige: 
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    $$
    \begin{table}[]
    \begin{tabular}{lll}
    Scenarier                    & Rente & Sandsynlighed \\ \hline
    Lav vækst, ej ØMU deltagelse & 5\%   & 20\%          \\
    Lav vækst, ØMU deltagelse    & 3\%   & 30\%          \\
    Høj vækst, ej ØMU deltagelse & 8\%   & 10\%          \\
    Høj vækst, ØMU deltagelse    & 6\%   & 40\%         
    \end{tabular}
    \end{table}
    $$ 
    """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
