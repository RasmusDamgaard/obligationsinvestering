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
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, pl, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.1
    Beskriv hvilke faktorer, der har indflydelse på renteniveauet.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    * Forbrugerenes valg mellem opsparing og forbrug i en simpel ligevægst model bestemmer renteniveauet. (Fishers intertemporale teori)
    * Inflation påvirker den nominelle rente
    * Forventet fremtidig inflation
    * Økonomisk politik (finanspolitik og pengepolitik)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""I Fishers intertemporale model vil øget produktivet skubbe produktionsmulighedskurven udaf. Det vil ikke ændre på forbrugerens præference men fører til øget forbrug i begge periode $\rightarrow$ ingen ændring i efterspørgsel og udbud af lån og dermed vil realrenten være uændret.""")
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


@app.cell(hide_code=True)
def _(pl):
    data = {"Produkter": ["Anfordringsindskud", "Indskud på 3 måneders opsigelse", "Indskud på 12 måneders opsigelse",
                         "Obligationsrente, 1 år", "Obligationsrente, 3 år", "Obligationsrente, 5 år", "Obligationsrente, 10 år",
                         "Obligationsrente, 30 år"],
           "Rentesats": [0.00, 0.5, 1.5, 3.00, 4.50, 5.50, 6.25, 6.75]}
    df = pl.DataFrame(data)
    return (df,)


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.4
    Kan man sammenligne effektive rentesater for penge- og obligationsmarkedet?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Svar:
    Ikke umiddelbart. Der er flere konventioner for hvordan den effektive rente beregnes. 1, Obligationsmarkedskonventionen $(1+R)^t-1$ samt, 2, pengemarkedskonventionen $(1+R\cdot t)-1$ og 3, en kontinuert beregningsmetode med løbende/kontinuert rentetilskrivning $e^{R\cdot t}-1$.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Svar:
    Den bliver højere. 
    Den kan ses af: 
    $$(1+0.05/4)^{4}-1 = 0.051 > 0.05$$
    """
    )
    return


@app.cell(hide_code=True)
def _():
    R = (1+0.05/4)**(4) - 1
    print("Hvilket er lig med: ",R)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.6
    Bestem den direkte rente på en obligation med en pålydende kuponrente på 7%, der handles til kurs 105.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Svar:
    $$r_d = \frac{r\cdot 100}{K}$$
    hvor $r_d$ er den direkte rente, $r$ er pålydende og $K$ er kurs.
    """
    )
    return


@app.cell
def _():
    r_d = 7*100/105
    print(f"{r_d:.2f}%")
    return (r_d,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.7
    Afgør hvorvidt den effektive rente for obligationen i opgave 1.6 er højere eller lavere end obligationens direkte rente.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Svar: 
    Effektiv rente er lig direkte rente plus kursregulering
    $E = r_d + v$
    """
    )
    return


@app.cell
def _(r_d):
    v = (100 - 105)/105
    e = r_d + v
    print(f"{e:.2f}%")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Den effektive rente er lavere end den direkte rente pga kursreguleringen.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.8
    Bestem den nominelle rente, der kan forventes at være gældende om 1 år, hvis følgende fire scenarier er mulige:
    """
    )
    return


@app.cell
def _(pl):
    data1_8 = [["Lav vækst, ØMU deltagelse",0.05,0.2],
            ["Lav vækst, ØMU deltagelse", 0.03, 0.3], 
            ["Høj vækst, ej ØMU deltagelse", 0.08, 0.1],
            ["Høj vækst, ØMU deltagelse", 0.06, 0.4]]
    df1_8 = pl.DataFrame(data1_8, schema=["Scenarier", "Rente", "Sandsynlighed"], orient="row")
    df1_8
    return (df1_8,)


@app.cell
def _(df1_8, pl):
    # sumproduct = Σ (a[i] * b[i])
    sumprod = df1_8.select( (pl.col("Rente") * pl.col("Sandsynlighed")).sum().alias("sumproduct") )
    # -> shape: (1, 1); use .item() to get the scalar:
    sumprod_value = sumprod.item()
    print("E(r): ",sumprod_value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 1.9""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Spørgsmål a.
    Økonomiens produktionsmulighedskurve er givet ved:
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""$$ C_2 = 105 - 0.0105\cdot C_1^2 $$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Illustrer produktionsmulighedskurven grafisk.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Svar:""")
    return


@app.cell
def _(np):
    c1 = np.linspace(0.1, 100, 1000)
    c2 = 105 - 0.0105 * c1**2
    return c1, c2


