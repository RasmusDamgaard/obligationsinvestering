import marimo

__generated_with = "0.14.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import seaborn as sns
    from datetime import date
    from scipy.optimize import root_scalar
    return date, mo, pl, root_scalar, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Investeringsteori og obligationsmarkedet""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.1""")
    return


@app.cell
def _(pl):
    data = [
        pl.Series("Løbetid", [1997,1997,1998,1998,1999,1999,2000,2001,2003,2002,2004,2006,2007,2024]),
        pl.Series("Effektiv rente", [0.0418,0.0377,0.0362,0.0392,0.0402,0.0447,0.0488,0.0529,0.0585,0.0585,0.0628,0.0656,0.0676,0.0750])
    ]
    df = pl.DataFrame(data)
    return (df,)


@app.cell
def _(df):
    df2 = df.sort(by="Løbetid")
    df2
    return (df2,)


@app.cell
def _(df2, sns):
    sns.lineplot(data=df2, x="Løbetid", y="Effektiv rente")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.2""")
    return


@app.cell
def _():
    # Serie lån
    H = 100 # Hovedstol
    N = 5 # Terminer
    R = 0.05 # Kuponrente (nominelle rente)
    return H, N, R


@app.function
def payment_s(H,N,R,t):
    """
    returns period t payment on series loan
    """
    y = H/N + R*(1 - (t-1)/N)*H
    return y


@app.function
def interest_s(H,N,R,t):
    """
    returns period t interest rate on series loan
    """
    r = R*(1 - (t-1)/N)*H
    return r


@app.function
def installment_s(H,N):
    """
    returns period t installment
    """
    a = H/N 
    return a


@app.cell
def _(H, N, R, pl):
    series_loan = (
        pl.DataFrame({"t": range(1, 6)})  # t = 1..5
        .with_columns([
            (pl.lit(installment_s(H,N))).alias("Afdrag"),
            (interest_s(H,N,R,pl.col("t"))).alias("Rente"),
            (payment_s(H,N,R,pl.col("t"))).alias("Ydelse"),
        ])
    )

    return (series_loan,)


@app.cell
def _(series_loan):
    series_loan
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.3""")
    return


@app.cell
def _():
    # Stående lån
    H_stand = 100 # Hovedstol
    N_stand = 5 # Terminer
    R_stand = 0.07 # Kuponrente (nominelle rente)
    return H_stand, N_stand, R_stand


@app.cell
def _(H_stand, N_stand, R_stand, pl):
    standing_loan = (
        pl.DataFrame({"t": range(1, 6)})
        .with_columns(
            Afdrag = pl.when(pl.col("t") == N_stand)
                       .then(pl.lit(H_stand))
                       .otherwise(0),
            Rente  = H_stand * R_stand,
        )
        .with_columns(
            Ydelse = pl.col("Afdrag") + pl.col("Rente")
        )
    )
    return (standing_loan,)


@app.cell
def _(standing_loan):
    standing_loan
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.4""")
    return


@app.cell
def _():
    H_a = 100 # hovedstol
    n_a = 5 # løbetid i år
    R_a = 0.06 # kuponrente
    return H_a, R_a, n_a


@app.function
def alfahage(R,n):
    """
    Alfahage
    """
    alfahage = (1-(1+R)**(-n))/R
    return alfahage


@app.function
def annuity_installment(H,R,n,t):
    """
    Afdrag i annuitet
    """
    installment_a = (1+R)**(-1*(n+1-t))*H
    return installment_a


@app.cell
def _(H_a, R_a, n_a, pl):
    def annuity_loan(H,R,n):
        annuity_loan = (
            pl.DataFrame({"t": range(1, n_a + 1)})
            .with_columns(
                Ydelse = H_a / alfahage(R_a,n_a),
            )
            .with_columns(
                Restgæld = pl.col("Ydelse")*alfahage(R_a, n_a + 1 - pl.col("t"))
            )
            .with_columns(
                Rente = pl.col("Restgæld") * R_a
            )
            .with_columns(
                Afdrag = pl.col("Ydelse") - pl.col("Rente")
            )

        )
        return annuity_loan
    return (annuity_loan,)


@app.cell
def _(H_a, R_a, annuity_loan, n_a):
    ann_loan = annuity_loan(H_a,R_a,n_a)
    ann_loan
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.5""")
    return


@app.cell
def _():
    k0 = 0.98
    K = k0 * alfahage(R=0.06,n=5)
    K
    return (K,)


@app.cell
def _(K, root_scalar):
    # use scipy
    def g(x):
        return (1 - (1 + x)**(-5)) / x - K

    sol = root_scalar(g, bracket=(1e-9, 1.0), method='brentq')
    print(sol.root)  

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.6""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$
    k_0 = \frac{R}{\tilde{R}}+\frac{1}{n}\cdot (1-\frac{R}{\tilde{R}})\cdot \alpha_{n\rceil \tilde{R}}
    $$
    """
    )
    return


@app.cell
def _():
    k0_26 = 1.02
    n_26 = 5
    R_26 = 0.05
    return R_26, k0_26, n_26


@app.cell
def _(R_26, k0_26, n_26, root_scalar):
    def g_serie(x, K, R, n):
        return R/x + (1/n)*(1-R/x)*alfahage(R=x,n=n) - K

    sol_series = root_scalar(
        g_serie,
        args=(k0_26, R_26, n_26),
        method='newton',
        maxiter=1000,
        x0=0.05,
    )

    return g_serie, sol_series


