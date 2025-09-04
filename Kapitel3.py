import marimo

__generated_with = "0.14.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Kapitel 3: Risikomål""")
    return


@app.cell
def _():
    import marimo as mo
    from datetime import date
    from scipy.optimize import root_scalar
    return date, mo, root_scalar


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 3.1""")
    return


@app.cell
def _(date):
    # vedhængende rente (termin 15 november for danske statsobligationer)
    d1 = date(1996, 11, 15)
    d2 = date(1997, 1, 15)

    days_valør = (d2 - d1).days      # calendar days, start-exclusive, end-inclusive
    print("dage til valør:", days_valør)

    # dage til næste termin
    d3 = date(1997, 11, 15)
    days_termin = (d3 - d2).days 
    print("dage til næste termin:", days_termin)

    return days_termin, days_valør


@app.cell
def _(days_termin):
    t = days_termin/360
    return (t,)


@app.cell
def _(t):
    t
    return


@app.cell
def _(days_valør):
    vedhæng_r = (0.07*(days_valør-1)) / (360*1)
    print("vedhængende rente:", vedhæng_r)
    return


@app.function
def standing_loan_effective_rate(x, r, n, k):
    return r/x + (1- r/x)*(1+x)**(-n) - k


@app.cell
def _():
    n1 = 7
    r1 = 0.07
    k1 = 1.0435
    k2 = 1.0535
    k_v = k1
    return k2, k_v, n1, r1


@app.cell
def _(k_v, n1, r1, root_scalar):
    sol_stand1 = root_scalar(
        standing_loan_effective_rate,
        args=(r1, n1, k_v),
        method='newton',
        maxiter=1000,
        x0=0.07,
    )
    r_tilde_stand1 = print(sol_stand1.root)
    return (sol_stand1,)


@app.cell
def _(k2, n1, r1, root_scalar):
    sol_stand2 = root_scalar(
        standing_loan_effective_rate,
        args=(r1, n1, k2),
        method='newton',
        maxiter=1000,
        x0=0.07,
    )
    r_tilde_stand2 = print(sol_stand2.root)
    return (sol_stand2,)


@app.cell
def _(sol_stand1, sol_stand2):
    diff = sol_stand1.root - sol_stand2.root
    diff*100
    return


@app.cell
def _(t):
    def sumbetalingsrække(x):
        return 7/(1+x)**(t) + 7/(1+x)**(t+2) + 7/(1+x)**(t+3) + 7/(1+x)**(t+4) + 7/(1+x)**(t+5) + 7/(1+x)**(t+6) + 107/(1+x)**(t+7) - 104.35
    return (sumbetalingsrække,)


@app.cell
def _(root_scalar, sumbetalingsrække):
    sum_betaling = root_scalar(
        sumbetalingsrække,
        method='newton',
        maxiter=1000,
        x0=0.05,
    )
    sum_betaling_sol= print(sum_betaling.root)
    return


@app.function
def stående_kurs(Rs, Rs_tilde, sn):
    return Rs/Rs_tilde + (1 - Rs/Rs_tilde)*(1+Rs_tilde)**(-sn)


@app.cell
def _():
    kurs = stående_kurs(0.07,0.0628,7)
    return (kurs,)


@app.cell
def _(kurs):
    kurs
    return


@app.cell
def _(kurs):
    opg_vedhæng = 1.0435 - kurs
    opg_vedhæng
    return


@app.cell
def _(kurs, root_scalar):
    sol_stand3 = root_scalar(
        standing_loan_effective_rate,
        args=(0.07, 7, kurs),
        method='newton',
        maxiter=1000,
        x0=0.07,
    )
    r_tilde_stand3 = print(sol_stand3.root)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""så vedhængende rente ifølge opg formulering må være 0.004.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Jeg kan ikke få obligationen til at give en effektiv rente på 6,28% som nævnt i opgavebeskrivelsen. Hverken med eller uden vedhængende rente. Jeg får i stedet en korrektionsfaktor på 0,17.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 3.2""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Korrektionsfaktoren har en række svagheder som risikomål:""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    * Korrektionsfaktoren udtrykker den absolutte ændring i den effektive rente ved en ændring i kursen (hvor varigheden udtrykker procentvise ændringer)
    * Varighed kan derfor sammenligne forskellige obligationstyper i modsætning til korrektionsfaktoren.
    * Korrektionsfaktoren angiver kursrisikoen men tager ikke hensyn til geninvesteringsrisikoen (hvilket varigheden derimod gør)
    * grundlæggende bygger korrektionsfaktoren på den effektive rente (en slags gennemsnitsrente) og lider derfor under begrænsningerne ved den effektive rente.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 3.3""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Varighedsbegrebet har forskellige fortolkninger:""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    * Udtryk for en obligations eller en portefølje af obligationers gennemsnitlige restløbetid
    * Den procentvise ændring i kursen på en obligation for en ændring på 1% i renten
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 3.4""")
    return


@app.cell
def _():
    # betalingsrække
    y34 = [7, 7, 7, 7, 7, 7, 107]
    r34 = 0.0628
    n34 = 7
    t34 = 0.844
    return r34, t34, y34


@app.function
def duration(r, y, dt):
    # r = effektiv årlig rente
    # y = liste over cashflows
    # dt = år pr. periode (fx 0.84444)
    N = len(y)
    num = sum((i + dt) * y[i] * (1+r)**(-(i + dt)) for i in range(0, N))
    den = sum(y[i] * (1+r)**(-(i + dt)) for i in range(0, N))
    return num / den


@app.cell
def _(y34):
    for i in range(0, len(y34)):
        print("Y:", y34[i], "i:", i)
    return


@app.cell
def _(r34, t34, y34):
    dur34 = duration(r34, y34, t34)
    return (dur34,)


@app.cell
def _(dur34):
    dur34
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Kan ikke få det til en varighed på 6.34""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 3.5""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Kursen vil falde med 6.34% hvis renten stiger 1%.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 3.6""")
    return


@app.function
def mod_duration(r, y, dt):
    # r = effektiv årlig rente
    # y = liste over cashflows
    # dt = år pr. periode (fx 0.84444)
    N = len(y)
    num = sum((i + dt) * y[i] * (1+r)**(-(i + dt)) for i in range(0, N))
    den = sum(y[i] * (1+r)**(-(i + dt)) for i in range(0, N))
    v = num / den
    return v/(1+r)


@app.cell
def _(r34, t34, y34):
    mod_v = mod_duration(r34, y34, t34)
    return (mod_v,)


@app.cell
def _(mod_v):
    mod_v
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 3.7""")
    return


@app.cell
def _(mod_v):
    mod_v2 = mod_v/2
    print(mod_v2, 1 - mod_v2/100)
    return (mod_v2,)


@app.cell
def _():
    k37 = 104.35
    return (k37,)


@app.cell
def _(k37, mod_v2):
    diff_k37 = k37*(1-mod_v2/100)
    diff_k37
    return


@app.cell
def _():
    ny_sum_k37 = stående_kurs(0.07, 0.0678,7)*100
    ny_sum_k37
    return


@app.function
def sumrække(x):
    return 7/(1+x) + 7/(1+x)**(2) + 7/(1+x)**(3) + 7/(1+x)**(4) + 7/(1+x)**(5) + 7/(1+x)**(6) + 107/(1+x)**(7)


@app.cell
def _():
    sum37 = sumrække(0.0678)
    sum37
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 3.8""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
