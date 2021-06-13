from click.testing import CliRunner
from gumshoe.commands import create
from gumshoe.commands import complete
from gumshoe.commands import show
from gumshoe.commands import remove


def test_create():
    runner = CliRunner()
    response = runner.invoke(create.cli, ["brush-teeth", "daily"])
    assert response.exit_code == 0
    assert "New habit has been created!" in response.output

def test_complete():
    runner = CliRunner()
    response = runner.invoke(complete.cli, ["brush-teeth"])
    assert response.exit_code == 0
    assert "Habit brush-teeth completed 1 times" in response.output

def test_show():
    runner = CliRunner()
    response = runner.invoke(show.cli, ["-n", "brush-teeth"])
    assert response.exit_code == 0
    #make sure headers and one completed mark is found in output
    assert "Name" and "Target" and "Current Streak" and "Longest Streak" and u"\u25A0" in response.output

def test_remove():
    runner = CliRunner()
    response = runner.invoke(remove.cli, ["brush-teeth"],input="y")
    assert response.exit_code == 0
    assert "Habit removed successfully!" in response.output