@app.cell
def _(sol_series):
    R_26_tilde = print(sol_series.root)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.7""")
    return


@app.function
def serie_kurs(R,R_tilde,n):
    k = R/R_tilde + (1- R/R_tilde)*(1+R_tilde)**(-n)
    return k


@app.cell
def _(R_27_tilde):
    R_27_tilde
    return


@app.cell
def _():
    n_27 = 5
    R_27_tilde = 0.04266062709353395
    R_27 = [0.00, 0.03, 0.07, 0.10]
    return R_27, R_27_tilde, n_27


@app.cell
def _(R, R_27, R_27_tilde, n_27):
    for rente27 in R_27:
        k = serie_kurs(rente27, R_27_tilde, n_27)
        print("Ved kupon på: ", R,"% er kursen: ", k)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.8""")
    return


@app.cell
def _():
    n_28 = [4, 3, 2, 1]
    R_28 = 0.05
    return R_28, n_28


@app.cell
def _(R_27_tilde, R_28, n_28):
    for aar in n_28:
        kurs28 = serie_kurs(R_28, R_27_tilde, aar)
        print("Ved restløbetid på: ", aar,"år er kursen: ", kurs28)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.9""")
    return


@app.cell
def _():
    n_29 = 5
    R_29 = 0.05
    R_29_tilde = [0.01, 0.05, 0.10, 0.20]
    return R_29, R_29_tilde, n_29


@app.cell
def _(R_29, R_29_tilde, n_29):
    kurs_29 = []
    for r29t in R_29_tilde:
        kurs29 = serie_kurs(R_29, r29t, n_29)
        kurs_29.append(kurs29)
        print("Ved effektiv rente på: ", r29t," er kursen: ", kurs29)
    return (kurs_29,)


@app.cell
def _(R_29_tilde, kurs_29, pl, sns):
    df29 = pl.DataFrame({"Effektiv rente R_tilde": R_29_tilde, "Kurs": kurs_29})
    sns.lineplot(data=df29, x="Effektiv rente R_tilde", y="Kurs")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.10""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    $$
    v = \frac{R\cdot D}{D'\cdot n}
    $$
    """
    )
    return


@app.cell
def _(date):

    d1 = date(1997, 4, 10)
    d2 = date(1997, 12, 15)

    days_valør = (d2 - d1).days      # calendar days, start-exclusive, end-inclusive
    print(days_valør)

    d1t = date(1996, 12, 15)
    d2t = date(1997, 12 ,15)

    days_termin = (d2t - d1t).days      # calendar days, start-exclusive, end-inclusive
    print(days_termin)
    return days_termin, days_valør


@app.cell
def _():
    r210 = 0.07
    n210 = 1
    return n210, r210


@app.cell
def _(days_termin, days_valør, n210, r210):
    vedhæng_r = (r210*days_valør) / (days_termin*n210)
    print(vedhæng_r)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.11""")
    return


@app.cell
def _(date):
    d11 = date(1997, 4, 10)
    d22 = date(1997, 5, 15)

    days_valør11 = (d22 - d11).days      # calendar days, start-exclusive, end-inclusive
    print(days_valør11)
    return


@app.cell
def _():
    vedhæng_r_11 = (0.08 * 35)/(365 * 1)
    print(vedhæng_r_11)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.12""")
    return


@app.cell
def _():
    r212 = 0.07
    r212t = 0.0628
    k212 = 1.0435
    n212 = 7
    return k212, n212, r212, r212t


@app.cell
def _(k212, n212, r212, root_scalar):
    sol_stand212 = root_scalar(
        s_stand,
        args=(r212, k212, n212),
        method='newton',
        maxiter=1000,
        x0=0.05,
    )
    r_tilde_stand212 = print(sol_stand212.root)
    return (sol_stand212,)


@app.cell
def _(n212, r212, r212t):
    K212 = (r212/r212t) + (1-r212/r212t)*(1+r212t)**(-n212)
    print(K212)
    return (K212,)


@app.cell
def _(date):
    d112 = date(1996, 12, 15)
    d212 = date(1997, 1, 10)

    days_valør212 = (d212 - d112).days      # calendar days, start-exclusive, end-inclusive
    print(days_valør212)
    return (days_valør212,)


@app.cell
def _(days_valør212, r212):
    v212 = (r212*days_valør212)/(365*1)
    print(v212)
    return (v212,)


@app.cell
def _(sol_stand212, v212):
    print(sol_stand212.root + v212 )
    return


@app.cell
def _(K212, v212):
    K212 + v212
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Kan ikke få det til at stemme med en effektiv rente på 6,28%""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.13""")
    return


@app.function
def s_stand(x, r, k, n):
    return r/x + (1- r/x)*(1+x)**(-n) - k


@app.cell
def _(k_stand, n_stand, r_stand, root_scalar):
    sol_stand213 = root_scalar(
        s_stand,
        args=(r_stand, k_stand, n_stand),
        method='newton',
        maxiter=1000,
        x0=0.05,
    )
    r_tilde_stand213 = print(sol_stand213.root)
    return


@app.cell
def _():
    r_stand = 0.05
    k_stand = 0.9932
    n_stand = 3

    r_serie = 0.06
    k_serie = 1.02
    n_serie = 5
    return k_serie, k_stand, n_serie, n_stand, r_serie, r_stand


@app.cell
def _(g_serie, k_serie, n_serie, r_serie, root_scalar):
    sol_series213 = root_scalar(
        g_serie,
        args=(k_serie, r_serie, n_serie),
        method='newton',
        maxiter=1000,
        x0=0.05,
    )
    r_tilde_serie213 = print(sol_series213.root)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Stående lån har højest effektiv rente""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Opgave 2.14""")
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.15""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.16""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.17""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.18""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.19""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
