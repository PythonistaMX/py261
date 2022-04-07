import typer

app = typer.Typer()


@app.command()
def admincreate(email: str, password: str):
    '''Hola, Pepech'''
    typer.echo(f"Hello {email}")
    

@app.command()
def changepass(email: str, password: str):
    typer.echo(f"Hello {email}")    
    
    
if __name__ == "__main__":
    app()