import marimo

__generated_with = "0.14.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import seaborn as sns
    from scipy.optimize import root_scalar
    return mo, pl, root_scalar, sns


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
    print(sol.root)  # ≈ 0.067470596505053

    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.6""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.7""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.8""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.9""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.10""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.11""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.12""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.13""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Opgave 2.14""")
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