@app.cell
def _(c1, c2, plt):
    # Create the plot
    plt.figure()
    plt.plot(c1, c2, label=r"$C_2 = 105 - 0.0105\,C_1^2$")
    plt.xlabel(r"$C_1$")
    plt.ylabel(r"$C_2$")
    plt.title(r"Plot of $C_2 = 105 - 0.0105\,C_1^2$")
    plt.grid(True)
    plt.legend()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Spørgsmål b.
    Hvilken real vækstrate er der i økonomien mellem de to perioder, hvis hele produktionen i periode 1 investeres?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Svar:""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$C_2=0 \Rightarrow 105 =0.0105\cdot C_1^2 \\
    C_1 = \sqrt\frac{105}{0.0105} = 100 = Y_1$$
    """
    )
    return


@app.cell
def _(np):
    Y_1 = np.sqrt(105/0.0105)
    print(Y_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""$$ C_1 = 0 \Rightarrow C_2 = 105 = Y_2$$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""$$ g = \frac{Y_2-Y_1}{Y_1} = 0.05$$""")
    return


@app.cell
def _():
    g = (105-100)/100
    print(g)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Spørgsmål c.
    Forbrugerens indifferenskurvesæt kan repræsenteres ved følgende tre funktioner:
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$ I_1: C_2=3536 \cdot C_1^{-1} - 8.4 \\
    I_2: C_2 = 4536\cdot C_1^{-1} - 8.4 \\
    I_3: C_2 = 5536 \cdot C_1^{-1} - 8.4$$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Illustrer i samme figur disse indifferenskurver og bestem forbrugerens optimale forbrugskombination mellem de to perioder.""")
    return


@app.cell(hide_code=True)
def _(c1, np):
    # For the hyperbolas, avoid |C1| < 1 to keep values finite and readable
    mask = np.abs(c1) >= 1
    c1_hyp = c1[mask]

    I1 = 3536 * (c1_hyp**-1) - 8.4
    I2 = 4536 * (c1_hyp**-1) - 8.4
    I3 = 5536 * (c1_hyp**-1) - 8.4
    return I1, I2, I3, c1_hyp


@app.cell(hide_code=True)
def _(I1, I2, I3, c1, c1_hyp, c2, plt):
    plt.figure()

    # Plot parabola
    plt.plot(c1, c2, label=r"$C_2 = 105 - 0.0105\,C_1^2$")
    plt.plot(c1_hyp, I1, label=r"$I_1 = 3536\,C_1^{-1} - 8.4$")
    plt.plot(c1_hyp, I2, label=r"$I_2 = 4536\,C_1^{-1} - 8.4$")
    plt.plot(c1_hyp, I3, label=r"$I_3 = 5536\,C_1^{-1} - 8.4$")
    # Optional: show the vertical asymptote at C1 = 0
    plt.axvline(0, linestyle="--", linewidth=1)

    plt.xlabel(r"$C_1$")
    plt.ylabel(r"$C_2$ / $I$")
    plt.title(r"Produktionsmulighedslinje C1/C2 og indifferenskurver I")
    plt.grid(True)
    plt.legend()
    plt.ylim(0, 150)
    plt.xlim(0, 110)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Svar: 
    Find rødderne i tredjegradsligningen:
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$ 105 - 0.0105\cdot C_1^2 = 4536C_1^{-1} - 8.4 \Leftrightarrow \\
    (C_1 - 60)^2(C_1 + 120) = 0$$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Herfra ses at rod $C_1 = 60$ er skæring og det optimale forbrug i periode 1.
    Alternativt differentier $C_2$ mht. $C_1$ og sæt lig differenteret indifferenskurve $I_x$.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Forbrugsbundt er i ligevægt $(60,67.2)$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Spørgsmål d. 
    Bestem hvor stor opsparingen er, samt hvilket afkast denne opsparing giver mellem periode 1 og periode 2
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Differentier""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$
    C_2 = 105 - 0.0105\cdot C_1^2 \\
    \frac{\partial C_2}{\partial C_1} = -0.021\cdot C_1
    $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Ved $C_1=60$ er $1 + r = -0.021\cdot 60 = 1.26$ så $r=26\%$.""")
    return


