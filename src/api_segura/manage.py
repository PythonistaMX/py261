import typer

app = typer.Typer()


@app.command()
def createadmin(email: str, password: str):
    '''Hola, Josech'''
    typer.echo(f"Hello {email}")
    

@app.command()
def changepass(email: str, password: str):
    typer.echo(f"Hello {email}")    
    
    
if __name__ == "__main__":
    app()