@app.cell(hide_code=True)
def _(I1, I2, I3, c1, c1_hyp, c2, np, plt):
    plt.figure()

    # Plot parabola
    plt.plot(c1, c2, label=r"$C_2 = 105 - 0.0105\,C_1^2$")
    plt.plot(c1_hyp, I1, label=r"$I_1 = 3536\,C_1^{-1} - 8.4$")
    plt.plot(c1_hyp, I2, label=r"$I_2 = 4536\,C_1^{-1} - 8.4$")
    plt.plot(c1_hyp, I3, label=r"$I_3 = 5536\,C_1^{-1} - 8.4$")
    # plt.plot(c1, bb, label=r"B'B forbrugsmulighed med lån'")
    # Optional: show the vertical asymptote at C1 = 0
    plt.axvline(0, linestyle="--", linewidth=1)

    plt.xlabel(r"$C_1$")
    plt.ylabel(r"$C_2$ / $I$")
    plt.title(r"Produktionsmulighedslinje C1/C2 og indifferenskurver I")
    plt.grid(True)
    plt.legend()
    plt.ylim(0, 150)
    plt.xlim(0, 110)

    # Production (value-maximizing) point and return from tangency
    C1_star = 60.0
    C2_star = 105 - 0.0105 * C1_star**2   # 67.2
    one_plus_r = 0.021 * C1_star          # = 1.26
    Y1, Y2 = C1_star, C2_star

    # Budget line: C2 = B' - (1+r) * C1
    Bp = Y2 + one_plus_r * Y1             # 142.8
    c1_line = np.linspace(0, 120, 400)
    c2_line = Bp - one_plus_r * c1_line

    # Plot the borrowing/lending line
    plt.plot(c1_line, c2_line, linestyle="--",
             label=rf"Budget line: $C_2={Bp:.1f} - {one_plus_r:.2f}C_1$")

    # (optional) mark the production/endowment point
    plt.scatter([Y1], [Y2], s=40)
    plt.annotate("Production point", xy=(Y1, Y2), xytext=(Y1+3, Y2+6),
                 arrowprops=dict(arrowstyle="->", lw=1))

    # Ensure the line is visible to its x-axis intercept
    plt.xlim(0, 120)
    plt.ylim(0, 150)
    plt.legend()
    plt.show()
    return


@app.cell
def _(mo):
    mo.md(r"""The consumer is at optimum so no borrowing.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Spørgsmål e. 
    Bytteforholdet mellem forbrug i periode 1 og 2 er 26%, hvilket kan udtrykkes ved kapitalmarkedslinjen
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""$$ C_2 = 142.80 - 1.26 \cdot C_1$$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Indtegn kapitalmarkedslinjen og bestem forbrugerens optimale forbrugskombination ud fra følgende indifferenskurve:""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""$$ I_4: C_2 = 8064 \cdot C_1^{-1} - 58.8$$""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Svar: 
    Differentierer kapitalmarkedslinje og indifferenskurve og sætter lig hinanden.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$
    \frac{\partial C_2}{\partial C_1} = -1.26 \\
    \frac{\partial I_4}{\partial C_1} = -8064\cdot C_1^{-2} \\
    1.26\cdot C_1^2 = 8064 \Leftrightarrow \\ 
    C_1 = \sqrt{8064/1.26} = 80 = C_1^* \\
    C_2^* = 8064 / 80 - 58.8 = 42
    $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""$(C_1^*,C_2^*)=(80,42)$""")
    return


@app.cell
def _(np):
    c11 = np.linspace(0.1, 100, 1000)
    c22 = 142.8 - 1.26*c11
    return c11, c22


@app.cell
def _(c11):
    I11 = 8064 * (c11**-1) - 58.8
    return (I11,)


@app.cell
def _(I11, c1, c11, c2, c22, plt):
    plt.figure()

    # Plot parabola
    plt.plot(c1,c2)
    plt.plot(c11, c22)
    plt.plot(c11, I11)

    c1_star = 80.0
    c2_star = 42

    # plot tangency
    plt.scatter([c1_star], [c2_star], s=40)                     # optional
    plt.annotate("Tangency (80, 42)", xy=(c1_star, c2_star),    # optional
                 xytext=(c1_star+5, c2_star+10),
                 arrowprops=dict(arrowstyle="->", lw=1))

    plt.xlabel(r"$C_1$")
    plt.ylabel(r"$C_2$")
    plt.title(r"Produktionsmulighedslinje C1/C2 og indifferenskurven I")
    plt.grid(True)
    # plt.legend()
    plt.ylim(0, 150)
    plt.xlim(0, 110)
    plt.show()
    return c1_star, c2_star


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Spørgsmål f: 
    Bestem hvor meget forbrugeren vælger at låne i periode1, samt hvor meget dette lån betyder i mistet forbrugsmulighed i periode 2 og eftervis at den effektive låneomkostning svarer til bytteforholdet 26%
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Forbruger går fra $(60,67.2)$ til $(80,42)$. Låner derfor i første periode.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$
    L = 80 - 60 = 20 \\
    \triangle C_2 = 67.2 - 42 = 25.2
    $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Forbrugeren låner til ekstra forbrug på 20 i periode 1 på bekostning af et forbrug på 25.2 i periode 2. Det giver en effektiv rente på: """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$ \frac{25.2}{20} = 1.26 \rightarrow r = 0.26
    $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Spørgsmål g.
    Markedsrenten falder nu fra 26% til 5% givet ved følgende kapitalmarkedslinje. Indtegn i samme figur den nye kapitalmarkedslinie og bestem forbrugerens optimale forbrugkombination ud fra følgende indifferenskurve.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$ C_2 = 131.25 - 1.05 \cdot C_1 \\
    I_5: C_2 = 8505\cdot C_1^-1 -57.75
    $$
    """
    )
    return


@app.cell
def _(c11):
    c25 = 131.25 - 1.05*c11
    I5 = 8505/c11 - 57.75
    return I5, c25


@app.cell(hide_code=True)
def _(I11, I5, c1, c11, c1_star, c2, c22, c25, c2_star, plt):
    plt.figure()

    # Plot parabola
    plt.plot(c1,c2)
    plt.plot(c11, c22)
    plt.plot(c11, I11)
    plt.plot(c11, c25)
    plt.plot(c11,I5)
    c11_star = 80.0
    c22_star = 42

    # plot tangency
    plt.scatter([c1_star], [c2_star], s=40)                     # optional
    plt.annotate("Tangency (80, 42)", xy=(c1_star, c2_star),    # optional
                 xytext=(c1_star+5, c2_star+10),
                 arrowprops=dict(arrowstyle="->", lw=1))

    plt.xlabel(r"$C_1$")
    plt.ylabel(r"$C_2$")
    plt.title(r"Produktionsmulighedslinje C1/C2 og indifferenskurven I")
    plt.grid(True)
    # plt.legend()
    plt.ylim(0, 150)
    plt.xlim(0, 110)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$
    \frac{\partial C_2}{\partial C_1} = -1.05 \\
    \frac{\partial I_5}{\partial C_1} = -8505\cdot C_1^{-2} \Leftrightarrow \\
    C_1 = \sqrt{8505/1.05} = 90 \Rightarrow \\
    C_2 = 36.75
    $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Spørgsmål h.
    Kommenter forbrugerens reaktion på rentefaldet og illustrer hans efterspørgselskurve for låntagning som funktion af renten, hvis det forudsættes, at der er tale om en linær funktion og bestem ligevægtsrenten, når udbudskurven forlångivning er givet ved: 
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$ r = 0.5 + 0.5 \cdot L
    $$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Rente faldet får forbrugeren til at låne mere. Gider ikke lave resten af opgaven. Det optimale forbrug Y2 og Y1 ændrer sig også ved rentenfald. Regn dette og dærnest lav en ret linje a og b over de to punkter af optimalt forbrug du har fundet c1 og c2 og c11 og c22 og det giver en funktion for låne efterspørgsel som funktion af L. Dernæst sæt denne lig med udbuddet af lån og isoler L.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Har fået ChatGPT-5 til at lave et løsningsforslag herunder:""")
    return


@app.cell
def _(mo):
    mo.image(src="Images\\chatgpt5_solve1.PNG")
    return


@app.cell
def _(mo):
    mo.image(src="Images\\chatgpt5_solve2.PNG")
    return


@app.cell
def _(mo):
    mo.image(src="Images\\chatgpt5_solve3.PNG")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Opgave 1.10
    Bestem den forventede inflation, hvis den nominelle rente er 8%, og realrenten er 3%.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Svar: """)
    return


@app.cell
def _():
    pi = 1.08/1.03 - 1
    pi
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$(1+R) = (1+r)(1+\pi) \\
    1.08 = 1.03(1+\pi) \Rightarrow \\
    \pi = \frac{1.08}{1.03} -1 = 0.05$$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Forventet inflation på 5%""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 1.11""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Hvis låntagere og långivere ikke reagere ens på ændringer i forventet inflationen overvæltes inflationen ikke 1 til 1 i den nominelle rente.

    Skat kan også skævvride overvæltningen.

    Mundell-Tobin effekten hvor stigning i forventet inflation øger den private sektors incitament til øget opsparing da inflationen udhulder virksomhedernes formue. Øget opsparing vil presse realrenten ned.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 1.12""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    $$(1+R) = (1+(r- (\pi \cdot 0.2))(1+\pi) =  \\
    1+R = 1.02\cdot 1.05 \Rightarrow \\
    R = 1.071 -1 = 0.071$$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Den nominelle rente vil i så fald være 7,1%""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 1.13""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 1.14""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 1.15""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 1.16""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 1.17""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Spørgsmål a.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Spørgsmål b.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Spørgsmål c.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 1.18""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 1.19""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 1.20""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
